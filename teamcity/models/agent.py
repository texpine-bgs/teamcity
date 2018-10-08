# coding: utf-8

from teamcity.custom.model import TeamcityObject


# from teamcity.models.agent_pool import AgentPool  # noqa: F401,E501
# from teamcity.models.authorized_info import AuthorizedInfo  # noqa: F401,E501
# from teamcity.models.build_types import BuildTypes  # noqa: F401,E501
# from teamcity.models.compatibilities import Compatibilities  # noqa: F401,E501
# from teamcity.models.enabled_info import EnabledInfo  # noqa: F401,E501
# from teamcity.models.properties import Properties  # noqa: F401,E501


class Agent(TeamCityObject):
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
        'authorized': 'bool',
        'authorized_info': 'AuthorizedInfo',
        'compatible_build_types': 'BuildTypes',
        'connected': 'bool',
        'enabled': 'bool',
        'enabled_info': 'EnabledInfo',
        'href': 'str',
        'id': 'int',
        'incompatible_build_types': 'Compatibilities',
        'ip': 'str',
        'locator': 'str',
        'name': 'str',
        'pool': 'AgentPool',
        'properties': 'Properties',
        'protocol': 'str',
        'type_id': 'int',
        'uptodate': 'bool'
    }

    attribute_map = {
        'authorized': 'authorized',
        'authorized_info': 'authorizedInfo',
        'compatible_build_types': 'compatibleBuildTypes',
        'connected': 'connected',
        'enabled': 'enabled',
        'enabled_info': 'enabledInfo',
        'href': 'href',
        'id': 'id',
        'incompatible_build_types': 'incompatibleBuildTypes',
        'ip': 'ip',
        'locator': 'locator',
        'name': 'name',
        'pool': 'pool',
        'properties': 'properties',
        'protocol': 'protocol',
        'type_id': 'typeId',
        'uptodate': 'uptodate'
    }

    def __init__(self, authorized=False, authorized_info=None, compatible_build_types=None, connected=False, enabled=False, enabled_info=None, href=None, id=None, incompatible_build_types=None, ip=None, locator=None, name=None, pool=None, properties=None, protocol=None, type_id=None, uptodate=False):  # noqa: E501
        """Agent - a model defined in Swagger"""  # noqa: E501
        super(Agent, self).__init__()

        self._authorized = None
        self._authorized_info = None
        self._compatible_build_types = None
        self._connected = None
        self._enabled = None
        self._enabled_info = None
        self._href = None
        self._id = None
        self._incompatible_build_types = None
        self._ip = None
        self._locator = None
        self._name = None
        self._pool = None
        self._properties = None
        self._protocol = None
        self._type_id = None
        self._uptodate = None
        self.discriminator = None

        if authorized is not None:
            self.authorized = authorized
        if authorized_info is not None:
            self.authorized_info = authorized_info
        if compatible_build_types is not None:
            self.compatible_build_types = compatible_build_types
        if connected is not None:
            self.connected = connected
        if enabled is not None:
            self.enabled = enabled
        if enabled_info is not None:
            self.enabled_info = enabled_info
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if incompatible_build_types is not None:
            self.incompatible_build_types = incompatible_build_types
        if ip is not None:
            self.ip = ip
        if locator is not None:
            self.locator = locator
        if name is not None:
            self.name = name
        if pool is not None:
            self.pool = pool
        if properties is not None:
            self.properties = properties
        if protocol is not None:
            self.protocol = protocol
        if type_id is not None:
            self.type_id = type_id
        if uptodate is not None:
            self.uptodate = uptodate

    @property
    def authorized(self):
        """Gets the authorized of this Agent.  # noqa: E501


        :return: The authorized of this Agent.  # noqa: E501
        :rtype: bool
        """
        return self._authorized

    @authorized.setter
    def authorized(self, authorized):
        """Sets the authorized of this Agent.


        :param authorized: The authorized of this Agent.  # noqa: E501
        :type: bool
        """

        self._authorized = authorized

    @property
    def authorized_info(self):
        """Gets the authorized_info of this Agent.  # noqa: E501


        :return: The authorized_info of this Agent.  # noqa: E501
        :rtype: AuthorizedInfo
        """
        return self._authorized_info

    @authorized_info.setter
    def authorized_info(self, authorized_info):
        """Sets the authorized_info of this Agent.


        :param authorized_info: The authorized_info of this Agent.  # noqa: E501
        :type: AuthorizedInfo
        """

        self._authorized_info = authorized_info

    @property
    def compatible_build_types(self):
        """Gets the compatible_build_types of this Agent.  # noqa: E501


        :return: The compatible_build_types of this Agent.  # noqa: E501
        :rtype: BuildTypes
        """
        return self._compatible_build_types

    @compatible_build_types.setter
    def compatible_build_types(self, compatible_build_types):
        """Sets the compatible_build_types of this Agent.


        :param compatible_build_types: The compatible_build_types of this Agent.  # noqa: E501
        :type: BuildTypes
        """

        self._compatible_build_types = compatible_build_types

    @property
    def connected(self):
        """Gets the connected of this Agent.  # noqa: E501


        :return: The connected of this Agent.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this Agent.


        :param connected: The connected of this Agent.  # noqa: E501
        :type: bool
        """

        self._connected = connected

    @property
    def enabled(self):
        """Gets the enabled of this Agent.  # noqa: E501


        :return: The enabled of this Agent.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Agent.


        :param enabled: The enabled of this Agent.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def enabled_info(self):
        """Gets the enabled_info of this Agent.  # noqa: E501


        :return: The enabled_info of this Agent.  # noqa: E501
        :rtype: EnabledInfo
        """
        return self._enabled_info

    @enabled_info.setter
    def enabled_info(self, enabled_info):
        """Sets the enabled_info of this Agent.


        :param enabled_info: The enabled_info of this Agent.  # noqa: E501
        :type: EnabledInfo
        """

        self._enabled_info = enabled_info

    @property
    def href(self):
        """Gets the href of this Agent.  # noqa: E501


        :return: The href of this Agent.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Agent.


        :param href: The href of this Agent.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this Agent.  # noqa: E501


        :return: The id of this Agent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Agent.


        :param id: The id of this Agent.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def incompatible_build_types(self):
        """Gets the incompatible_build_types of this Agent.  # noqa: E501


        :return: The incompatible_build_types of this Agent.  # noqa: E501
        :rtype: Compatibilities
        """
        return self._incompatible_build_types

    @incompatible_build_types.setter
    def incompatible_build_types(self, incompatible_build_types):
        """Sets the incompatible_build_types of this Agent.


        :param incompatible_build_types: The incompatible_build_types of this Agent.  # noqa: E501
        :type: Compatibilities
        """

        self._incompatible_build_types = incompatible_build_types

    @property
    def ip(self):
        """Gets the ip of this Agent.  # noqa: E501


        :return: The ip of this Agent.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Agent.


        :param ip: The ip of this Agent.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def locator(self):
        """Gets the locator of this Agent.  # noqa: E501


        :return: The locator of this Agent.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this Agent.


        :param locator: The locator of this Agent.  # noqa: E501
        :type: str
        """

        self._locator = locator

    @property
    def name(self):
        """Gets the name of this Agent.  # noqa: E501


        :return: The name of this Agent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Agent.


        :param name: The name of this Agent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pool(self):
        """Gets the pool of this Agent.  # noqa: E501


        :return: The pool of this Agent.  # noqa: E501
        :rtype: AgentPool
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this Agent.


        :param pool: The pool of this Agent.  # noqa: E501
        :type: AgentPool
        """

        self._pool = pool

    @property
    def properties(self):
        """Gets the properties of this Agent.  # noqa: E501


        :return: The properties of this Agent.  # noqa: E501
        :rtype: Properties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Agent.


        :param properties: The properties of this Agent.  # noqa: E501
        :type: Properties
        """

        self._properties = properties

    @property
    def protocol(self):
        """Gets the protocol of this Agent.  # noqa: E501


        :return: The protocol of this Agent.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Agent.


        :param protocol: The protocol of this Agent.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def type_id(self):
        """Gets the type_id of this Agent.  # noqa: E501


        :return: The type_id of this Agent.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this Agent.


        :param type_id: The type_id of this Agent.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    @property
    def uptodate(self):
        """Gets the uptodate of this Agent.  # noqa: E501


        :return: The uptodate of this Agent.  # noqa: E501
        :rtype: bool
        """
        return self._uptodate

    @uptodate.setter
    def uptodate(self, uptodate):
        """Sets the uptodate of this Agent.


        :param uptodate: The uptodate of this Agent.  # noqa: E501
        :type: bool
        """

        self._uptodate = uptodate

