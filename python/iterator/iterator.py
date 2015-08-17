#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Iterator(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next():
        pass

