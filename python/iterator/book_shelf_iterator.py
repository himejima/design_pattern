#!/usr/bin/python
# -*- coding: utf-8 -*-

from iterator import Iterator

class BookShelfIterator(Iterator):
    def __init__(self, book_shelf):
        self.__book_shelf = book_shelf
        self.__index = 0

    def has_next(self):
        if self.__index < self.__book_shelf.get_length():
            return True
        else:
            return False

    def next(self):
        book = self.__book_shelf.get_book_at(self.__index)
        self.__index += 1
        return book
