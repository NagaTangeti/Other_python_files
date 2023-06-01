#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 14:56:00 2023

@author: nagatangeti
"""
import random

def comp_num(numb,uguess):
    cowbull = [0,0]
    for i in range(len(numb)):
        if numb[i] == uguess[i]:
            cowbull[0] += 1
        else:
            cowbull[1] += 1
    return cowbull

if __name__ == "__main__":
    playing = True
    numb = str(random.randint(0,9999))
    guess = 0
    
while playing:
    uguess = input("Gimme ur best guess:")
    if uguess == "exit":
        break
    cbcount = comp_num(numb,uguess)
    guess += 1
    print("U've " + str(cbcount[0]) + " cows, and " + str(cbcount[1]) + " bulls.")
    
    if cbcount[0] == 4:
        playing = False
        print("U'll win game after" + str(guess) + "! The number was" + str(numb))
        break
    else:
        print("Ur guess isn't quite right, try again.")
