# coding: utf-8

from teamcity.custom.model import TeamcityObject


# from teamcity.models.entry import Entry  # noqa: F401,E501


class Entries(TeamCityObject):
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
        'count': 'int',
        'entry': 'list[Entry]'
    }

    attribute_map = {
        'count': 'count',
        'entry': 'entry'
    }

    def __init__(self, count=None, entry=None):  # noqa: E501
        """Entries - a model defined in Swagger"""  # noqa: E501
        super(Entries, self).__init__()

        self._count = None
        self._entry = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if entry is not None:
            self.entry = entry

    @property
    def count(self):
        """Gets the count of this Entries.  # noqa: E501


        :return: The count of this Entries.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Entries.


        :param count: The count of this Entries.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def entry(self):
        """Gets the entry of this Entries.  # noqa: E501


        :return: The entry of this Entries.  # noqa: E501
        :rtype: list[Entry]
        """
        return self._entry

    @entry.setter
    def entry(self, entry):
        """Sets the entry of this Entries.


        :param entry: The entry of this Entries.  # noqa: E501
        :type: list[Entry]
        """

        self._entry = entry

