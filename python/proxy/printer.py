#!/usr/bin/python
# -*- coding: utf-8 -*-

from printable import Printable
import time

class Printer(Printable):
    def __init__(self):
        self.heavy_job('Printerのインスタンスを生成中')

    def __init__(self, name):
        self.__name = name
        self.heavy_job('Printerのインスタンス(' + name + ')を生成中')

    def set_printer_name(self, name):
        self.__name = name

    def get_printer_name(self):
        return self.__name

    def printer(self, string):
        print '=== ' + self.__name + ' ==='
        print string

    def heavy_job(self, msg):
        print msg
        # 重い処理
        for i in range(5):
            try:
                time.sleep(1)
            except:
                pass
            print '.'

        print '完了'
