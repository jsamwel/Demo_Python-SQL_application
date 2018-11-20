# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:11:10 2018

@author: JolanSamwel
"""

import tkinter as tk
from tkinter import ttk

class TimeEntry():
    def __init__(self, Frame, x, y):
        self._Frame = ttk.Frame(Frame)
        self._Frame.place(relx=x, rely=y)
        
        self._Time = "00:00"
        
        self._Hours = tk.StringVar() 
        self._Hours.set("00")  
        
        self._Minutes = tk.StringVar() 
        self._Minutes.set("00")
        
        self._EntryHours = ttk.Entry(self._Frame, textvariable=self._Hours)
        self._EntryHours.config(justify="right", width=5)
        self._EntryHours.grid(row=0, column=0)
        
        self._Hours.trace('w', lambda *args, **kw: self._LimitEntry(Entry=self._EntryHours, 
                                                            Value=self._Hours, Limit=24))
        
        self._EntryMinutes = ttk.Entry(self._Frame, textvariable=self._Minutes)
        self._EntryMinutes.config(justify="right", width=5)
        self._EntryMinutes.grid(row=0, column=2)
        
        self._Minutes.trace('w', lambda *args, **kw: self._LimitEntry(Entry=self._EntryMinutes, 
                                                            Value=self._Minutes, Limit=59))
        
        self._Divider = ttk.Label(self._Frame, text=":")
        self._Divider.config(justify="center", width=1)
        self._Divider.grid(row=0, column=1)
        
    def _LimitEntry(self, *args, **kw):
        Entry = kw.pop('Entry', None)
        Value = kw.pop('Value', None)
        Limit = kw.pop('Limit', 0)
        
        Input = Entry.get()       
        
        if len(Input) < 1: 
            Value.set("00")
            return
        
        if len(Input) < 2: 
            Value.set("0" + Input[0])
            return
            
        if len(Input) > 2: 
            Value.set(Input[:2]) 
        
        if not str.isdigit(Input): 
            Value.set("00")
            return
        
        if int(Input[:2]) > Limit: 
            Value.set(str(Limit))
            return
     
    @property    
    def Time(self):        
        return self._Time
    
    @Time.getter
    def Time(self):
        self._Time = self._Hours.get() + ":" + self._Minutes.get()
        
    @Time.setter
    def Time(self, value):
        self._Time = value
        
        self._Hours = value[:2]
        self._Minutes= value[3:5]