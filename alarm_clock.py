#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 13:59:37 2023

@author: nagatangeti
"""

import time
from playsound import playsound

#


def mad_alarm_clock():
    print("Welcome to the Mad Scientist's Alarm Clock!")
    alarm_time = input("Enter the time for the alarm in HH:MM format: ")

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up! Wake up!")
            #frequency = 2500  # Set frequency to 2500 Hz
            #duration = 2000  # Set duration to 2000 ms (2 seconds)
            playsound('/Desktop/Anaconda_spyder/alarm.mp3')

            break
        else:
            print(f"Current time is {current_time}. Waiting for {alarm_time}...")
            time.sleep(60)  # Wait for 60 seconds before checking the time again

mad_alarm_clock()
