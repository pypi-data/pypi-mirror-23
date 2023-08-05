# Copyright 2015 Cloudbase Solutions Srl
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Base Utility class for operations on Hyper-V.
"""

import time

from oslo_log import log as logging

from os_win._i18n import _
from os_win import _utils
from os_win import constants
from os_win import exceptions
from os_win.utils import baseutils

LOG = logging.getLogger(__name__)


class JobUtils(baseutils.BaseUtilsVirt):

    _CONCRETE_JOB_CLASS = "Msvm_ConcreteJob"

    _DEFAULT_JOB_TERMINATE_TIMEOUT = 15  # seconds
    _KILL_JOB_STATE_CHANGE_REQUEST = 5

    _completed_job_states = [constants.JOB_STATE_COMPLETED,
                             constants.JOB_STATE_TERMINATED,
                             constants.JOB_STATE_KILLED,
                             constants.JOB_STATE_COMPLETED_WITH_WARNINGS]

    def check_ret_val(self, ret_val, job_path, success_values=[0]):
        """Checks that the job represented by the given arguments succeeded.

        Some Hyper-V operations are not atomic, and will return a reference
        to a job. In this case, this method will wait for the job's
        completion.

        :param ret_val: integer, representing the return value of the job.
            if the value is WMI_JOB_STATUS_STARTED or WMI_JOB_STATE_RUNNING,
            a job_path cannot be None.
        :param job_path: string representing the WMI object path of a
            Hyper-V job.
        :param success_values: list of return values that can be considered
            successful. WMI_JOB_STATUS_STARTED and WMI_JOB_STATE_RUNNING
            values are ignored.
        :raises exceptions.HyperVException: if the given ret_val is
            WMI_JOB_STATUS_STARTED or WMI_JOB_STATE_RUNNING and the state of
            job represented by the given job_path is not
            WMI_JOB_STATE_COMPLETED, or if the given ret_val is not in the
            list of given success_values.
        """
        if ret_val in [constants.WMI_JOB_STATUS_STARTED,
                       constants.WMI_JOB_STATE_RUNNING]:
            return self._wait_for_job(job_path)
        elif ret_val not in success_values:
            raise exceptions.HyperVException(
                _('Operation failed with return value: %s') % ret_val)

    def _wait_for_job(self, job_path):
        """Poll WMI job state and wait for completion."""

        job_wmi_path = job_path.replace('\\', '/')
        job = self._get_wmi_obj(job_wmi_path)

        while job.JobState == constants.WMI_JOB_STATE_RUNNING:
            time.sleep(0.1)
            job = self._get_wmi_obj(job_wmi_path)

        if job.JobState != constants.WMI_JOB_STATE_COMPLETED:
            job_state = job.JobState
            if job.path().Class == "Msvm_ConcreteJob":
                err_sum_desc = job.ErrorSummaryDescription
                err_desc = job.ErrorDescription
                err_code = job.ErrorCode
                data = {'job_state': job_state,
                        'err_sum_desc': err_sum_desc,
                        'err_desc': err_desc,
                        'err_code': err_code}
                raise exceptions.HyperVException(
                    _("WMI job failed with status %(job_state)d. "
                      "Error details: %(err_sum_desc)s - %(err_desc)s - "
                      "Error code: %(err_code)d") % data)
            else:
                (error, ret_val) = job.GetError()
                if not ret_val and error:
                    data = {'job_state': job_state,
                            'error': error}
                    raise exceptions.HyperVException(
                        _("WMI job failed with status %(job_state)d. "
                          "Error details: %(error)s") % data)
                else:
                    raise exceptions.HyperVException(
                        _("WMI job failed with status %d. No error "
                          "description available") % job_state)
        desc = job.Description
        elap = job.ElapsedTime
        LOG.debug("WMI job succeeded: %(desc)s, Elapsed=%(elap)s",
                  {'desc': desc, 'elap': elap})
        return job

    def _get_pending_jobs_affecting_element(self, element,
                                            ignore_error_state=True):
        # Msvm_AffectedJobElement is in fact an association between
        # the affected element and the affecting job.
        mappings = self._conn.Msvm_AffectedJobElement(
            AffectedElement=element.path_())
        pending_jobs = []
        for mapping in mappings:
            try:
                if mapping.AffectingElement and not self._is_job_completed(
                        mapping.AffectingElement, ignore_error_state):
                    pending_jobs.append(mapping.AffectingElement)

            except exceptions.x_wmi as ex:
                # NOTE(claudiub): we can ignore "Not found" type exceptions.
                if not _utils._is_not_found_exc(ex):
                    raise

        return pending_jobs

    def _stop_jobs(self, element):
        pending_jobs = self._get_pending_jobs_affecting_element(
            element, ignore_error_state=False)
        for job in pending_jobs:
            try:
                if not job.Cancellable:
                    LOG.debug("Got request to terminate "
                              "non-cancelable job.")
                    continue
                elif job.JobState == constants.JOB_STATE_EXCEPTION:
                    LOG.debug("Attempting to terminate exception state job.")

                job.RequestStateChange(
                    self._KILL_JOB_STATE_CHANGE_REQUEST)
            except exceptions.x_wmi as ex:
                # The job may had been completed right before we've
                # attempted to kill it.
                if not _utils._is_not_found_exc(ex):
                    LOG.debug("Failed to stop job. Exception: %s", ex)

        pending_jobs = self._get_pending_jobs_affecting_element(element)
        if pending_jobs:
            LOG.debug("Attempted to terminate jobs "
                      "affecting element %(element)s but "
                      "%(pending_count)s jobs are still pending.",
                      dict(element=element,
                           pending_count=len(pending_jobs)))
            raise exceptions.JobTerminateFailed()

    def _is_job_completed(self, job, ignore_error_state=True):
        return (job.JobState in self._completed_job_states or
                (job.JobState == constants.JOB_STATE_EXCEPTION and
                 ignore_error_state))

    def stop_jobs(self, element, timeout=_DEFAULT_JOB_TERMINATE_TIMEOUT):
        """Stops the Hyper-V jobs associated with the given resource.

        :param element: string representing the path of the Hyper-V resource
            whose jobs will be stopped.
        :param timeout: the maximum amount of time allowed to stop all the
            given resource's jobs.
        :raises exceptions.JobTerminateFailed: if there are still pending jobs
            associated with the given resource and the given timeout amount of
            time has passed.
        """
        @_utils.retry_decorator(exceptions=exceptions.JobTerminateFailed,
                                timeout=timeout, max_retry_count=None)
        def _stop_jobs_with_timeout():
            self._stop_jobs(element)

        _stop_jobs_with_timeout()

    @_utils.not_found_decorator
    @_utils.retry_decorator(exceptions=exceptions.HyperVException)
    def add_virt_resource(self, virt_resource, parent):
        (job_path, new_resources,
         ret_val) = self._vs_man_svc.AddResourceSettings(
            parent.path_(), [virt_resource.GetText_(1)])
        self.check_ret_val(ret_val, job_path)
        return new_resources

    # modify_virt_resource can fail, especially while setting up the VM's
    # serial port connection. Retrying the operation will yield success.
    @_utils.not_found_decorator
    @_utils.retry_decorator(exceptions=exceptions.HyperVException)
    def modify_virt_resource(self, virt_resource):
        (job_path, out_set_data,
         ret_val) = self._vs_man_svc.ModifyResourceSettings(
            ResourceSettings=[virt_resource.GetText_(1)])
        self.check_ret_val(ret_val, job_path)

    def remove_virt_resource(self, virt_resource):
        self.remove_multiple_virt_resources([virt_resource])

    @_utils.not_found_decorator
    @_utils.retry_decorator(exceptions=exceptions.HyperVException)
    def remove_multiple_virt_resources(self, virt_resources):
        (job, ret_val) = self._vs_man_svc.RemoveResourceSettings(
            ResourceSettings=[r.path_() for r in virt_resources])
        self.check_ret_val(ret_val, job)

    def add_virt_feature(self, virt_feature, parent):
        self.add_multiple_virt_features([virt_feature], parent)

    @_utils.not_found_decorator
    @_utils.retry_decorator(exceptions=exceptions.HyperVException)
    def add_multiple_virt_features(self, virt_features, parent):
        (job_path, out_set_data,
         ret_val) = self._vs_man_svc.AddFeatureSettings(
            parent.path_(), [f.GetText_(1) for f in virt_features])
        self.check_ret_val(ret_val, job_path)

    def remove_virt_feature(self, virt_feature):
        self.remove_multiple_virt_features([virt_feature])

    @_utils.not_found_decorator
    def remove_multiple_virt_features(self, virt_features):
        (job_path, ret_val) = self._vs_man_svc.RemoveFeatureSettings(
            FeatureSettings=[f.path_() for f in virt_features])
        self.check_ret_val(ret_val, job_path)
