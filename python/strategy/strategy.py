#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

# 抽象クラス
class Strategy(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def next_hand(self):
        pass

    @abstractmethod
    def study(self, win):
        pass


