#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:47:55 2023

@author: nagatangeti
"""

import tkinter as tk
import random
import time

class SpeedTypingTest:
    def __init__(self, master):
        self.master = master
        self.master.title('Speed Typing Test')
        self.text = tk.Text(self.master, height=10, width=50)
        self.text.pack()
        self.start_button = tk.Button(self.master, text='Start', command=self.start_test)
        self.start_button.pack()
        self.time_label = tk.Label(self.master, text='Time: 0')
        self.time_label.pack()
        self.accuracy_label = tk.Label(self.master, text='Accuracy: 0%')
        self.accuracy_label.pack()
        self.wpm_label = tk.Label(self.master, text='WPM: 0')
        self.wpm_label.pack()
        self.words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
        self.current_word = ''
        self.start_time = 0
        self.total_time = 0
        self.total_chars = 0
        self.correct_chars = 0

    def start_test(self):
        self.start_button.config(state='disabled')
        self.text.config(state='normal')
        self.text.delete('1.0', 'end')
        self.current_word = random.choice(self.words)
        self.text.insert('1.0', self.current_word)
        self.text.tag_add('current_word', '1.0', '1.' + str(len(self.current_word)))
        self.text.tag_config('current_word', background='yellow')
        self.text.config(state='disabled')
        self.start_time = time.time()
        self.master.after(1000, self.update_time)

    def update_time(self):
        self.total_time += 1
        self.time_label.config(text='Time: ' + str(self.total_time))
        self.master.after(1000, self.update_time)

    def check_input(self, event):
        if event.char == ' ':
            input_word = self.text.get('1.0', 'end').strip()
            if input_word == self.current_word:
                self.correct_chars += len(self.current_word)
            self.total_chars += len(self.current_word) + 1
            accuracy = round(self.correct_chars / self.total_chars * 100, 2)
            self.accuracy_label.config(text='Accuracy: ' + str(accuracy) + '%')
            wpm = round(self.correct_chars / 5 / (time.time() - self.start_time) * 60, 2)
            self.wpm_label.config(text='WPM: ' + str(wpm))
            self.text.config(state='normal')
            self.text.delete('1.0', 'end')
            self.current_word = random.choice(self.words)
            self.text.insert('1.0', self.current_word)
            self.text.tag_add('current_word', '1.0', '1.' + str(len(self.current_word)))
            self.text.tag_config('current_word', background='yellow')
            self.text.config(state='disabled')

root = tk.Tk()
speed_typing_test = SpeedTypingTest(root)
root.bind('<Key>', speed_typing_test.check_input)
root.mainloop()
