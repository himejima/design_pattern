#!/usr/bin/python
# -*- coding: utf-8 -*-

from aggregate import Aggregate
from book_shelf_iterator import BookShelfIterator

class BookShelf(Aggregate):
    def __init__(self, maxsize):
        self.__last = 0
        self.__books = [0 for i in range(maxsize)]

    def get_book_at(self, index):
        return self.__books[index]

    def append_book(self, book):
        self.__books[self.__last] = book
        self.__last += 1

    def get_length(self):
        return self.__last

    def iterator(self):
        return BookShelfIterator(self)
