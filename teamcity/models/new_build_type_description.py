# coding: utf-8

from teamcity.custom.model import TeamcityObject


# from teamcity.models.build_type import BuildType  # noqa: F401,E501
# from teamcity.models.properties import Properties  # noqa: F401,E501


class NewBuildTypeDescription(TeamCityObject):
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
        'build_types_ids_map': 'Properties',
        'copy_all_associated_settings': 'bool',
        'id': 'str',
        'name': 'str',
        'projects_ids_map': 'Properties',
        'source_build_type': 'BuildType',
        'source_build_type_locator': 'str',
        'vcs_roots_ids_map': 'Properties'
    }

    attribute_map = {
        'build_types_ids_map': 'buildTypesIdsMap',
        'copy_all_associated_settings': 'copyAllAssociatedSettings',
        'id': 'id',
        'name': 'name',
        'projects_ids_map': 'projectsIdsMap',
        'source_build_type': 'sourceBuildType',
        'source_build_type_locator': 'sourceBuildTypeLocator',
        'vcs_roots_ids_map': 'vcsRootsIdsMap'
    }

    def __init__(self, build_types_ids_map=None, copy_all_associated_settings=False, id=None, name=None, projects_ids_map=None, source_build_type=None, source_build_type_locator=None, vcs_roots_ids_map=None):  # noqa: E501
        """NewBuildTypeDescription - a model defined in Swagger"""  # noqa: E501
        super(NewBuildTypeDescription, self).__init__()

        self._build_types_ids_map = None
        self._copy_all_associated_settings = None
        self._id = None
        self._name = None
        self._projects_ids_map = None
        self._source_build_type = None
        self._source_build_type_locator = None
        self._vcs_roots_ids_map = None
        self.discriminator = None

        if build_types_ids_map is not None:
            self.build_types_ids_map = build_types_ids_map
        if copy_all_associated_settings is not None:
            self.copy_all_associated_settings = copy_all_associated_settings
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if projects_ids_map is not None:
            self.projects_ids_map = projects_ids_map
        if source_build_type is not None:
            self.source_build_type = source_build_type
        if source_build_type_locator is not None:
            self.source_build_type_locator = source_build_type_locator
        if vcs_roots_ids_map is not None:
            self.vcs_roots_ids_map = vcs_roots_ids_map

    @property
    def build_types_ids_map(self):
        """Gets the build_types_ids_map of this NewBuildTypeDescription.  # noqa: E501


        :return: The build_types_ids_map of this NewBuildTypeDescription.  # noqa: E501
        :rtype: Properties
        """
        return self._build_types_ids_map

    @build_types_ids_map.setter
    def build_types_ids_map(self, build_types_ids_map):
        """Sets the build_types_ids_map of this NewBuildTypeDescription.


        :param build_types_ids_map: The build_types_ids_map of this NewBuildTypeDescription.  # noqa: E501
        :type: Properties
        """

        self._build_types_ids_map = build_types_ids_map

    @property
    def copy_all_associated_settings(self):
        """Gets the copy_all_associated_settings of this NewBuildTypeDescription.  # noqa: E501


        :return: The copy_all_associated_settings of this NewBuildTypeDescription.  # noqa: E501
        :rtype: bool
        """
        return self._copy_all_associated_settings

    @copy_all_associated_settings.setter
    def copy_all_associated_settings(self, copy_all_associated_settings):
        """Sets the copy_all_associated_settings of this NewBuildTypeDescription.


        :param copy_all_associated_settings: The copy_all_associated_settings of this NewBuildTypeDescription.  # noqa: E501
        :type: bool
        """

        self._copy_all_associated_settings = copy_all_associated_settings

    @property
    def id(self):
        """Gets the id of this NewBuildTypeDescription.  # noqa: E501


        :return: The id of this NewBuildTypeDescription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NewBuildTypeDescription.


        :param id: The id of this NewBuildTypeDescription.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NewBuildTypeDescription.  # noqa: E501


        :return: The name of this NewBuildTypeDescription.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewBuildTypeDescription.


        :param name: The name of this NewBuildTypeDescription.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def projects_ids_map(self):
        """Gets the projects_ids_map of this NewBuildTypeDescription.  # noqa: E501


        :return: The projects_ids_map of this NewBuildTypeDescription.  # noqa: E501
        :rtype: Properties
        """
        return self._projects_ids_map

    @projects_ids_map.setter
    def projects_ids_map(self, projects_ids_map):
        """Sets the projects_ids_map of this NewBuildTypeDescription.


        :param projects_ids_map: The projects_ids_map of this NewBuildTypeDescription.  # noqa: E501
        :type: Properties
        """

        self._projects_ids_map = projects_ids_map

    @property
    def source_build_type(self):
        """Gets the source_build_type of this NewBuildTypeDescription.  # noqa: E501


        :return: The source_build_type of this NewBuildTypeDescription.  # noqa: E501
        :rtype: BuildType
        """
        return self._source_build_type

    @source_build_type.setter
    def source_build_type(self, source_build_type):
        """Sets the source_build_type of this NewBuildTypeDescription.


        :param source_build_type: The source_build_type of this NewBuildTypeDescription.  # noqa: E501
        :type: BuildType
        """

        self._source_build_type = source_build_type

    @property
    def source_build_type_locator(self):
        """Gets the source_build_type_locator of this NewBuildTypeDescription.  # noqa: E501


        :return: The source_build_type_locator of this NewBuildTypeDescription.  # noqa: E501
        :rtype: str
        """
        return self._source_build_type_locator

    @source_build_type_locator.setter
    def source_build_type_locator(self, source_build_type_locator):
        """Sets the source_build_type_locator of this NewBuildTypeDescription.


        :param source_build_type_locator: The source_build_type_locator of this NewBuildTypeDescription.  # noqa: E501
        :type: str
        """

        self._source_build_type_locator = source_build_type_locator

    @property
    def vcs_roots_ids_map(self):
        """Gets the vcs_roots_ids_map of this NewBuildTypeDescription.  # noqa: E501


        :return: The vcs_roots_ids_map of this NewBuildTypeDescription.  # noqa: E501
        :rtype: Properties
        """
        return self._vcs_roots_ids_map

    @vcs_roots_ids_map.setter
    def vcs_roots_ids_map(self, vcs_roots_ids_map):
        """Sets the vcs_roots_ids_map of this NewBuildTypeDescription.


        :param vcs_roots_ids_map: The vcs_roots_ids_map of this NewBuildTypeDescription.  # noqa: E501
        :type: Properties
        """

        self._vcs_roots_ids_map = vcs_roots_ids_map

