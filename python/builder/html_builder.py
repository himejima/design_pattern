#!/usr/bin/python
# -*- coding: utf-8 -*-
from builder import Builder

class HTMLBuilder(Builder):
    def __init__(self):
        self.__filename = None

    def make_title(self, title):
        self.__filename = title + '.html'
        # TODO: ファイル作成
        try:
            pass
        except:
            pass
        print '<html><head><title>' + title + '</title></head><body>'
        # タイトルを出力
        print '<h1>' + title + '</h1>'

    def make_string(self, str):
        print '<p>' + str + '</p>'

    def make_items(self, items):
        print '<ul>'

        for i in range(len(items)):
            print '<li>' + items[i] + '</li>'

        print '</ul>'

    def closing(self):
        print '</body></html>'
        # TODO: ファイルクローズ


    def get_result(self):
        return self.__filename
