#!/usr/bin/python
# -*- coding: utf-8 -*-

class Singleton(object):
    _instance = None
    
    def __new__(cls, *a, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

if __name__ == '__main__':
    s1 = Singleton("test1")
    s2 = Singleton("test2")

    if s1 is s2:
        print 's1 is s2'
    else:
        print 's1 is not s2'
