# coding: utf-8

from teamcity.custom.model import TeamcityObject


# from teamcity.models.backup_process import BackupProcess  # noqa: F401,E501


class BackupProcessManager(TeamCityObject):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'current_backup_process': 'BackupProcess'
    }

    attribute_map = {
        'current_backup_process': 'currentBackupProcess'
    }

    def __init__(self, current_backup_process=None):  # noqa: E501
        """BackupProcessManager - a model defined in Swagger"""  # noqa: E501
        super(BackupProcessManager, self).__init__()

        self._current_backup_process = None
        self.discriminator = None

        if current_backup_process is not None:
            self.current_backup_process = current_backup_process

    @property
    def current_backup_process(self):
        """Gets the current_backup_process of this BackupProcessManager.  # noqa: E501


        :return: The current_backup_process of this BackupProcessManager.  # noqa: E501
        :rtype: BackupProcess
        """
        return self._current_backup_process

    @current_backup_process.setter
    def current_backup_process(self, current_backup_process):
        """Sets the current_backup_process of this BackupProcessManager.


        :param current_backup_process: The current_backup_process of this BackupProcessManager.  # noqa: E501
        :type: BackupProcess
        """

        self._current_backup_process = current_backup_process

