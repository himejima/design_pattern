#!/usr/bin/python
# -*- coding: utf-8 -*-

from banner import Banner
# from printer import Printer
# TODO: 継承するだけで良い？

class PrinterBanner(Banner):
    def __init__(self, string):
        self.__banner = Banner(string)

    def print_weak(self):
        self.__banner.show_with_paren()

    def print_strong(self):
        self.__banner.show_with_aster()
