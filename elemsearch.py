#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 15:27:40 2023

@author: nagatangeti
"""
import random

x = []
n = int(input("length of list is:"))
for i in range(n):
    x.append(random.randint(0,99))
print(x)

#for i in range(0,n):
    #print("number at index is:",i)
    #elem = int(input())
    #x.append(elem)

#print(x)

sx = sorted(x)
print(sx)

#def find(ord_list,elem_to_find):
    #for elem in ord_list:
        #return True
    #return False

def find(ord_list,elem_to_find):
    s_i = 1
    e_i = len(ord_list) - 1
    
    while True:
        m_i = (e_i - s_i)/2
        
        if m_i < s_i or m_i > e_i or m_i < 0:
            return False
        
        m_e = ord_list[m_i]
        if m_e == elem_to_find:
            return True
        elif m_e < elem_to_find:
            e_i = m_i
        else:
            s_i = m_i
            
        

if __name__ == "__main__":
    print(find(sx,8))
    

