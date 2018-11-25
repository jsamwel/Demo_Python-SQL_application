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