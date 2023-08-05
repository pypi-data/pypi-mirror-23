# Copyright 2014 Cloudbase Solutions Srl
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

import mock

from os_win.tests import test_base
from os_win.utils.storage.initiator import base_iscsi_utils


class BaseISCSIInitiatorUtilsTestCase(test_base.OsWinBaseTestCase):
    """Unit tests for the Hyper-V BaseISCSIInitiatorUtils class."""

    _FAKE_COMPUTER_NAME = "fake_computer_name"
    _FAKE_DOMAIN_NAME = "fake_domain_name"
    _FAKE_INITIATOR_NAME = "fake_initiator_name"
    _FAKE_INITIATOR_IQN_NAME = "iqn.1991-05.com.microsoft:fake_computer_name"
    _FAKE_DISK_PATH = 'fake_path DeviceID="123\\\\2"'
    _FAKE_MOUNT_DEVICE = '/dev/fake/mount'
    _FAKE_DEVICE_NAME = '/dev/fake/path'
    _FAKE_SWAP = {'device_name': _FAKE_DISK_PATH}

    def setUp(self):
        self._utils = base_iscsi_utils.BaseISCSIInitiatorUtils()
        self._utils._conn_wmi = mock.MagicMock()
        self._utils._conn_cimv2 = mock.MagicMock()

        super(BaseISCSIInitiatorUtilsTestCase, self).setUp()

    def test_get_iscsi_initiator_ok(self):
        self._check_get_iscsi_initiator(
            self._FAKE_INITIATOR_NAME)

    def test_get_iscsi_initiator_exception(self):
        initiator_name = "%(iqn)s.%(domain)s" % {
            'iqn': self._FAKE_INITIATOR_IQN_NAME,
            'domain': self._FAKE_DOMAIN_NAME
        }

        self._check_get_iscsi_initiator(initiator_name,
                                        side_effect=Exception)

    def _check_get_iscsi_initiator(self, expected=None, side_effect=None):
        mock_computer = mock.MagicMock()
        mock_computer.name = self._FAKE_COMPUTER_NAME
        mock_computer.Domain = self._FAKE_DOMAIN_NAME
        self._utils._conn_cimv2.Win32_ComputerSystem.return_value = [
            mock_computer]

        expected_key_path = (
            "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\"
            "iSCSI\\Discovery")

        with mock.patch.object(base_iscsi_utils,
                               'winreg', create=True) as mock_winreg:
            mock_winreg.CloseKey.side_effect = side_effect
            mock_winreg.QueryValueEx.return_value = [expected]
            mock_winreg.OpenKey.return_value = mock.sentinel.key

            initiator_name = self._utils.get_iscsi_initiator()
            self.assertEqual(expected, initiator_name)
            mock_winreg.OpenKey.assert_called_once_with(
                mock_winreg.HKEY_LOCAL_MACHINE,
                expected_key_path,
                0,
                mock_winreg.KEY_WOW64_64KEY + mock_winreg.KEY_ALL_ACCESS)
            mock_winreg.QueryValueEx.assert_called_once_with(
                mock.sentinel.key, "DefaultInitiatorName")
            mock_winreg.CloseKey.assert_called_once_with(mock.sentinel.key)

    def test_get_drive_number_from_disk_path(self):
        fake_disk_path = (
            '\\\\WIN-I5BTVHOIFGK\\root\\virtualization\\v2:Msvm_DiskDrive.'
            'CreationClassName="Msvm_DiskDrive",DeviceID="Microsoft:353B3BE8-'
            '310C-4cf4-839E-4E1B14616136\\\\1",SystemCreationClassName='
            '"Msvm_ComputerSystem",SystemName="WIN-I5BTVHOIFGK"')
        expected_disk_number = 1

        ret_val = self._utils._get_drive_number_from_disk_path(
            fake_disk_path)

        self.assertEqual(expected_disk_number, ret_val)

    def test_get_drive_number_not_found(self):
        fake_disk_path = 'fake_disk_path'

        ret_val = self._utils._get_drive_number_from_disk_path(
            fake_disk_path)

        self.assertFalse(ret_val)

    @mock.patch.object(base_iscsi_utils.BaseISCSIInitiatorUtils,
                       "_get_drive_number_from_disk_path")
    def test_get_session_id_from_mounted_disk(self, mock_get_session_id):
        mock_get_session_id.return_value = mock.sentinel.FAKE_DEVICE_NUMBER
        mock_initiator_session = self._create_initiator_session()
        mock_ses_class = self._utils._conn_wmi.MSiSCSIInitiator_SessionClass
        mock_ses_class.return_value = [mock_initiator_session]

        session_id = self._utils.get_session_id_from_mounted_disk(
            self._FAKE_DISK_PATH)

        self.assertEqual(mock.sentinel.FAKE_SESSION_ID, session_id)

    def test_get_devices_for_target(self):
        init_session = self._create_initiator_session()
        mock_ses_class = self._utils._conn_wmi.MSiSCSIInitiator_SessionClass
        mock_ses_class.return_value = [init_session]
        devices = self._utils._get_devices_for_target(
            mock.sentinel.FAKE_IQN)

        self.assertEqual(init_session.Devices, devices)

    def test_get_devices_for_target_not_found(self):
        mock_ses_class = self._utils._conn_wmi.MSiSCSIInitiator_SessionClass
        mock_ses_class.return_value = []
        devices = self._utils._get_devices_for_target(mock.sentinel.FAKE_IQN)

        self.assertEqual(0, len(devices))

    @mock.patch.object(base_iscsi_utils.BaseISCSIInitiatorUtils,
                       '_get_devices_for_target')
    def test_get_device_number_for_target(self, fake_get_devices):
        init_session = self._create_initiator_session()
        fake_get_devices.return_value = init_session.Devices
        mock_ses_class = self._utils._conn_wmi.MSiSCSIInitiator_SessionClass
        mock_ses_class.return_value = [init_session]
        device_number = self._utils.get_device_number_for_target(
            mock.sentinel.FAKE_IQN, mock.sentinel.FAKE_LUN)

        self.assertEqual(mock.sentinel.FAKE_DEVICE_NUMBER, device_number)

    @mock.patch.object(base_iscsi_utils.BaseISCSIInitiatorUtils,
                       '_get_devices_for_target')
    def test_get_target_lun_count(self, fake_get_devices):
        init_session = self._create_initiator_session()
        # Only disk devices are being counted.
        disk_device = mock.Mock(DeviceType=self._utils._FILE_DEVICE_DISK)
        init_session.Devices.append(disk_device)
        fake_get_devices.return_value = init_session.Devices

        lun_count = self._utils.get_target_lun_count(mock.sentinel.FAKE_IQN)

        self.assertEqual(1, lun_count)

    @mock.patch.object(base_iscsi_utils.BaseISCSIInitiatorUtils,
                       "_get_drive_number_from_disk_path")
    def test_get_target_from_disk_path(self, mock_get_session_id):
        mock_get_session_id.return_value = mock.sentinel.FAKE_DEVICE_NUMBER
        init_sess = self._create_initiator_session()
        mock_ses_class = self._utils._conn_wmi.MSiSCSIInitiator_SessionClass
        mock_ses_class.return_value = [init_sess]

        (target_name, scsi_lun) = self._utils.get_target_from_disk_path(
            self._FAKE_DISK_PATH)

        self.assertEqual(mock.sentinel.FAKE_TARGET_NAME, target_name)
        self.assertEqual(mock.sentinel.FAKE_LUN, scsi_lun)

    def _create_initiator_session(self):
        device = mock.MagicMock()
        device.ScsiLun = mock.sentinel.FAKE_LUN
        device.DeviceNumber = mock.sentinel.FAKE_DEVICE_NUMBER
        device.TargetName = mock.sentinel.FAKE_TARGET_NAME
        init_session = mock.MagicMock()
        init_session.Devices = [device]
        init_session.SessionId = mock.sentinel.FAKE_SESSION_ID

        return init_session
