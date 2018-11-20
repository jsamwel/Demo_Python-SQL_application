# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:11:10 2018

@author: JolanSamwel
"""

import tkinter as tk
from tkinter import ttk

class TimeEntry():
    def __init__(self, Frame, x, y):
        #Created a new frame
        FrameTime = ttk.Frame(Frame)
        FrameTime.place(relx=x, rely=y)
        
        self._Time = "00:00"
        
        #Variables for the hours and the minutes
        self._Hours = tk.StringVar() 
        self._Hours.set("00")  
        
        self._Minutes = tk.StringVar() 
        self._Minutes.set("00")
        
        #Entry's for the hours and the minutes
        EntryHours = ttk.Entry(FrameTime, textvariable=self._Hours)
        EntryHours.config(justify="right", width=5)
        EntryHours.grid(row=0, column=0)
        
        EntryMinutes = ttk.Entry(FrameTime, textvariable=self._Minutes)
        EntryMinutes.config(justify="right", width=5)
        EntryMinutes.grid(row=0, column=2)
        
         #Adds a : between the entry for hours and minutes
        Divider = ttk.Label(FrameTime, text=":")
        Divider.config(justify="center", width=1)
        Divider.grid(row=0, column=1)
        
        #When the input changes check the imput
        self._Hours.trace('w', lambda *args, **kw: self._EntryCheck(Entry=EntryHours, 
                                                            Value=self._Hours, Limit=24))  
                
        self._Minutes.trace('w', lambda *args, **kw: self._EntryCheck(Entry=EntryMinutes, 
                                                            Value=self._Minutes, Limit=59))

    def _EntryCheck(self, *args, **kw):
        Entry = kw.pop('Entry', None)
        Value = kw.pop('Value', None)
        Limit = kw.pop('Limit', 0)
        
        Input = Entry.get()       
        
        #Ensure that the entry always contains two numbers
        if len(Input) < 1: 
            Value.set("00")
            return
        
        if len(Input) < 2: 
            Value.set("0" + Input[0])
            return
                
        if len(Input) > 2: 
            Value.set(Input[:2]) 
        
        #Reset the value when the input is not a number
        if not str.isdigit(Input): 
            Value.set("00")
            return
        
        #Limit the input to a maximum value
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
