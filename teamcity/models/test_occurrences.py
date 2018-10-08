# coding: utf-8

from teamcity.custom.model import TeamcityObject


# from teamcity.models.test_occurrence import TestOccurrence  # noqa: F401,E501


class TestOccurrences(TeamCityObject):
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
        'default': 'bool',
        'failed': 'int',
        'href': 'str',
        'ignored': 'int',
        'muted': 'int',
        'new_failed': 'int',
        'next_href': 'str',
        'passed': 'int',
        'prev_href': 'str',
        'test_occurrence': 'list[TestOccurrence]'
    }

    attribute_map = {
        'count': 'count',
        'default': 'default',
        'failed': 'failed',
        'href': 'href',
        'ignored': 'ignored',
        'muted': 'muted',
        'new_failed': 'newFailed',
        'next_href': 'nextHref',
        'passed': 'passed',
        'prev_href': 'prevHref',
        'test_occurrence': 'testOccurrence'
    }

    def __init__(self, count=None, default=False, failed=None, href=None, ignored=None, muted=None, new_failed=None, next_href=None, passed=None, prev_href=None, test_occurrence=None):  # noqa: E501
        """TestOccurrences - a model defined in Swagger"""  # noqa: E501
        super(TestOccurrences, self).__init__()

        self._count = None
        self._default = None
        self._failed = None
        self._href = None
        self._ignored = None
        self._muted = None
        self._new_failed = None
        self._next_href = None
        self._passed = None
        self._prev_href = None
        self._test_occurrence = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if default is not None:
            self.default = default
        if failed is not None:
            self.failed = failed
        if href is not None:
            self.href = href
        if ignored is not None:
            self.ignored = ignored
        if muted is not None:
            self.muted = muted
        if new_failed is not None:
            self.new_failed = new_failed
        if next_href is not None:
            self.next_href = next_href
        if passed is not None:
            self.passed = passed
        if prev_href is not None:
            self.prev_href = prev_href
        if test_occurrence is not None:
            self.test_occurrence = test_occurrence

    @property
    def count(self):
        """Gets the count of this TestOccurrences.  # noqa: E501


        :return: The count of this TestOccurrences.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this TestOccurrences.


        :param count: The count of this TestOccurrences.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def default(self):
        """Gets the default of this TestOccurrences.  # noqa: E501


        :return: The default of this TestOccurrences.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this TestOccurrences.


        :param default: The default of this TestOccurrences.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def failed(self):
        """Gets the failed of this TestOccurrences.  # noqa: E501


        :return: The failed of this TestOccurrences.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this TestOccurrences.


        :param failed: The failed of this TestOccurrences.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def href(self):
        """Gets the href of this TestOccurrences.  # noqa: E501


        :return: The href of this TestOccurrences.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this TestOccurrences.


        :param href: The href of this TestOccurrences.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def ignored(self):
        """Gets the ignored of this TestOccurrences.  # noqa: E501


        :return: The ignored of this TestOccurrences.  # noqa: E501
        :rtype: int
        """
        return self._ignored

    @ignored.setter
    def ignored(self, ignored):
        """Sets the ignored of this TestOccurrences.


        :param ignored: The ignored of this TestOccurrences.  # noqa: E501
        :type: int
        """

        self._ignored = ignored

    @property
    def muted(self):
        """Gets the muted of this TestOccurrences.  # noqa: E501


        :return: The muted of this TestOccurrences.  # noqa: E501
        :rtype: int
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        """Sets the muted of this TestOccurrences.


        :param muted: The muted of this TestOccurrences.  # noqa: E501
        :type: int
        """

        self._muted = muted

    @property
    def new_failed(self):
        """Gets the new_failed of this TestOccurrences.  # noqa: E501


        :return: The new_failed of this TestOccurrences.  # noqa: E501
        :rtype: int
        """
        return self._new_failed

    @new_failed.setter
    def new_failed(self, new_failed):
        """Sets the new_failed of this TestOccurrences.


        :param new_failed: The new_failed of this TestOccurrences.  # noqa: E501
        :type: int
        """

        self._new_failed = new_failed

    @property
    def next_href(self):
        """Gets the next_href of this TestOccurrences.  # noqa: E501


        :return: The next_href of this TestOccurrences.  # noqa: E501
        :rtype: str
        """
        return self._next_href

    @next_href.setter
    def next_href(self, next_href):
        """Sets the next_href of this TestOccurrences.


        :param next_href: The next_href of this TestOccurrences.  # noqa: E501
        :type: str
        """

        self._next_href = next_href

    @property
    def passed(self):
        """Gets the passed of this TestOccurrences.  # noqa: E501


        :return: The passed of this TestOccurrences.  # noqa: E501
        :rtype: int
        """
        return self._passed

    @passed.setter
    def passed(self, passed):
        """Sets the passed of this TestOccurrences.


        :param passed: The passed of this TestOccurrences.  # noqa: E501
        :type: int
        """

        self._passed = passed

    @property
    def prev_href(self):
        """Gets the prev_href of this TestOccurrences.  # noqa: E501


        :return: The prev_href of this TestOccurrences.  # noqa: E501
        :rtype: str
        """
        return self._prev_href

    @prev_href.setter
    def prev_href(self, prev_href):
        """Sets the prev_href of this TestOccurrences.


        :param prev_href: The prev_href of this TestOccurrences.  # noqa: E501
        :type: str
        """

        self._prev_href = prev_href

    @property
    def test_occurrence(self):
        """Gets the test_occurrence of this TestOccurrences.  # noqa: E501


        :return: The test_occurrence of this TestOccurrences.  # noqa: E501
        :rtype: list[TestOccurrence]
        """
        return self._test_occurrence

    @test_occurrence.setter
    def test_occurrence(self, test_occurrence):
        """Sets the test_occurrence of this TestOccurrences.


        :param test_occurrence: The test_occurrence of this TestOccurrences.  # noqa: E501
        :type: list[TestOccurrence]
        """

        self._test_occurrence = test_occurrence

