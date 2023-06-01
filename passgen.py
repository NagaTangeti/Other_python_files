#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 12:39:16 2023

@author: nagatangeti
"""

import random

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*#?"
strength = ["weak", "medium", "strong"]

passlen = 0
pwstrong = str(input("How strong do u need ur password (weak, medium, strong):"))

def pass_gen(passlen):
    if pwstrong == "weak":
       passlen = random.randint(1,2)
       return passlen
        
    elif pwstrong == "medium":
         passlen = random.randint(5,6)
         return passlen
    
    elif pwstrong == "strong":
         passlen = random.randint(8,9)
         return passlen
    

print("".join(random.sample(s,pass_gen(passlen))))
