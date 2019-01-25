# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.changes import Changes  # noqa: F401,E501
# from dohq_teamcity.models.file_changes import FileChanges  # noqa: F401,E501
# from dohq_teamcity.models.items import Items  # noqa: F401,E501
# from dohq_teamcity.models.user import User  # noqa: F401,E501
# from dohq_teamcity.models.vcs_root_instance import VcsRootInstance  # noqa: F401,E501


class Change(TeamCityObject):
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
        'id': 'int',
        'version': 'str',
        'internal_version': 'str',
        'username': 'str',
        '_date': 'str',
        'registration_date': 'str',
        'personal': 'bool',
        'href': 'str',
        'web_url': 'str',
        'comment': 'str',
        'user': 'User',
        'files': 'FileChanges',
        'vcs_root_instance': 'VcsRootInstance',
        'parent_changes': 'Changes',
        'parent_revisions': 'Items',
        'locator': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'internal_version': 'internalVersion',
        'username': 'username',
        '_date': 'date',
        'registration_date': 'registrationDate',
        'personal': 'personal',
        'href': 'href',
        'web_url': 'webUrl',
        'comment': 'comment',
        'user': 'user',
        'files': 'files',
        'vcs_root_instance': 'vcsRootInstance',
        'parent_changes': 'parentChanges',
        'parent_revisions': 'parentRevisions',
        'locator': 'locator'
    }

    def __init__(self, id=None, version=None, internal_version=None, username=None, _date=None, registration_date=None, personal=False, href=None, web_url=None, comment=None, user=None, files=None, vcs_root_instance=None, parent_changes=None, parent_revisions=None, locator=None, teamcity=None):  # noqa: E501
        """Change - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._version = None
        self._internal_version = None
        self._username = None
        self.__date = None
        self._registration_date = None
        self._personal = None
        self._href = None
        self._web_url = None
        self._comment = None
        self._user = None
        self._files = None
        self._vcs_root_instance = None
        self._parent_changes = None
        self._parent_revisions = None
        self._locator = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if internal_version is not None:
            self.internal_version = internal_version
        if username is not None:
            self.username = username
        if _date is not None:
            self._date = _date
        if registration_date is not None:
            self.registration_date = registration_date
        if personal is not None:
            self.personal = personal
        if href is not None:
            self.href = href
        if web_url is not None:
            self.web_url = web_url
        if comment is not None:
            self.comment = comment
        if user is not None:
            self.user = user
        if files is not None:
            self.files = files
        if vcs_root_instance is not None:
            self.vcs_root_instance = vcs_root_instance
        if parent_changes is not None:
            self.parent_changes = parent_changes
        if parent_revisions is not None:
            self.parent_revisions = parent_revisions
        if locator is not None:
            self.locator = locator
        super(Change, self).__init__(teamcity=teamcity)

    @property
    def id(self):
        """Gets the id of this Change.  # noqa: E501


        :return: The id of this Change.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Change.


        :param id: The id of this Change.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this Change.  # noqa: E501


        :return: The version of this Change.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Change.


        :param version: The version of this Change.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def internal_version(self):
        """Gets the internal_version of this Change.  # noqa: E501


        :return: The internal_version of this Change.  # noqa: E501
        :rtype: str
        """
        return self._internal_version

    @internal_version.setter
    def internal_version(self, internal_version):
        """Sets the internal_version of this Change.


        :param internal_version: The internal_version of this Change.  # noqa: E501
        :type: str
        """

        self._internal_version = internal_version

    @property
    def username(self):
        """Gets the username of this Change.  # noqa: E501


        :return: The username of this Change.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Change.


        :param username: The username of this Change.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def _date(self):
        """Gets the _date of this Change.  # noqa: E501


        :return: The _date of this Change.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Change.


        :param _date: The _date of this Change.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def registration_date(self):
        """Gets the registration_date of this Change.  # noqa: E501


        :return: The registration_date of this Change.  # noqa: E501
        :rtype: str
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        """Sets the registration_date of this Change.


        :param registration_date: The registration_date of this Change.  # noqa: E501
        :type: str
        """

        self._registration_date = registration_date

    @property
    def personal(self):
        """Gets the personal of this Change.  # noqa: E501


        :return: The personal of this Change.  # noqa: E501
        :rtype: bool
        """
        return self._personal

    @personal.setter
    def personal(self, personal):
        """Sets the personal of this Change.


        :param personal: The personal of this Change.  # noqa: E501
        :type: bool
        """

        self._personal = personal

    @property
    def href(self):
        """Gets the href of this Change.  # noqa: E501


        :return: The href of this Change.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Change.


        :param href: The href of this Change.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def web_url(self):
        """Gets the web_url of this Change.  # noqa: E501


        :return: The web_url of this Change.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this Change.


        :param web_url: The web_url of this Change.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

    @property
    def comment(self):
        """Gets the comment of this Change.  # noqa: E501


        :return: The comment of this Change.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Change.


        :param comment: The comment of this Change.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def user(self):
        """Gets the user of this Change.  # noqa: E501


        :return: The user of this Change.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Change.


        :param user: The user of this Change.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def files(self):
        """Gets the files of this Change.  # noqa: E501


        :return: The files of this Change.  # noqa: E501
        :rtype: FileChanges
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Change.


        :param files: The files of this Change.  # noqa: E501
        :type: FileChanges
        """

        self._files = files

    @property
    def vcs_root_instance(self):
        """Gets the vcs_root_instance of this Change.  # noqa: E501


        :return: The vcs_root_instance of this Change.  # noqa: E501
        :rtype: VcsRootInstance
        """
        return self._vcs_root_instance

    @vcs_root_instance.setter
    def vcs_root_instance(self, vcs_root_instance):
        """Sets the vcs_root_instance of this Change.


        :param vcs_root_instance: The vcs_root_instance of this Change.  # noqa: E501
        :type: VcsRootInstance
        """

        self._vcs_root_instance = vcs_root_instance

    @property
    def parent_changes(self):
        """Gets the parent_changes of this Change.  # noqa: E501


        :return: The parent_changes of this Change.  # noqa: E501
        :rtype: Changes
        """
        return self._parent_changes

    @parent_changes.setter
    def parent_changes(self, parent_changes):
        """Sets the parent_changes of this Change.


        :param parent_changes: The parent_changes of this Change.  # noqa: E501
        :type: Changes
        """

        self._parent_changes = parent_changes

    @property
    def parent_revisions(self):
        """Gets the parent_revisions of this Change.  # noqa: E501


        :return: The parent_revisions of this Change.  # noqa: E501
        :rtype: Items
        """
        return self._parent_revisions

    @parent_revisions.setter
    def parent_revisions(self, parent_revisions):
        """Sets the parent_revisions of this Change.


        :param parent_revisions: The parent_revisions of this Change.  # noqa: E501
        :type: Items
        """

        self._parent_revisions = parent_revisions

    @property
    def locator(self):
        """Gets the locator of this Change.  # noqa: E501


        :return: The locator of this Change.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this Change.


        :param locator: The locator of this Change.  # noqa: E501
        :type: str
        """

        self._locator = locator
