#!/usr/bin/python
# -*- coding: utf-8 -*-

from printable import Printable
from printer import Printer

class PrinterProxy(Printable):
    def __init__(self):
        pass

    def __init__(self, name):
        self.__name = name
        self.__real = None

    def set_printer_name(self, name):
        if self.__real is not None:
            self.__real.set_printer_name(name)
        
        self.__name = name

    def get_printer_name(self):
        return self.__name

    def printer(self, string):
        self.realize()
        self.__real.printer(string)

    def realize(self):
        if self.__real is None:
            self.__real = Printer(self.__name)
