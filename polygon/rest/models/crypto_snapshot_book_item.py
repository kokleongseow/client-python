# coding: utf-8

"""
    Polygon API

    The future of fintech.  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CryptoSnapshotBookItem(object):
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
        'p': 'int',
        'x': 'object'
    }

    attribute_map = {
        'p': 'p',
        'x': 'x'
    }

    def __init__(self, p=None, x=None):  # noqa: E501
        """CryptoSnapshotBookItem - a model defined in Swagger"""  # noqa: E501
        self._p = None
        self._x = None
        self.discriminator = None
        self.p = p
        self.x = x

    @property
    def p(self):
        """Gets the p of this CryptoSnapshotBookItem.  # noqa: E501

        Price of this book level  # noqa: E501

        :return: The p of this CryptoSnapshotBookItem.  # noqa: E501
        :rtype: int
        """
        return self._p

    @p.setter
    def p(self, p):
        """Sets the p of this CryptoSnapshotBookItem.

        Price of this book level  # noqa: E501

        :param p: The p of this CryptoSnapshotBookItem.  # noqa: E501
        :type: int
        """
        if p is None:
            raise ValueError("Invalid value for `p`, must not be `None`")  # noqa: E501

        self._p = p

    @property
    def x(self):
        """Gets the x of this CryptoSnapshotBookItem.  # noqa: E501

        Exchange to Size of this price level  # noqa: E501

        :return: The x of this CryptoSnapshotBookItem.  # noqa: E501
        :rtype: object
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this CryptoSnapshotBookItem.

        Exchange to Size of this price level  # noqa: E501

        :param x: The x of this CryptoSnapshotBookItem.  # noqa: E501
        :type: object
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

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
        if issubclass(CryptoSnapshotBookItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CryptoSnapshotBookItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
