# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.attribute import Attribute
from openapi_server.models.names import Names
from openapi_server import util

from openapi_server.models.attribute import Attribute  # noqa: E501
from openapi_server.models.names import Names  # noqa: E501

class Element(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, biolink_class=None, identifiers=None, names_synonyms=None, attributes=None, source=None):  # noqa: E501
        """Element - a model defined in OpenAPI

        :param id: The id of this Element.  # noqa: E501
        :type id: str
        :param biolink_class: The biolink_class of this Element.  # noqa: E501
        :type biolink_class: str
        :param identifiers: The identifiers of this Element.  # noqa: E501
        :type identifiers: Dict[str, object]
        :param names_synonyms: The names_synonyms of this Element.  # noqa: E501
        :type names_synonyms: List[Names]
        :param attributes: The attributes of this Element.  # noqa: E501
        :type attributes: List[Attribute]
        :param source: The source of this Element.  # noqa: E501
        :type source: str
        """
        self.openapi_types = {
            'id': str,
            'biolink_class': str,
            'identifiers': Dict[str, object],
            'names_synonyms': List[Names],
            'attributes': List[Attribute],
            'source': str
        }

        self.attribute_map = {
            'id': 'id',
            'biolink_class': 'biolink_class',
            'identifiers': 'identifiers',
            'names_synonyms': 'names_synonyms',
            'attributes': 'attributes',
            'source': 'source'
        }

        self._id = id
        self._biolink_class = biolink_class
        self._identifiers = identifiers
        self._names_synonyms = names_synonyms
        self._attributes = attributes
        self._source = source

    @classmethod
    def from_dict(cls, dikt) -> 'Element':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The element of this Element.  # noqa: E501
        :rtype: Element
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Element.

        Id of the gene.  # noqa: E501

        :return: The id of this Element.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Element.

        Id of the gene.  # noqa: E501

        :param id: The id of this Element.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def biolink_class(self):
        """Gets the biolink_class of this Element.

        BioLink class of the element.  # noqa: E501

        :return: The biolink_class of this Element.
        :rtype: str
        """
        return self._biolink_class

    @biolink_class.setter
    def biolink_class(self, biolink_class):
        """Sets the biolink_class of this Element.

        BioLink class of the element.  # noqa: E501

        :param biolink_class: The biolink_class of this Element.
        :type biolink_class: str
        """

        self._biolink_class = biolink_class

    @property
    def identifiers(self):
        """Gets the identifiers of this Element.


        :return: The identifiers of this Element.
        :rtype: Dict[str, object]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this Element.


        :param identifiers: The identifiers of this Element.
        :type identifiers: Dict[str, object]
        """

        self._identifiers = identifiers

    @property
    def names_synonyms(self):
        """Gets the names_synonyms of this Element.

        Names and synonyms of the element.  # noqa: E501

        :return: The names_synonyms of this Element.
        :rtype: List[Names]
        """
        return self._names_synonyms

    @names_synonyms.setter
    def names_synonyms(self, names_synonyms):
        """Sets the names_synonyms of this Element.

        Names and synonyms of the element.  # noqa: E501

        :param names_synonyms: The names_synonyms of this Element.
        :type names_synonyms: List[Names]
        """

        self._names_synonyms = names_synonyms

    @property
    def attributes(self):
        """Gets the attributes of this Element.

        Additional information about the element and provenance about collection membership.  # noqa: E501

        :return: The attributes of this Element.
        :rtype: List[Attribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Element.

        Additional information about the element and provenance about collection membership.  # noqa: E501

        :param attributes: The attributes of this Element.
        :type attributes: List[Attribute]
        """

        self._attributes = attributes

    @property
    def source(self):
        """Gets the source of this Element.

        Name of a transformer that added the element to the collection.  # noqa: E501

        :return: The source of this Element.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Element.

        Name of a transformer that added the element to the collection.  # noqa: E501

        :param source: The source of this Element.
        :type source: str
        """

        self._source = source
