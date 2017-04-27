# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:48:26 2017

@author: cal31
"""

import random

#create beginning card, which will be 17 
beginCard = 17

#create an array for the deck of cards
deckOfCards = []
secondCard = 0

#method to draw a card
def pullRandomCard():
    i = random.uniform(0,51)
    return int(i)

#use loop to populate array with card values
for i in range(0, 52):
    if i < 9:
        deckOfCards.append(i + 2)
       
    elif 9 <= i and i < 18:
        deckOfCards.append(i - 7)
        
    elif 18 <= i and i < 27:
        deckOfCards.append(i - 16)
        
    elif 27 <= i and i < 36:
        deckOfCards.append(i - 25) 
        
    elif 36 <= i and i < 48:
        deckOfCards.append (10) 
        
    elif 48 <= i and i < 52:
        deckOfCards.append(1)
       
       

#run for 100k iterations
loss = 0.0
win = 0.0
probablyWin = 0.0

for iterator in range(0,100000):
    #shuffle the deck
    random.shuffle(deckOfCards)
    
    #pull random card value for iteration 
    secondCard = deckOfCards[pullRandomCard()]
   
    cardTotal = beginCard + secondCard
    
    if cardTotal < 21:
        probablyWin += 1
    elif cardTotal is 21:
        win += 1
    elif cardTotal > 21:
        loss += 1
     
      

#print out the results
print "Likely Victories: " + str("%.1f" % (probablyWin/1000)) + "%" 
print "Certain Victories: " + str("%.1f" % (win/1000)) + "%"
print "Defeats: " + str("%.1f" % (loss/1000)) + "%"




    

        

    
