# coding: utf-8

"""
    ASR documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cloud_client.models.word_dto import WordDto  # noqa: F401,E501


class ASRAdvancedResultDto(object):
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
        'channel_id': 'int',
        'result': 'list[WordDto]'
    }

    attribute_map = {
        'channel_id': 'channel_id',
        'result': 'result'
    }

    def __init__(self, channel_id=None, result=None):  # noqa: E501
        """ASRAdvancedResultDto - a model defined in Swagger"""  # noqa: E501

        self._channel_id = None
        self._result = None
        self.discriminator = None

        self.channel_id = channel_id
        self.result = result

    @property
    def channel_id(self):
        """Gets the channel_id of this ASRAdvancedResultDto.  # noqa: E501

        Channel id  # noqa: E501

        :return: The channel_id of this ASRAdvancedResultDto.  # noqa: E501
        :rtype: int
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this ASRAdvancedResultDto.

        Channel id  # noqa: E501

        :param channel_id: The channel_id of this ASRAdvancedResultDto.  # noqa: E501
        :type: int
        """
        if channel_id is None:
            raise ValueError("Invalid value for `channel_id`, must not be `None`")  # noqa: E501

        self._channel_id = channel_id

    @property
    def result(self):
        """Gets the result of this ASRAdvancedResultDto.  # noqa: E501

        Recognition result  # noqa: E501

        :return: The result of this ASRAdvancedResultDto.  # noqa: E501
        :rtype: list[WordDto]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ASRAdvancedResultDto.

        Recognition result  # noqa: E501

        :param result: The result of this ASRAdvancedResultDto.  # noqa: E501
        :type: list[WordDto]
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

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
        if not isinstance(other, ASRAdvancedResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
