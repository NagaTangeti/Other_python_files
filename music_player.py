#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:51:59 2023

@author: nagatangeti
"""

import pygame
import os

def mad_music_player():
    print("Welcome to the Mad Scientist's Music Player!")

    pygame.mixer.init()

    while True:
        action = input("Choose your action (play, stop, pause, unpause, quit): ").lower()

        if action == "play":
            song = input("Enter the path to your audio file: ")
            if not os.path.isfile(song):
                print("Invalid file path! The Mad Scientist is displeased. Try again.")
                continue

            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            print("The symphony begins! Mwahahaha!")
        elif action == "stop":
            pygame.mixer.music.stop()
            print("The music has been silenced!")
        elif action == "pause":
            pygame.mixer.music.pause()
            print("The melody is paused, awaiting your command.")
        elif action == "unpause":
            pygame.mixer.music.unpause()
            print("The music resumes its enchanting dance!")
        elif action == "quit":
            pygame.mixer.music.stop()
            print("Farewell, my musical apprentice! Until we meet again!")
            break
        else:
            print("Invalid action! The Mad Scientist is displeased. Try again.")

mad_music_player()

