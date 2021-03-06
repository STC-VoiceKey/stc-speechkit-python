# coding: utf-8

"""
    SessionService documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.2.158
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AuthRequestDto(object):
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
        'username': 'str',
        'domain_id': 'int',
        'password': 'str'
    }

    attribute_map = {
        'username': 'username',
        'domain_id': 'domain_id',
        'password': 'password'
    }

    def __init__(self, username=None, domain_id=None, password=None):  # noqa: E501
        """AuthRequestDto - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._domain_id = None
        self._password = None
        self.discriminator = None

        self.username = username
        self.domain_id = domain_id
        self.password = password

    @property
    def username(self):
        """Gets the username of this AuthRequestDto.  # noqa: E501

        User name  # noqa: E501

        :return: The username of this AuthRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuthRequestDto.

        User name  # noqa: E501

        :param username: The username of this AuthRequestDto.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def domain_id(self):
        """Gets the domain_id of this AuthRequestDto.  # noqa: E501

        User domain  # noqa: E501

        :return: The domain_id of this AuthRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this AuthRequestDto.

        User domain  # noqa: E501

        :param domain_id: The domain_id of this AuthRequestDto.  # noqa: E501
        :type: int
        """
        if domain_id is None:
            raise ValueError("Invalid value for `domain_id`, must not be `None`")  # noqa: E501

        self._domain_id = domain_id

    @property
    def password(self):
        """Gets the password of this AuthRequestDto.  # noqa: E501

        User password - planed text  # noqa: E501

        :return: The password of this AuthRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AuthRequestDto.

        User password - planed text  # noqa: E501

        :param password: The password of this AuthRequestDto.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

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
        if not isinstance(other, AuthRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
