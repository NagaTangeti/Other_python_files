#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 13:10:48 2023

@author: nagatangeti
"""



x = []
def fib(x):
    num = int(input("How many digits to generate:"))
    i = 1
    if num == 0:
        x = []
    elif num == 1:
        x = [1]
    elif num == 2:
        x = [1,1]
    elif num > 2:
        x = [1,1]
        while i < num - 1:
            x.append(x[i] + x[i-1])
            i += 1
            
    print(x)
    
fib(x)