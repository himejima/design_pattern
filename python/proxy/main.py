#!/usr/bin/python
# -*- coding: utf-8 -*-
from printer_proxy import PrinterProxy

if __name__ == '__main__':
    p = PrinterProxy('Alice')
    print "名前は現在" + p.get_printer_name() + "です。"
    p.set_printer_name('bob')
    print "名前は現在" + p.get_printer_name() + "です。"
    p.printer('Hello, world.')
