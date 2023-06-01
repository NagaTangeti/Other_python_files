#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:27:59 2023

@author: nagatangeti
"""

from survey import AnonymousSurvey

#Define a question, and make a survey.
question = "What language did u first learn to speak?"
my_survey = AnonymousSurvey(question)

#Show the question, and store responses to the questions.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
    
#Show the survey results.
print("\nThank u to everyone who participated in the survey!")
my_survey.show_results()