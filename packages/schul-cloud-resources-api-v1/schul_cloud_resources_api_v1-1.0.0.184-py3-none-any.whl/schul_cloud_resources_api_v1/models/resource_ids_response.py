# coding: utf-8

"""
    Schul-Cloud Content API

    This is the specification for the content of Schul-Cloud. You can find more information in the [repository](https://github.com/schul-cloud/resources-api-v1). 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ResourceIdsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, jsonapi=None, links=None, data=None):
        """
        ResourceIdsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'jsonapi': 'Jsonapi',
            'links': 'ResourceIdsResponseLinks',
            'data': 'list[ResourceIdsResponseData]'
        }

        self.attribute_map = {
            'jsonapi': 'jsonapi',
            'links': 'links',
            'data': 'data'
        }

        self._jsonapi = jsonapi
        self._links = links
        self._data = data

    @property
    def jsonapi(self):
        """
        Gets the jsonapi of this ResourceIdsResponse.

        :return: The jsonapi of this ResourceIdsResponse.
        :rtype: Jsonapi
        """
        return self._jsonapi

    @jsonapi.setter
    def jsonapi(self, jsonapi):
        """
        Sets the jsonapi of this ResourceIdsResponse.

        :param jsonapi: The jsonapi of this ResourceIdsResponse.
        :type: Jsonapi
        """
        if jsonapi is None:
            raise ValueError("Invalid value for `jsonapi`, must not be `None`")

        self._jsonapi = jsonapi

    @property
    def links(self):
        """
        Gets the links of this ResourceIdsResponse.

        :return: The links of this ResourceIdsResponse.
        :rtype: ResourceIdsResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this ResourceIdsResponse.

        :param links: The links of this ResourceIdsResponse.
        :type: ResourceIdsResponseLinks
        """

        self._links = links

    @property
    def data(self):
        """
        Gets the data of this ResourceIdsResponse.

        :return: The data of this ResourceIdsResponse.
        :rtype: list[ResourceIdsResponseData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this ResourceIdsResponse.

        :param data: The data of this ResourceIdsResponse.
        :type: list[ResourceIdsResponseData]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ResourceIdsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
