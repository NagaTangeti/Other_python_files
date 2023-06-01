#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:46:23 2023

@author: nagatangeti
"""
import random

user = input('ur choice is:')
choice = ['rock', 'paper', 'scissors']
comp = random.choice(choice)
print("computer's choice is:" + comp)

def compare(user, comp):
    if user == comp:
        print("Oh, it's a tie!")
    elif user == 'rock':
        if comp == 'scissors':
         print("Congratulations, u win!")
        else: print("Sorry, computer wins")
    
    elif user == 'paper':
        if comp == 'rock':
            print("Congratulations, u win!")
        else: print("Sorry, computer wins")
        
    elif user == 'scissors':
        if comp == 'paper':
            print("Congratulations, u win!")
        else: print("Sorry, computer wins")
    
    else: 
        return("Invalid input!!! Plzz Choose from rock, paper and scissors")
        

compare(user,comp)       