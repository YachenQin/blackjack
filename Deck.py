#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:20:54 2019

@author: qinyachen
"""
from random import shuffle


class deck(object):
    def __init__(self,decksnum = 4):
        self.new_cards(decksnum)
        self.shuffle()

    def new_cards(self,decksnum):
        self.cards = []
        for card in ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', 'A']:
            for card_num in range(4*decksnum):
                self.cards.append(card)
        self.num_cards_left = len(self.cards)
    
    def shuffle(self):
        shuffle(self.cards)
        
    
    
    def deal(self):
        self.num_cards_left -= 1
        if self.num_cards_left == 0:
            self.new_cards()
            self.shuffle()
        return self.cards.pop()
    
    def ifenough(self):
        if(len(self.cards) < 108):
            return False
        return True