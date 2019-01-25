# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class LicenseKey(TeamCityObject):
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
        'valid': 'bool',
        'active': 'bool',
        'expired': 'bool',
        'obsolete': 'bool',
        'expiration_date': 'str',
        'maintenance_end_date': 'str',
        'type': 'str',
        'servers': 'int',
        'agents': 'int',
        'unlimited_agents': 'bool',
        'build_types': 'int',
        'unlimited_build_types': 'bool',
        'error_details': 'str',
        'key': 'str',
        'raw_type': 'str'
    }

    attribute_map = {
        'valid': 'valid',
        'active': 'active',
        'expired': 'expired',
        'obsolete': 'obsolete',
        'expiration_date': 'expirationDate',
        'maintenance_end_date': 'maintenanceEndDate',
        'type': 'type',
        'servers': 'servers',
        'agents': 'agents',
        'unlimited_agents': 'unlimitedAgents',
        'build_types': 'buildTypes',
        'unlimited_build_types': 'unlimitedBuildTypes',
        'error_details': 'errorDetails',
        'key': 'key',
        'raw_type': 'rawType'
    }

    def __init__(self, valid=False, active=False, expired=False, obsolete=False, expiration_date=None, maintenance_end_date=None, type=None, servers=None, agents=None, unlimited_agents=False, build_types=None, unlimited_build_types=False, error_details=None, key=None, raw_type=None, teamcity=None):  # noqa: E501
        """LicenseKey - a model defined in Swagger"""  # noqa: E501

        self._valid = None
        self._active = None
        self._expired = None
        self._obsolete = None
        self._expiration_date = None
        self._maintenance_end_date = None
        self._type = None
        self._servers = None
        self._agents = None
        self._unlimited_agents = None
        self._build_types = None
        self._unlimited_build_types = None
        self._error_details = None
        self._key = None
        self._raw_type = None
        self.discriminator = None

        if valid is not None:
            self.valid = valid
        if active is not None:
            self.active = active
        if expired is not None:
            self.expired = expired
        if obsolete is not None:
            self.obsolete = obsolete
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if maintenance_end_date is not None:
            self.maintenance_end_date = maintenance_end_date
        if type is not None:
            self.type = type
        if servers is not None:
            self.servers = servers
        if agents is not None:
            self.agents = agents
        if unlimited_agents is not None:
            self.unlimited_agents = unlimited_agents
        if build_types is not None:
            self.build_types = build_types
        if unlimited_build_types is not None:
            self.unlimited_build_types = unlimited_build_types
        if error_details is not None:
            self.error_details = error_details
        if key is not None:
            self.key = key
        if raw_type is not None:
            self.raw_type = raw_type
        super(LicenseKey, self).__init__(teamcity=teamcity)

    @property
    def valid(self):
        """Gets the valid of this LicenseKey.  # noqa: E501


        :return: The valid of this LicenseKey.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this LicenseKey.


        :param valid: The valid of this LicenseKey.  # noqa: E501
        :type: bool
        """

        self._valid = valid

    @property
    def active(self):
        """Gets the active of this LicenseKey.  # noqa: E501


        :return: The active of this LicenseKey.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this LicenseKey.


        :param active: The active of this LicenseKey.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def expired(self):
        """Gets the expired of this LicenseKey.  # noqa: E501


        :return: The expired of this LicenseKey.  # noqa: E501
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this LicenseKey.


        :param expired: The expired of this LicenseKey.  # noqa: E501
        :type: bool
        """

        self._expired = expired

    @property
    def obsolete(self):
        """Gets the obsolete of this LicenseKey.  # noqa: E501


        :return: The obsolete of this LicenseKey.  # noqa: E501
        :rtype: bool
        """
        return self._obsolete

    @obsolete.setter
    def obsolete(self, obsolete):
        """Sets the obsolete of this LicenseKey.


        :param obsolete: The obsolete of this LicenseKey.  # noqa: E501
        :type: bool
        """

        self._obsolete = obsolete

    @property
    def expiration_date(self):
        """Gets the expiration_date of this LicenseKey.  # noqa: E501


        :return: The expiration_date of this LicenseKey.  # noqa: E501
        :rtype: str
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this LicenseKey.


        :param expiration_date: The expiration_date of this LicenseKey.  # noqa: E501
        :type: str
        """

        self._expiration_date = expiration_date

    @property
    def maintenance_end_date(self):
        """Gets the maintenance_end_date of this LicenseKey.  # noqa: E501


        :return: The maintenance_end_date of this LicenseKey.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_end_date

    @maintenance_end_date.setter
    def maintenance_end_date(self, maintenance_end_date):
        """Sets the maintenance_end_date of this LicenseKey.


        :param maintenance_end_date: The maintenance_end_date of this LicenseKey.  # noqa: E501
        :type: str
        """

        self._maintenance_end_date = maintenance_end_date

    @property
    def type(self):
        """Gets the type of this LicenseKey.  # noqa: E501


        :return: The type of this LicenseKey.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LicenseKey.


        :param type: The type of this LicenseKey.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def servers(self):
        """Gets the servers of this LicenseKey.  # noqa: E501


        :return: The servers of this LicenseKey.  # noqa: E501
        :rtype: int
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this LicenseKey.


        :param servers: The servers of this LicenseKey.  # noqa: E501
        :type: int
        """

        self._servers = servers

    @property
    def agents(self):
        """Gets the agents of this LicenseKey.  # noqa: E501


        :return: The agents of this LicenseKey.  # noqa: E501
        :rtype: int
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this LicenseKey.


        :param agents: The agents of this LicenseKey.  # noqa: E501
        :type: int
        """

        self._agents = agents

    @property
    def unlimited_agents(self):
        """Gets the unlimited_agents of this LicenseKey.  # noqa: E501


        :return: The unlimited_agents of this LicenseKey.  # noqa: E501
        :rtype: bool
        """
        return self._unlimited_agents

    @unlimited_agents.setter
    def unlimited_agents(self, unlimited_agents):
        """Sets the unlimited_agents of this LicenseKey.


        :param unlimited_agents: The unlimited_agents of this LicenseKey.  # noqa: E501
        :type: bool
        """

        self._unlimited_agents = unlimited_agents

    @property
    def build_types(self):
        """Gets the build_types of this LicenseKey.  # noqa: E501


        :return: The build_types of this LicenseKey.  # noqa: E501
        :rtype: int
        """
        return self._build_types

    @build_types.setter
    def build_types(self, build_types):
        """Sets the build_types of this LicenseKey.


        :param build_types: The build_types of this LicenseKey.  # noqa: E501
        :type: int
        """

        self._build_types = build_types

    @property
    def unlimited_build_types(self):
        """Gets the unlimited_build_types of this LicenseKey.  # noqa: E501


        :return: The unlimited_build_types of this LicenseKey.  # noqa: E501
        :rtype: bool
        """
        return self._unlimited_build_types

    @unlimited_build_types.setter
    def unlimited_build_types(self, unlimited_build_types):
        """Sets the unlimited_build_types of this LicenseKey.


        :param unlimited_build_types: The unlimited_build_types of this LicenseKey.  # noqa: E501
        :type: bool
        """

        self._unlimited_build_types = unlimited_build_types

    @property
    def error_details(self):
        """Gets the error_details of this LicenseKey.  # noqa: E501


        :return: The error_details of this LicenseKey.  # noqa: E501
        :rtype: str
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this LicenseKey.


        :param error_details: The error_details of this LicenseKey.  # noqa: E501
        :type: str
        """

        self._error_details = error_details

    @property
    def key(self):
        """Gets the key of this LicenseKey.  # noqa: E501


        :return: The key of this LicenseKey.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LicenseKey.


        :param key: The key of this LicenseKey.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def raw_type(self):
        """Gets the raw_type of this LicenseKey.  # noqa: E501


        :return: The raw_type of this LicenseKey.  # noqa: E501
        :rtype: str
        """
        return self._raw_type

    @raw_type.setter
    def raw_type(self, raw_type):
        """Sets the raw_type of this LicenseKey.


        :param raw_type: The raw_type of this LicenseKey.  # noqa: E501
        :type: str
        """

        self._raw_type = raw_type
