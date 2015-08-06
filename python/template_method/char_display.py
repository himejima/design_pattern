#!/usr/bin/python
# -*- coding: utf-8 -*-

from abstract_display import AbstractDisplay

class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.__ch = ch

    def opening(self):
        print '<<'

    def printing(self):
        print self.__ch

    def closing(self):
        print '>>'
