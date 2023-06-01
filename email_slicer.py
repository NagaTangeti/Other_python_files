#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:45:19 2023

@author: nagatangeti
"""

email = input('Enter your email address: ')

# Find the position of the @ symbol in the email address
at_index = email.find('@')

# Extract the username and domain name from the email address
username = email[:at_index]
domain = email[at_index+1:]

# Print the username and domain name
print('Username:', username)
print('Domain:', domain)
