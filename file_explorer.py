#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 12:59:15 2023

@author: nagatangeti
"""

import tkinter as tk
from tkinter import filedialog

class FileExplorer:
    def __init__(self, master):
        self.master = master
        self.master.title('File Explorer')
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.button = tk.Button(self.frame, text='Browse', command=self.browse_files)
        self.button.pack(side='left')
        self.filename_label = tk.Label(self.frame, text='No file selected')
        self.filename_label.pack(side='left')

    def browse_files(self):
        filetypes = [('All Files', '*.*')]
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            self.filename_label.config(text=filename)

root = tk.Tk()
file_explorer = FileExplorer(root)
root.mainloop()
