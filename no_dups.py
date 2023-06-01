#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:25:17 2023

@author: nagatangeti
"""

def no_dups1(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y
        
def no_dups2(x):
    return list(set(x))

x= []
n = int(input("length of list is:"))

for i in range(0,n):
    print("number at index is:",i)
    elem = int(input())
    x.append(elem)
print(x)

print(no_dups1(x))

print(no_dups2(x))