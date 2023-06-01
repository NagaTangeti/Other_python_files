#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:37:45 2023

@author: nagatangeti
"""

def pattern(n):
    num = 65
    for i in range(0,n):
        for j in range(0,i+1):
            ch = chr(num)
            print(ch,end=" ")
            num = num+1
        print("\r")
    
n = int(input("Enter a number of rows: "))
pattern(n)