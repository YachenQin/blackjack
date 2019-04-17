#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:37:34 2019

@author: qinyachen
"""

class Player(object):
    def __init__(self, number):
        self.number = number

    def bet(self, current_funds, minimum_bet, maximum_bet):
        return minimum_bet

    def play(self, current_hand, current_table):
        return 'stand'

    def final_look(self, final_table):
        pass
    
class dealerplayer(Player):
    def __init__(self, number=0):
        Player.__init__(self, number)

    def play(self, current_hand, current_table):
        possible_scores = current_hand.possible_scores()
        
        if possible_scores == 'blackjack':
            return 'stand'
        
        for score in possible_scores:
            if score >= 17 and score <= 21:
                return 'stand'
        return 'hit'
    
    
    