#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:35:20 2019

@author: qinyachen
"""

from Deck import deck

class Player(object):
    
    def __init__(self, playerNum,playertype):
        self.name = playerNum
        self.points = 0
        self.hand = []
        self.type = playertype
        self.finalA = 0
    
    def getcard(self, Deck):
        self.hand.append(Deck.deal())
    
    
        
    def getpoints(self):
        points = 0
        Anum = 0
        finalA = 0
        for card in self.hand:
            if(card!='A'):
                points = points + int(card) 
            else:
               Anum += 1
               finalA += 1
               points = points + 11
        
        while Anum > 0 and points > 21:
            Anum = Anum - 1
            points = points - 10
            
        
        return (points,finalA)
    
    def reset_(self):
        self.hand = []
                
            