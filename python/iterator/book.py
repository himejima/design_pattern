#!/usr/bin/python
# -*- coding: utf-8 -*-

class Book(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
