# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse200(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, value: str=None):
        """
        InlineResponse200 - a model defined in Swagger

        :param value: The value of this InlineResponse200.
        :type value: str
        """
        self.swagger_types = {
            'value': str
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.
        :rtype: InlineResponse200
        """
        return deserialize_model(dikt, cls)

    @property
    def value(self) -> str:
        """
        Gets the value of this InlineResponse200.

        :return: The value of this InlineResponse200.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """
        Sets the value of this InlineResponse200.

        :param value: The value of this InlineResponse200.
        :type value: str
        """

        self._value = value
