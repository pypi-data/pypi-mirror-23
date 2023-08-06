# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import

import abc

import six


@six.add_metaclass(abc.ABCMeta)
class TableWriterInterface(object):
    """
    Interface class for a writing table.
    """

    @abc.abstractproperty
    def format_name(self):  # pragma: no cover
        pass

    @abc.abstractproperty
    def support_split_write(self):  # pragma: no cover
        pass

    @abc.abstractmethod
    def write_table(self):  # pragma: no cover
        pass

    @abc.abstractmethod
    def write_table_iter(self):  # pragma: no cover
        pass

    @abc.abstractmethod
    def close(self):  # pragma: no cover
        pass

    @abc.abstractmethod
    def _write_value_row_separator(self):  # pragma: no cover
        pass


@six.add_metaclass(abc.ABCMeta)
class TextWriterInterface(object):
    """
    Interface class for writing texts.
    """

    @abc.abstractmethod
    def write_null_line(self):  # pragma: no cover
        pass


@six.add_metaclass(abc.ABCMeta)
class BinaryWriterInterface(object):

    @abc.abstractmethod
    def open(self, file_path):  # pragma: no cover
        pass


@six.add_metaclass(abc.ABCMeta)
class IndentationInterface(object):
    """
    Interface class for indentation methods.
    """

    @abc.abstractmethod
    def set_indent_level(self, indent_level):  # pragma: no cover
        pass

    @abc.abstractmethod
    def inc_indent_level(self):  # pragma: no cover
        pass

    @abc.abstractmethod
    def dec_indent_level(self):  # pragma: no cover
        pass
