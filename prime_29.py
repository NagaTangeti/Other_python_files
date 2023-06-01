#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:46:41 2023

@author: nagatangeti
"""


num = int(input("Enter the number u want to check if prime: "))
#num = 29

if all(num % i != 0 for i in range(2,num)):
    print(num,"is prime number.")

else: 
    print(num,"isn't prime number.")
    

#flag = False

#if num == 1:
#    print(num, "isn't prime number.")
#elif num > 1:
#    for i in range(2,num):
#        if (num % i) == 0:
#            flag = True
#            break
#    if flag:
#        print(num,"isn't prime number.")
#    else:
#        print(num,"is prime number.")