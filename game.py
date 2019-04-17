#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:22:35 2019

@author: qinyachen
"""

from Deck import deck
from player import Player
import random
import time

class Game:
    def __init__(self,players):
        
        self.playerlist = []
        
        for player in enumerate(players):
            self.playerlist.append(Player(player[0],player[1]))
        
        self.dealer = Player(6,0)
        self.dealerpoints = 0
        
        self.playerpoints = []
        self.playerAnums = []
        self.actions = [0,1,2,3,4,5,6]
        
        self.table = deck()
        self.table.shuffle()
        
        
        self.bust = 0
        #self.max_num = 0
        #self.winner = []
        
        self.rewards = [50,50,50,50,50,50,50]
        self.moneybet = [0,0,0,0,0,0,0,0]
    
    def play(self):
        while(self.table.ifenough()):
            self.reset()
            self.run_one_time()
        
        print("game end")
        print("the final money is")
        print(self.rewards)    
    
    def reset(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("round start")
        self.playerpoints = []
        self.playerAnums = []
        self.bust = 0
        for player in self.playerlist:
            player.reset_()
            player.getcard(self.table)
            player.getcard(self.table)
            self.playerpoints.append(player.getpoints()[0]) 
            self.playerAnums.append(player.getpoints()[1])
        self.dealer.reset_()
        self.dealer.getcard(self.table)
        self.dealerpoints = self.dealer.getpoints()[0]
        print("now the points of all after all deals" )
        print(self.playerpoints)
        print("now the num of A in all players " )
        print(self.playerAnums)
        print("the dealer points after first is " + str(self.dealerpoints))
        self.dealer.getcard(self.table)
        self.dealerpoints = self.dealer.getpoints()[0]
        print("the money of all person")
        print(self.rewards)
        
        
    def run_one_time(self,):
        for action in self.actions:
            
            #dealers turn
            if(action == 6):
                while(self.dealerpoints < 17):
                    self.dealer.getcard(self.table)
                    self.dealerpoints = self.dealer.getpoints()[0]
                
                
                
                if(self.dealerpoints > 21):
                    self.bust += 1
                    print("dealer bust!")
                    for i in range(6):
                        self.rewards[i] += self.moneybet[i]
                        self.rewards[action] -= self.moneybet[i]
                else:
                    for points in enumerate(self.playerpoints):
                        if(points[1] > self.dealerpoints and points[1] <=21):
                            self.rewards[points[0]]+=self.moneybet[points[0]]
                            self.rewards[action] -= self.moneybet[points[0]]
                        elif(points[1] < self.dealerpoints and points[1] <=21):
                            self.rewards[action]+=self.moneybet[points[0]]
                            self.rewards[points[0]]-=self.moneybet[points[0]]
                        
            #human turn
            elif(self.playerlist[action].type == 1):
                self.humanrun(action)
            #AI turn
            else:
                self.AI_run(action)
            
        
        print("===================================================")
        print("the result is for this round is ")
        print(self.playerpoints)
        print("the result of dealer for this round is ")
        print(self.dealerpoints)
        print("the money is for this round is ")
        print(self.rewards)
        print("round end")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        time.sleep(10)
        
    def humanrun(self,action):
        print("===================YOUR TURN================================")
        print("now the points of all after all deals" )
        print(self.playerpoints)
        print("now the num of A in all players " )
        print(self.playerAnums)
        print("now is player "+str(action+1)+"'s turn")
        print("now the points of you is" )
        print(self.playerpoints[action])
        print("now the A num of you is" )
        print(self.playerAnums[action])
        print("====================================================")
        print("now the money of all is" )
        print(self.rewards)
        print("===================================================")
        bet = int(input("the money you want to bet:"))
        self.moneybet[action] = bet
        print("y is hit and n is not")
        
        while(input()=="y" and self.playerpoints[action] < 21):
            self.playerlist[action].getcard(self.table)
            self.playerpoints[action]=self.playerlist[action].getpoints()[0]
            print("now the points of you is" )
            print(self.playerpoints[action])
            if(self.playerpoints[action] >= 21):
                break
        
        if(self.playerpoints[action] > 21):
            print("player "+str(action+1)+ " bust!")
            self.bust += 1
            self.rewards[action] =  self.rewards[action] - bet
            self.rewards[6] += bet
        else:
            self.rewards[action] += 0
        print("=============YOUR TURN END======================================")
    
    
    def AI_run(self,action):
        bet = int(self.rewards[action]/3)
        if(bet==0):
            bet = 1;
        self.moneybet[action] = bet
        seq = [1,0]
        ifnext = self.rand_pick(seq,[(21 - self.playerpoints[action])/10,1-(21 - self.playerpoints[action])/10])
        while(ifnext == 1 and self.playerpoints[action] < 21):
            self.playerlist[action].getcard(self.table)
            self.playerpoints[action]=self.playerlist[action].getpoints()[0]
            ifnext = self.rand_pick(seq,[(21 - self.playerpoints[action])/10,1-(21 - self.playerpoints[action])/10]) 
        
        if(self.playerpoints[action] > 21):
            print("player "+str(action+1)+ " bust!")
            self.bust += 1
            self.rewards[action] = self.rewards[action] - bet
            self.rewards[6] += bet
        else:
            self.rewards[action]+=0
        
      
    def rand_pick(self,seq,probabilities):
        x = random.uniform(0 ,1)
        cumprob = 0.0
        for item , item_pro in zip(seq , probabilities):
            cumprob += item_pro
            if x < cumprob:
                break
        return item          




            
                
                
                
                
                
                