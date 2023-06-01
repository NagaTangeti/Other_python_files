#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:15:39 2023

@author: nagatangeti
"""

from name_function import get_formatted_name

print("Enter 'q' at anytime to quit.")
while True:
    first = input("\nPlz gimme a first name: ")
    if first == 'q':
        break
    last = input("Plz gimme a last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
    
    
    