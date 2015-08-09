#!/usr/bin/python
# -*- coding: utf-8 -*-

from banner import Banner
# from printer import Printer
# TODO: 継承するだけで良い？

class PrinterBanner(Banner):
    def __init__(self, string):
        super(PrinterBanner, self).__init__(string)

    def print_weak(self):
        # super(PrinterBanner, self).show_with_paren()
        self.show_with_paren()

    def print_strong(self):
        # super(PrinterBanner, self).show_with_aster()
        self.show_with_aster()
