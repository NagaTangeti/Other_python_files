#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:49:56 2023

@author: nagatangeti
"""

pal = input('give me a word:')
#n = len(pal) + 1

#for c in pal:
  #  if pal[c] == pal[-1-c]

rev = pal[::-1]
print(rev)

if pal == rev:
    print('Palindrome')
else:
    print('Not palindrome')
    
    