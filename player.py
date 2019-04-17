#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:35:20 2019

@author: qinyachen
"""

from Deck import deck

class Player(object):
     #A player has a hand,a palyer number, a type and a finalA. Interacts with the deck
    
    def __init__(self, playerNum,playertype):
        self.name = playerNum
        self.points = 0
        self.hand = []
        self.type = playertype #0-AI,1-human
        self.finalA = 0 #the number of A in players' hand
    
    def getcard(self, Deck):
        self.hand.append(Deck.deal())
    
    
        
    def getpoints(self):
        '''
        calculate the points of cards in palyers' hand.
        If player has A in hand, consider it as 11 first, 
        if final is larger than 21,
        consider it as 1.
        
        return (the points player has, the number of A in player's hand)
        '''
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
        '''
        claer all cards and points in player's hand
        '''
        self.hand = []
                
            