# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Balance(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, email: str=None):  # noqa: E501
        """Balance - a model defined in Swagger

        :param email: The email of this Balance.  # noqa: E501
        :type email: str
        """
        self.swagger_types = {
            'email': str
        }

        self.attribute_map = {
            'email': 'email'
        }

        self._email = email

    @classmethod
    def from_dict(cls, dikt) -> 'Balance':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Balance of this Balance.  # noqa: E501
        :rtype: Balance
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self) -> str:
        """Gets the email of this Balance.


        :return: The email of this Balance.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this Balance.


        :param email: The email of this Balance.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email
