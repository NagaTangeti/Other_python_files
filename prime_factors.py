#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:27:35 2023

@author: nagatangeti
"""

num = int(input("gimme a number:"))
prime = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
a = [x for x in range(2,num) if num % x == 0]

def primality(num):
    if num > 1:
        if len(a) == 0:
            print("Yay, prime number")
        else:
            print("Oh no, not prime")
            print(a)
    else:
        print("Oh no, not prime")
        
primality(num)
