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


class ASRResultDto(object):
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
        'score': 'str',
        'text': 'str'
    }

    attribute_map = {
        'score': 'score',
        'text': 'text'
    }

    def __init__(self, score=None, text=None):  # noqa: E501
        """ASRResultDto - a model defined in Swagger"""  # noqa: E501

        self._score = None
        self._text = None
        self.discriminator = None

        self.score = score
        self.text = text

    @property
    def score(self):
        """Gets the score of this ASRResultDto.  # noqa: E501

        Text score  # noqa: E501

        :return: The score of this ASRResultDto.  # noqa: E501
        :rtype: str
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ASRResultDto.

        Text score  # noqa: E501

        :param score: The score of this ASRResultDto.  # noqa: E501
        :type: str
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

    @property
    def text(self):
        """Gets the text of this ASRResultDto.  # noqa: E501

        Result text  # noqa: E501

        :return: The text of this ASRResultDto.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ASRResultDto.

        Result text  # noqa: E501

        :param text: The text of this ASRResultDto.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

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
        if not isinstance(other, ASRResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other