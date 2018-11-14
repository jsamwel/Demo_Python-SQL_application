# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 15:32:50 2018

@author: JolanSamwel
"""

import tkinter as tk
from tkinter import ttk

class StartPage(tk.Frame):
    Layout = "place"
    Title = "Home"
    
    def __init__(self, parent, controller, SQL):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Start Page")
        label.place(relx=.1, rely=.1)