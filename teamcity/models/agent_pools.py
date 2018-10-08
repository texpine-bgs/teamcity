# coding: utf-8

from teamcity.custom.model import TeamcityObject


# from teamcity.models.agent_pool import AgentPool  # noqa: F401,E501


class AgentPools(TeamCityObject):
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
        'agent_pool': 'list[AgentPool]',
        'count': 'int',
        'href': 'str',
        'next_href': 'str',
        'prev_href': 'str'
    }

    attribute_map = {
        'agent_pool': 'agentPool',
        'count': 'count',
        'href': 'href',
        'next_href': 'nextHref',
        'prev_href': 'prevHref'
    }

    def __init__(self, agent_pool=None, count=None, href=None, next_href=None, prev_href=None):  # noqa: E501
        """AgentPools - a model defined in Swagger"""  # noqa: E501
        super(AgentPools, self).__init__()

        self._agent_pool = None
        self._count = None
        self._href = None
        self._next_href = None
        self._prev_href = None
        self.discriminator = None

        if agent_pool is not None:
            self.agent_pool = agent_pool
        if count is not None:
            self.count = count
        if href is not None:
            self.href = href
        if next_href is not None:
            self.next_href = next_href
        if prev_href is not None:
            self.prev_href = prev_href

    @property
    def agent_pool(self):
        """Gets the agent_pool of this AgentPools.  # noqa: E501


        :return: The agent_pool of this AgentPools.  # noqa: E501
        :rtype: list[AgentPool]
        """
        return self._agent_pool

    @agent_pool.setter
    def agent_pool(self, agent_pool):
        """Sets the agent_pool of this AgentPools.


        :param agent_pool: The agent_pool of this AgentPools.  # noqa: E501
        :type: list[AgentPool]
        """

        self._agent_pool = agent_pool

    @property
    def count(self):
        """Gets the count of this AgentPools.  # noqa: E501


        :return: The count of this AgentPools.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this AgentPools.


        :param count: The count of this AgentPools.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def href(self):
        """Gets the href of this AgentPools.  # noqa: E501


        :return: The href of this AgentPools.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AgentPools.


        :param href: The href of this AgentPools.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def next_href(self):
        """Gets the next_href of this AgentPools.  # noqa: E501


        :return: The next_href of this AgentPools.  # noqa: E501
        :rtype: str
        """
        return self._next_href

    @next_href.setter
    def next_href(self, next_href):
        """Sets the next_href of this AgentPools.


        :param next_href: The next_href of this AgentPools.  # noqa: E501
        :type: str
        """

        self._next_href = next_href

    @property
    def prev_href(self):
        """Gets the prev_href of this AgentPools.  # noqa: E501


        :return: The prev_href of this AgentPools.  # noqa: E501
        :rtype: str
        """
        return self._prev_href

    @prev_href.setter
    def prev_href(self, prev_href):
        """Sets the prev_href of this AgentPools.


        :param prev_href: The prev_href of this AgentPools.  # noqa: E501
        :type: str
        """

        self._prev_href = prev_href

