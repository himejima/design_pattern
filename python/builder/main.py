#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from text_builder import TextBuilder
from html_builder import HTMLBuilder
from director import Director

def usage():
    print 'Usage: python Main plain     プレーンテキストで文書作成'
    print 'Usage: python Main html      HTMLファイルで文書作成'

if __name__ == '__main__':
    # print sys.argv
    # 引数の数 check
    if len(sys.argv) != 2:
        usage()
        exit()

    if sys.argv[1] == 'plain':
        textbuilder = TextBuilder()
        director = Director(textbuilder)
        director.construct()
        result = textbuilder.get_result()
        print result
    elif sys.argv[1] == 'html':
        htmlbuilder = HTMLBuilder()
        director = Director(htmlbuilder)
        director.construct()

        filename = htmlbuilder.get_result()
        print filename + 'が作成されました。'
    else:
        usage()
        exit()



