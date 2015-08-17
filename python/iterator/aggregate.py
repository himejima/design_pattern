#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

# 抽象クラス
class Aggregate(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def iterator(self):
        pass
