#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:16:50 2023

@author: nagatangeti
"""

import secrets
import string

def mad_password_generator():
    print("Welcome to the Mad Scientist's Password Generator!")

    length = int(input("Enter the desired length of your password (minimum 8 characters): "))
    if length < 8:
        print("A password shorter than 8 characters? Preposterous! I shall set it to 8.")
        length = 8

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))

    print(f"Behold, your cryptic key: {password}")

mad_password_generator()
