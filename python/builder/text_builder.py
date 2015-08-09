#!/usr/bin/python
# -*- coding: utf-8 -*-
from builder import Builder

# TODO: stringに変換する
class TextBuilder(Builder):
    # TODO: bufferにいれる
    def __init__(self):
        self.__buffer = []

    def make_title(self, title):
        self.__buffer.append('=====')
        self.__buffer.append('『' + title + '』')
        

    def make_string(self, str):
        self.__buffer.append('▪️' + str + '\n')

    def make_items(self, items):
        for i in range(len(items)):
            self.__buffer.append('  ・' + items[i])

    def closing(self):
        self.__buffer.append('=====')

    def get_result(self):
        return self.__buffer
