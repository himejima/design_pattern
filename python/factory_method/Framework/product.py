#!/usr/bin/python
# -*- coding: utf-8 -*-_

from abc import ABCMeta, abstractmethod

class Product(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def use(self):
        pass
