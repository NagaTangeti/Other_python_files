#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:26:01 2023

@author: nagatangeti
"""


def mad_calculator():
    print("Welcome to the Mad Scientist's Calculator!")

    while True:
        operation = input("Choose your operation (add, subtract, multiply, divide) or type 'quit' to exit: ").lower()

        if operation == "quit":
            print("Farewell, my curious apprentice! Until we meet again!")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == "add":
            result = num1 + num2
            print(f"Eureka! The sum is: {result}")
        elif operation == "subtract":
            result = num1 - num2
            print(f"Aha! The difference is: {result}")
        elif operation == "multiply":
            result = num1 * num2
            print(f"By Jove! The product is: {result}")
        elif operation == "divide":
            if num2 == 0:
                print("Dividing by zero? Preposterous! Try again.")
            else:
                result = num1 / num2
                print(f"Voilà! The quotient is: {result}")
        else:
            print("Invalid operation! The Mad Scientist is displeased. Try again.")

mad_calculator()
