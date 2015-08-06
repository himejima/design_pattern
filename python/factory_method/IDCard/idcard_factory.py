#!/usr/bin/python
# -*- coding: utf-8 -*-
from Framework.factory import Factory
from IDCard.id_card import IDCard

class IDCardFactory(Factory):
    def __init__(self):
        self.__owners = []

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        self.__owners.append(product.get_owner())

    def get_owners(self):
        return self.__owners
