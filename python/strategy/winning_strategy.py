#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from strategy import Strategy
from hand import Hand

class WinningStrategy(Strategy):
    def __init__(self, seed):
        self.__won = False
        self.__prev_hand = None
        self.__random = random.seed(seed) 

    def next_hand(self):
        if not self.__won:
            # self.__prev_hand = Hand.get_hand(random.randint(1,3))
            self.__prev_hand = Hand.get_hand(random.randint(0,2))

        return self.__prev_hand

    def study(self, win):
        self.__won = win
