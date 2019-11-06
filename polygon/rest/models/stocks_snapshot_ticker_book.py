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


class StocksSnapshotTickerBook(object):
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
        'ticker': 'str',
        'bids': 'list[StocksSnapshotBookItem]',
        'asks': 'list[StocksSnapshotBookItem]',
        'bid_count': 'int',
        'ask_count': 'int',
        'spread': 'int',
        'updated': 'int'
    }

    attribute_map = {
        'ticker': 'ticker',
        'bids': 'bids',
        'asks': 'asks',
        'bid_count': 'bidCount',
        'ask_count': 'askCount',
        'spread': 'spread',
        'updated': 'updated'
    }

    def __init__(self, ticker=None, bids=None, asks=None, bid_count=None, ask_count=None, spread=None, updated=None):  # noqa: E501
        """StocksSnapshotTickerBook - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._bids = None
        self._asks = None
        self._bid_count = None
        self._ask_count = None
        self._spread = None
        self._updated = None
        self.discriminator = None
        self.ticker = ticker
        if bids is not None:
            self.bids = bids
        if asks is not None:
            self.asks = asks
        if bid_count is not None:
            self.bid_count = bid_count
        if ask_count is not None:
            self.ask_count = ask_count
        if spread is not None:
            self.spread = spread
        self.updated = updated

    @property
    def ticker(self):
        """Gets the ticker of this StocksSnapshotTickerBook.  # noqa: E501

        Ticker of the object  # noqa: E501

        :return: The ticker of this StocksSnapshotTickerBook.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this StocksSnapshotTickerBook.

        Ticker of the object  # noqa: E501

        :param ticker: The ticker of this StocksSnapshotTickerBook.  # noqa: E501
        :type: str
        """
        if ticker is None:
            raise ValueError("Invalid value for `ticker`, must not be `None`")  # noqa: E501

        self._ticker = ticker

    @property
    def bids(self):
        """Gets the bids of this StocksSnapshotTickerBook.  # noqa: E501

        Bids  # noqa: E501

        :return: The bids of this StocksSnapshotTickerBook.  # noqa: E501
        :rtype: list[StocksSnapshotBookItem]
        """
        return self._bids

    @bids.setter
    def bids(self, bids):
        """Sets the bids of this StocksSnapshotTickerBook.

        Bids  # noqa: E501

        :param bids: The bids of this StocksSnapshotTickerBook.  # noqa: E501
        :type: list[StocksSnapshotBookItem]
        """

        self._bids = bids

    @property
    def asks(self):
        """Gets the asks of this StocksSnapshotTickerBook.  # noqa: E501

        Asks  # noqa: E501

        :return: The asks of this StocksSnapshotTickerBook.  # noqa: E501
        :rtype: list[StocksSnapshotBookItem]
        """
        return self._asks

    @asks.setter
    def asks(self, asks):
        """Sets the asks of this StocksSnapshotTickerBook.

        Asks  # noqa: E501

        :param asks: The asks of this StocksSnapshotTickerBook.  # noqa: E501
        :type: list[StocksSnapshotBookItem]
        """

        self._asks = asks

    @property
    def bid_count(self):
        """Gets the bid_count of this StocksSnapshotTickerBook.  # noqa: E501

        Combined total number of bids in the book  # noqa: E501

        :return: The bid_count of this StocksSnapshotTickerBook.  # noqa: E501
        :rtype: int
        """
        return self._bid_count

    @bid_count.setter
    def bid_count(self, bid_count):
        """Sets the bid_count of this StocksSnapshotTickerBook.

        Combined total number of bids in the book  # noqa: E501

        :param bid_count: The bid_count of this StocksSnapshotTickerBook.  # noqa: E501
        :type: int
        """

        self._bid_count = bid_count

    @property
    def ask_count(self):
        """Gets the ask_count of this StocksSnapshotTickerBook.  # noqa: E501

        Combined total number of asks in the book  # noqa: E501

        :return: The ask_count of this StocksSnapshotTickerBook.  # noqa: E501
        :rtype: int
        """
        return self._ask_count

    @ask_count.setter
    def ask_count(self, ask_count):
        """Sets the ask_count of this StocksSnapshotTickerBook.

        Combined total number of asks in the book  # noqa: E501

        :param ask_count: The ask_count of this StocksSnapshotTickerBook.  # noqa: E501
        :type: int
        """

        self._ask_count = ask_count

    @property
    def spread(self):
        """Gets the spread of this StocksSnapshotTickerBook.  # noqa: E501

        Difference between the best bid and the best ask price accross exchanges  # noqa: E501

        :return: The spread of this StocksSnapshotTickerBook.  # noqa: E501
        :rtype: int
        """
        return self._spread

    @spread.setter
    def spread(self, spread):
        """Sets the spread of this StocksSnapshotTickerBook.

        Difference between the best bid and the best ask price accross exchanges  # noqa: E501

        :param spread: The spread of this StocksSnapshotTickerBook.  # noqa: E501
        :type: int
        """

        self._spread = spread

    @property
    def updated(self):
        """Gets the updated of this StocksSnapshotTickerBook.  # noqa: E501

        Last Updated timestamp  # noqa: E501

        :return: The updated of this StocksSnapshotTickerBook.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this StocksSnapshotTickerBook.

        Last Updated timestamp  # noqa: E501

        :param updated: The updated of this StocksSnapshotTickerBook.  # noqa: E501
        :type: int
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

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
        if issubclass(StocksSnapshotTickerBook, dict):
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
        if not isinstance(other, StocksSnapshotTickerBook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
