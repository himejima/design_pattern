#!/usr/bin/python
# -*- coding: utf-8 -*-
from char_display import CharDisplay
from string_display import StringDisplay

if __name__ == '__main__':
    d1 = CharDisplay('H')
    d2 = StringDisplay('Hello, world.')
    d3 = StringDisplay('こんにちは。')

    d1.display()
    d2.display()
    d3.display()
