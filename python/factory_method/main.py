#!/usr/bin/python
# -*- coding: utf-8 -*-
from IDCard.idcard_factory import IDCardFactory

if __name__ == '__main__':
    factory = IDCardFactory()
    card1 = factory.create('あいうえお')
    card2 = factory.create('かきくけこ')
    card3 = factory.create('花子')

    card1.use()
    card2.use()
    card3.use()
