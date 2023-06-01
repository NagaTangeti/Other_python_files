#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:56:44 2023

@author: nagatangeti
"""

num = int(input('give me a number:'))
x = list(range(1, num + 1))

print(x)

d = []

for elem in x:
   if num % elem == 0:
       d.append(num)
        
print(d)

#num = int(input("Please choose a number to divide: "))

#listRange = list(range(1,num+1))

#divisorList = []

#for number in listRange:
 #   if num % number == 0:
  #      divisorList.append(number)

#print(divisorList)
