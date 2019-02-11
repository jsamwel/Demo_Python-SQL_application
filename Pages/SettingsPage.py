# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 08:47:27 2019

@author: JolanSamwel
"""

import sys
sys.path.insert(0, sys.path[0]+'../')

from tkinter import ttk

class SettingsPage(ttk.Frame):
    Layout = "place"
    Title = "Settings"
    
    def __init__(self, parent, controller, SQL):
        ttk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text="SQL connection")
        label.place(relx=.1, rely=.1)
        
        SQLStatusTextLabel = ttk.Label(self, text="Status:")
        SQLStatusTextLabel.place(relx=.11, rely=.15)
        
        SQLStatusLabel = ttk.Label(self, text="Not connected")
        SQLStatusLabel.place(relx=.15, rely=.15)
        
        controller.SQL.Connected.trace(mode="w", callback=self._SQLConnectionChange)
        
    def _SQLConnectionChange(self):
        if self.parent.SQL.connected.get():       
            self.SQLStatusLabel.config(text="Connected")
        else:
            self.SQLStatusLabel.config(text="Not connected")