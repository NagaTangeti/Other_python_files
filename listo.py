#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:21:28 2023

@author: nagatangeti
"""

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
import random

a = rand()
b = random()

k = []

for elem in a:
    if elem in b:
        k.append(elem)
        
print(set(k))