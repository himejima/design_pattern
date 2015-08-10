#!/usr/bin/python
# -*- coding: utf-8 -*-

class Player():
    # 名前と戦略を授けられる
    def __init__(self, name, strategy):
        self.__name = name
        self.__strategy = strategy

        self.__wincount = 0
        self.__losecount = 0
        self.__gamecount = 0

    # 戦略におうかがいを立てる
    def next_hand(self):
        return self.__strategy.next_hand()

    def win(self):
        self.__strategy.study(True)
        self.__wincount += 1
        self.__gamecount += 1

    def lose(self):
        self.__strategy.study(False)
        self.__losecount += 1
        self.__gamecount += 1

    def even(self):
        self.__gamecount += 1

    def to_string(self):
        return '[' + self.__name + ':' + str(self.__gamecount) + ' games, ' + str(self.__wincount) + ' win, ' + str(self.__losecount) + ' lose' + ']' 
