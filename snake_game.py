#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:07:36 2023

@author: nagatangeti
"""

import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title('Snack Game')
screen.bgcolor('black')
screen.setup(width=600, height=600)

# Create the snack
snack = turtle.Turtle()
snack.shape('square')
snack.color('white')
snack.penup()
snack.speed(0)
snack.goto(0, 0)

# Create the food
food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.penup()
food.speed(0)
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# Define the snack movement functions
def move_up():
    snack.setheading(90)

def move_down():
    snack.setheading(90)

def move_left():
    snack.setheading(90)

def move_right():
    snack.setheading(0)

# Set up the keyboard bindings
screen.listen()
screen.onkeypress(move_up, 'Up')
screen.onkeypress(move_down, 'Down')
screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')

# Define the main game loop
while True:
    snack.forward(20)

    # Check for collision with the food
    if snack.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

    # Check for collision with the walls
    if snack.xcor() > 290 or snack.xcor() < -290 or snack.ycor() > 290 or snack.ycor() < -290:
        time.sleep(1)
        snack.goto(0, 0)
        snack.direction = 'stop'

    # Update the screen
    screen.update()

# Start the game
screen.mainloop()
