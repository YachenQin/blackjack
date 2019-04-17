#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:24:28 2019

@author: qinyachen
"""

#from Deck import deck
#from player import Player
from game import Game

if __name__ == '__main__':
    players = [0,0,0,0,0,0]
    print("for 1-6, which player you want to choose?")
    print("we have 7 players, the 7th is dealer")
    chosen = input("please input any number from 1-6:")
    players[int(chosen)-1]=1
    game = Game(players)
    game.play()
            