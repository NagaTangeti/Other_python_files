#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:07:33 2023

@author: nagatangeti
"""

rows = int(input("Enter number of rows: "))

for i in range(1, rows+1):
    print("  "*(rows-i), end="")
    print("* "*(2*i-1))
