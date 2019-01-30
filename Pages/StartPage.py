# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 15:32:50 2018

@author: JolanSamwel
"""

import sys
sys.path.insert(0, sys.path[0]+'../')

import tkinter as tk
from tkinter import ttk

class StartPage(ttk.Frame):
    Layout = "place"
    Title = "Home"
    
    def __init__(self, parent, controller, SQL):
        ttk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text="Start Page")
        label.place(relx=.1, rely=.1)
        
        label2 = ttk.Label(self, text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")
        label2.config(wraplength=600)
        label2.place(relx=.1, rely=.2)