# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:48:26 2018

@author: JolanSamwel
"""

import tkinter.ttk as ttk

class SortButton(ttk.Frame):
    _State = 'Default'
    
    def __init__(self, parent, Callback, text):
        ttk.Frame.__init__(self, parent) 
        
        self._Callback = Callback
        self._SetStyle()
        self._SetWidget(text)

    def _SetStyle(self):
        style = ttk.Style()
        
        arrow_layout = lambda dir: ([('Button.focus', {'children': [('Button.%sarrow' % dir, {'side': 'right'}), 
                                                                    ('Button.label', {'side': 'left'})]})])
        
        style.layout('SortUp.TButton', arrow_layout('up'))
        style.layout('SortDown.TButton', arrow_layout('down'))
        style.layout('Sort.TButton', ([('Button.focus', {'children': [('Button.label', None)]})]))
        
    def _SetWidget(self, Text):
        self._lbutton = ttk.Button(self, style='Sort.TButton',
                                   text=Text, command=self._SortList)
        self._lbutton.pack()
        
    def _SortList(self):
        if self.State == 'Default':
            self.State = 'Up'          
        elif self.State == 'Up':
            self.State = 'Down'           
        elif self.State == 'Down':
            self.State = 'Up'
            
        if self._Callback is not None: self._Callback(self, self.State)     
            
    @property        
    def State(self):
        return self._State
    
    @State.setter
    def State(self, value):
        if value == 'Default':
            self._State = 'Default'
            self._lbutton.config(style='Sort.TButton')            
        elif value == 'Up':
            self._State = 'Up'
            self._lbutton.config(style='SortUp.TButton')            
        elif value == 'Down':
            self._State = 'Down'
            self._lbutton.config(style='SortDown.TButton')            
        else:
            self._State = 'Default'
            self._lbutton.config(style='Sort.TButton')