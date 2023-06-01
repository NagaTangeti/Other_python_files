#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:39:45 2023

@author: nagatangeti
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [element for element in a if element % 2 == 0]

print(b)