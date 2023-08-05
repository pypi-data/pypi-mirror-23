# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import
from __future__ import unicode_literals

from decimal import Decimal
import hashlib

import six
import typepy

import dataproperty as dp

from .error import InvalidDataError


class TableData(object):
    """
    Class to represent a table data structure.

    :param str table_name: Name of the table.
    :param list header_list: Table header names.
    :param list record_list: Table data records.
    """

    @property
    def table_name(self):
        """
        :return: Name of the table.
        :rtype: str
        """

        return self.__table_name

    @property
    def header_list(self):
        """
        :return: Table header names.
        :rtype: list
        """

        return self.__header_list

    @property
    def value_matrix(self):
        """
        :return: Table data records.
        :rtype: list
        """

        return self.__record_list

    @property
    def record_list(self):
        # alias property of value_matrix. this method will be deleted in the
        # future

        return self.value_matrix

    def __init__(
            self, table_name, header_list, record_list, is_strip_quote=False):

        self.__dp_extractor = dp.DataPropertyExtractor()
        self.__dp_extractor.strip_str_header = '"'
        if is_strip_quote:
            self.__dp_extractor.strip_str_value = '"'

        self.__table_name = table_name
        self.__header_list = header_list
        self.__record_list = self.__to_record_list(record_list)

    def __repr__(self):
        return "table_name={}, header_list={}, record_list={}".format(
            self.table_name, self.header_list, self.value_matrix)

    def __eq__(self, other):
        return all([
            self.table_name == other.table_name,
            self.header_list == other.header_list,
            all([
                all([
                    self.__compare_helper(lhs, rhs)
                    for lhs, rhs in zip(lhs_list, rhs_list)
                ])
                for lhs_list, rhs_list
                in zip(self.value_matrix, other.value_matrix)
            ]),
        ])

    def __ne__(self, other):
        return any([
            self.table_name != other.table_name,
            self.header_list != other.header_list,
            any([
                any([
                    not self.__compare_helper(lhs, rhs)
                    for lhs, rhs in zip(lhs_list, rhs_list)
                ])
                for lhs_list, rhs_list
                in zip(self.value_matrix, other.value_matrix)
            ]),
        ])

    def __hash__(self):
        body = (
            self.table_name +
            six.text_type(self.header_list) +
            six.text_type(self.value_matrix)
        )
        return hashlib.sha1(body.encode("utf-8")).hexdigest()

    def is_empty_header(self):
        """
        :return: |True| if the data :py:attr:`.header_list` is empty.
        :rtype: bool
        """

        return typepy.is_empty_sequence(self.header_list)

    def is_empty_record(self):
        """
        :return: |True| if the data :py:attr:`.value_matrix` is empty.
        :rtype: bool
        """

        return typepy.is_empty_sequence(self.value_matrix)

    def is_empty(self):
        """
        :return:
            |True| if the data :py:attr:`.header_list` or
            :py:attr:`.value_matrix` is empty.
        :rtype: bool
        """

        return any([self.is_empty_header(), self.is_empty_record()])

    def as_dict(self):
        """
        :return: Table data as a |dict| instance.
        :rtype: dict

        :Examples:

            .. code:: python

                from pytablereader import TableData

                TableData(
                    table_name="sample",
                    header_list=["a", "b"],
                    record_list=[[1, 2], [3.3, 4.4]]
                ).as_dict()

            .. code:: json

                {'sample': [{'a': 1, 'b': 2}, {'a': 3.3, 'b': 4.4}]}
        """

        self.__dp_extractor.float_type = float

        dict_body = []
        for value_list in self.value_matrix:
            if typepy.is_empty_sequence(value_list):
                continue

            dict_record = [
                (header, self.__dp_extractor.to_dataproperty(value).data)
                for header, value in zip(self.header_list, value_list)
                if value is not None
            ]

            if typepy.is_empty_sequence(dict_record):
                continue

            dict_body.append(dict(dict_record))

        return {self.table_name: dict_body}

    def asdict(self):
        return self.asdict()

        # alias to as_dict method.
        # this method will be deleted in the future.

    def as_dataframe(self):
        """
        :return: Table data as a ``pandas.DataFrame`` instance.
        :rtype: pandas.DataFrame

        :Examples:

            :ref:`example-as-dataframe`

        .. note::
            ``pandas`` package required to execute this method.
        """

        import pandas

        dataframe = pandas.DataFrame(self.value_matrix)
        if not self.is_empty_header():
            dataframe.columns = self.header_list

        return dataframe

    @staticmethod
    def from_dataframe(dataframe, table_name=""):
        """
        Initialize TableData instance from a pandas.DataFrame instance.

        :param pandas.DataFrame dataframe:
        :param str table_name: Table name to create.
        """

        return TableData(
            table_name=table_name,
            header_list=list(dataframe.columns.values),
            record_list=dataframe.values.tolist())

    def __compare_helper(self, lhs, rhs):
        from typepy.type import Nan

        if Nan(lhs).is_type() and Nan(rhs).is_type():
            return True

        return lhs == rhs

    def __to_record(self, values):
        """
        Convert values to a record.

        :param values: Value to be converted.
        :type values: |dict|/|namedtuple|/|list|/|tuple|
        :raises ValueError: If the ``value`` is invalid.
        """

        try:
            # dictionary to list
            return [
                self.__dp_extractor.to_dataproperty(values.get(header)).data
                for header in self.header_list
            ]
        except AttributeError:
            pass

        try:
            # namedtuple to list
            dict_value = values._asdict()
            return [
                self.__dp_extractor.to_dataproperty(
                    dict_value.get(header)).data
                for header in self.header_list
            ]
        except AttributeError:
            pass

        try:
            return [
                self.__dp_extractor.to_dataproperty(value).data
                for value in values
            ]
        except TypeError:
            raise InvalidDataError(
                "record must be a list or tuple: actual={}".format(values))

    def __to_record_list(self, record_list):
        """
        Convert matrix to records
        """

        self.__dp_extractor.float_type = Decimal

        if typepy.is_empty_sequence(self.header_list):
            return record_list

        return [
            self.__to_record(record)
            for record in record_list
        ]
