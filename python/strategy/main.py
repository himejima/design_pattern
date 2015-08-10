#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from winning_strategy import WinningStrategy
# from prob_strategy import ProbStrategy
from player import Player

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage: python main.py randomseed1 randomseed2'
        print 'Example: python main.py 314 15'
        exit()

    seed1 = sys.argv[1]
    seed2 = sys.argv[2]

    player1 = Player('Taro', WinningStrategy(seed1))
    # player2 = Player('Hana', ProbStrategy(seed2))
    player2 = Player('Hana', WinningStrategy(seed2))

    for i in range(1000):
        next_hand1 = player1.next_hand()
        next_hand2 = player2.next_hand()

        if next_hand1.is_stronger_than(next_hand2):
            print 'Winner:' + player1.to_string()
            player1.win()
            player1.lose()
    #####     elif next_hand2.is_stronger_than(next_hand1):
    #####         print 'Winner:' + player2
    #####         player1.lose()
    #####         player2.win()
    #####     else:
    #####         print 'Even...'
    #####         player1.even()
    #####         player2.even()

    print 'Total result:'
    ##### print player1.to_string()
    ##### print player2.to_string()
