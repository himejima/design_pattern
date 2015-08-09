#!/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser

class Database(object):
    def __init__(self):
        pass

    @staticmethod
    def get_properties(dbname):
        filename = dbname + '.ini'
        initfile = ConfigParser.SafeConfigParser()

        try:
            initfile.readfp(open(filename))
            # print 1
            initfile.read(filename)
            # print 2
            # print len(initfile.sections())
            # for debug
            # for s in initfile.sections():
            #     print s
            #     for option in initfile.options(s):
            #         print initfile.get(s, option)
        except:
            print 'Warning: ' + filename + ' is not found.'
        
        return initfile 
