#!/usr/bin/python
# -*- coding: utf-8 -*-_

from abc import ABCMeta, abstractmethod

class Factory(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def create_product(self, owner):
        pass

    @abstractmethod
    def register_product(self, product):
        pass

    def create(self, owner):
        self.__p = self.create_product(owner)
        self.register_product(self.__p)
        return self.__p
