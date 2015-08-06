#!/usr/bin/python
# -*- coding: utf-8 -*-

from abstract_display import AbstractDisplay

class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.__string = string
        self.__width = len(string)

    def opening(self):
        self.__print_line()

    def printing(self):
        print '|' + self.__string + '|'

    def closing(self):
        self.__print_line()

    def __print_line(self):
        print '+'

        for i in range(self.__width):
            print '-'

        print '+'

