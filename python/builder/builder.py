#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Builder(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def make_title(self, title):
        pass

    @abstractmethod
    def make_string(self, str):
        pass

    @abstractmethod
    def make_items(self, items):
        pass

    @abstractmethod
    def closing(self):
        pass

