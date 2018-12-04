# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:11:23 2018

@author: JolanSamwel
"""

import sys
sys.path.insert(0, sys.path[0]+'../')

import tkinter as tk
from tkinter import ttk

class Werknemers(ttk.Frame):
    Layout = "grid"
    Title = "Werknemers"
    
    def __init__(self, parent, controller, SQL):
        ttk.Frame.__init__(self, parent)