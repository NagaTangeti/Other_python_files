#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:52:41 2023

@author: nagatangeti
"""

x = input("enter sentence:")

def rev_str1(x):
    y = x.split()
    r = []
    for w in y:
        r.insert(0,w)
    return" ".join(r)

print(rev_str1(x))
    
def rev_str2(x):
    y = x.split()
    return ' '.join(y[::-1])

print(rev_str2(x))

def rev_str3(x):
    y = x.split()
    return" ".join(reversed(y))
    
print(rev_str3(x))

def rev_str4(x):
    y = x.split()
    y.reverse()
    return" ".join(y)
    
print(rev_str4(x))

