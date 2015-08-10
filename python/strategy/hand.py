#!/usr/bin/python
# -*- coding: utf-8 -*-

class Hand():
    HANDVALUE_GUU = 0
    HANDVALUE_CHO = 1
    HANDVALUE_PAA = 2
    name = [
        'グー', 'チョキ', 'パー'
    ]

    def __init__(self, handvalue):
        self.__handvalue = handvalue # じゃんけんの手の値
    
    @staticmethod
    def get_hand(handvalue):
        # FIXME: 記述場所 静的にしたい 
        hand = [
            Hand(Hand.HANDVALUE_GUU),
            Hand(Hand.HANDVALUE_CHO),
            Hand(Hand.HANDVALUE_PAA)
        ]
        print handvalue
        return hand[handvalue]

    def is_stronger_than(self, h):
        return self._fight(h) == 1

    def is_weaker_than(self, h):
        return self._fight(h) == -1

    def _fight(self, h):
        return 1

    def to_string(self):
        return self.__name[self.__handvalue]
