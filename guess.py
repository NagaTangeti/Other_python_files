#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:56:12 2023

@author: nagatangeti
"""
import random

num = random.randint(1,9)
#print(num)

c = 0
guess = 0

#def Guessgame(num,guess):
    #if num == guess:
        #print("Wow, ur exactly right!!")
        
while guess != "exit" and guess != num:
    guess = input("Ur guess btw 1 and 9 is:")

    if guess == "exit":
        break 
    
    guess = int(guess)
    c +=1
    
    if num > guess:
        print("Ohh, too low!!")
    elif num < guess:
        print("Ohh, too high!!")
    else:
        print("Wow, ur exactly right!!")
        print("u only took" + str(c) + "tries.")
input()



