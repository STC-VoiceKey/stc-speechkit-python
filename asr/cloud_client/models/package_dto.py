# coding: utf-8

"""
    ASR documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.dev
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PackageDto(object):
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
        'package_id': 'str',
        'name': 'str',
        'language': 'str',
        'sample_rate': 'int',
        'loaded': 'bool'
    }

    attribute_map = {
        'package_id': 'package_id',
        'name': 'name',
        'language': 'language',
        'sample_rate': 'sample_rate',
        'loaded': 'loaded'
    }

    def __init__(self, package_id=None, name=None, language=None, sample_rate=None, loaded=None):  # noqa: E501
        """PackageDto - a model defined in Swagger"""  # noqa: E501

        self._package_id = None
        self._name = None
        self._language = None
        self._sample_rate = None
        self._loaded = None
        self.discriminator = None

        self.package_id = package_id
        self.name = name
        self.language = language
        self.sample_rate = sample_rate
        self.loaded = loaded

    @property
    def package_id(self):
        """Gets the package_id of this PackageDto.  # noqa: E501

        Package ID  # noqa: E501

        :return: The package_id of this PackageDto.  # noqa: E501
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this PackageDto.

        Package ID  # noqa: E501

        :param package_id: The package_id of this PackageDto.  # noqa: E501
        :type: str
        """
        if package_id is None:
            raise ValueError("Invalid value for `package_id`, must not be `None`")  # noqa: E501

        self._package_id = package_id

    @property
    def name(self):
        """Gets the name of this PackageDto.  # noqa: E501

        Package name  # noqa: E501

        :return: The name of this PackageDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PackageDto.

        Package name  # noqa: E501

        :param name: The name of this PackageDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def language(self):
        """Gets the language of this PackageDto.  # noqa: E501

        Package language  # noqa: E501

        :return: The language of this PackageDto.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PackageDto.

        Package language  # noqa: E501

        :param language: The language of this PackageDto.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def sample_rate(self):
        """Gets the sample_rate of this PackageDto.  # noqa: E501

        Required sample rate of data  # noqa: E501

        :return: The sample_rate of this PackageDto.  # noqa: E501
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this PackageDto.

        Required sample rate of data  # noqa: E501

        :param sample_rate: The sample_rate of this PackageDto.  # noqa: E501
        :type: int
        """
        if sample_rate is None:
            raise ValueError("Invalid value for `sample_rate`, must not be `None`")  # noqa: E501

        self._sample_rate = sample_rate

    @property
    def loaded(self):
        """Gets the loaded of this PackageDto.  # noqa: E501

        Is package loaded to the cache  # noqa: E501

        :return: The loaded of this PackageDto.  # noqa: E501
        :rtype: bool
        """
        return self._loaded

    @loaded.setter
    def loaded(self, loaded):
        """Sets the loaded of this PackageDto.

        Is package loaded to the cache  # noqa: E501

        :param loaded: The loaded of this PackageDto.  # noqa: E501
        :type: bool
        """
        if loaded is None:
            raise ValueError("Invalid value for `loaded`, must not be `None`")  # noqa: E501

        self._loaded = loaded

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PackageDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other