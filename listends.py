#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:03:33 2023

@author: nagatangeti
"""

x = []
n = int(input("length of list is:"))

for i in range(0,n):
    print("number at index is:",i)
    elem = int(input())
    x.append(elem)
print(x)


def list_ends(x):
    e = [x[0],x[len(x)-1]]
    print(e)

list_ends(x)


