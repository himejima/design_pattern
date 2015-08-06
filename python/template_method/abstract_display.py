#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class AbstractDisplay(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def opening(self):
        pass

    @abstractmethod
    def printing(self):
        pass

    @abstractmethod
    def closing(self):
        pass

    def display(self):
        self.opening()

        for i in range(5):
            self.printing()

        self.closing()
