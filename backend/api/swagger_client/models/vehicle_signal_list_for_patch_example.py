# coding: utf-8

"""
    Vehicle Booking API by e.GO Digital 

    Describes all backend endpoints.  # noqa: E501

    OpenAPI spec version: 2.0.5
    Contact: hello@e-go-digital.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VehicleSignalListForPatchExample(object):
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
        'location': 'str',
        'turn_signal_left': 'str',
        'turn_signal_right': 'str'
    }

    attribute_map = {
        'location': 'location',
        'turn_signal_left': 'turn_signal_left',
        'turn_signal_right': 'turn_signal_right'
    }

    def __init__(self, location=None, turn_signal_left=None, turn_signal_right=None):  # noqa: E501
        """VehicleSignalListForPatchExample - a model defined in Swagger"""  # noqa: E501

        self._location = None
        self._turn_signal_left = None
        self._turn_signal_right = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if turn_signal_left is not None:
            self.turn_signal_left = turn_signal_left
        if turn_signal_right is not None:
            self.turn_signal_right = turn_signal_right

    @property
    def location(self):
        """Gets the location of this VehicleSignalListForPatchExample.  # noqa: E501


        :return: The location of this VehicleSignalListForPatchExample.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this VehicleSignalListForPatchExample.


        :param location: The location of this VehicleSignalListForPatchExample.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def turn_signal_left(self):
        """Gets the turn_signal_left of this VehicleSignalListForPatchExample.  # noqa: E501


        :return: The turn_signal_left of this VehicleSignalListForPatchExample.  # noqa: E501
        :rtype: str
        """
        return self._turn_signal_left

    @turn_signal_left.setter
    def turn_signal_left(self, turn_signal_left):
        """Sets the turn_signal_left of this VehicleSignalListForPatchExample.


        :param turn_signal_left: The turn_signal_left of this VehicleSignalListForPatchExample.  # noqa: E501
        :type: str
        """

        self._turn_signal_left = turn_signal_left

    @property
    def turn_signal_right(self):
        """Gets the turn_signal_right of this VehicleSignalListForPatchExample.  # noqa: E501


        :return: The turn_signal_right of this VehicleSignalListForPatchExample.  # noqa: E501
        :rtype: str
        """
        return self._turn_signal_right

    @turn_signal_right.setter
    def turn_signal_right(self, turn_signal_right):
        """Sets the turn_signal_right of this VehicleSignalListForPatchExample.


        :param turn_signal_right: The turn_signal_right of this VehicleSignalListForPatchExample.  # noqa: E501
        :type: str
        """

        self._turn_signal_right = turn_signal_right

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
        if issubclass(VehicleSignalListForPatchExample, dict):
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
        if not isinstance(other, VehicleSignalListForPatchExample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other