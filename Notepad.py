#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 13:50:54 2023

@author: nagatangeti
"""

import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title('Notepad')
        self.textarea = tk.Text(self.master, undo=True)
        self.textarea.pack(fill='both', expand=True)
        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='New', command=self.new_file)
        self.filemenu.add_command(label='Open', command=self.open_file)
        self.filemenu.add_command(label='Save', command=self.save_file)
        self.filemenu.add_command(label='Save As', command=self.save_file_as)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=self.master.quit)
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label='Undo', command=self.textarea.edit_undo)
        self.editmenu.add_command(label='Redo', command=self.textarea.edit_redo)
        self.editmenu.add_separator()
        self.editmenu.add_command(label='Cut', command=self.cut)
        self.editmenu.add_command(label='Copy', command=self.copy)
        self.editmenu.add_command(label='Paste', command=self.paste)
        self.menubar.add_cascade(label='Edit', menu=self.editmenu)
        self.master.config(menu=self.menubar)
        self.filename = None

    def new_file(self):
        self.textarea.delete('1.0', 'end')
        self.filename = None

    def open_file(self):
        filetypes = [('Text Files', '*.txt'), ('All Files', '*.*')]
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            with open(filename, 'r') as f:
                self.textarea.delete('1.0', 'end')
                self.textarea.insert('1.0', f.read())
            self.filename = filename

    def save_file(self):
        if self.filename:
            with open(self.filename, 'w') as f:
                f.write(self.textarea.get('1.0', 'end'))
        else:
            self.save_file_as()

    def save_file_as(self):
        filetypes = [('Text Files', '*.txt'), ('All Files', '*.*')]
        filename = filedialog.asksaveasfilename(filetypes=filetypes)
        if filename:
            with open(filename, 'w') as f:
                f.write(self.textarea.get('1.0', 'end'))
            self.filename = filename

    def cut(self):
        self.textarea.event_generate('<<Cut>>')

    def copy(self):
        self.textarea.event_generate('<<Copy>>')

    def paste(self):
        self.textarea.event_generate('<<Paste>>')

root = tk.Tk()
notepad = Notepad(root)
root.mainloop()
