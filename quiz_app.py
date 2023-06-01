#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:34:45 2023

@author: nagatangeti
"""

def mad_quiz_application():
    print("Welcome to the Mad Scientist's Quiz!")

    questions = [
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "CO2", "NaCl", "O2"],
            "answer": "H2O"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Venus", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "What is the speed of light in a vacuum?",
            "options": ["299,792 km/s", "1,080 km/h", "1,126 km/h", "3,000 km/s"],
            "answer": "299,792 km/s"
        }
    ]

    score = 0

    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

        answer = int(input("Enter the number of your answer: "))
        if question["options"][answer - 1] == question["answer"]:
            print("Correct! The Mad Scientist is impressed!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}")

    print(f"Your final score is: {score}/{len(questions)}")

mad_quiz_application()
