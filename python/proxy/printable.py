#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Printable(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def set_printer_name(self, string):
        pass

    @abstractmethod
    def get_printer_name(self):
        pass

    @abstractmethod
    def printer(self, string):
        pass
