# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:11:23 2018

@author: JolanSamwel
"""

import sys
sys.path.insert(0, sys.path[0]+'../')

import tkinter as tk
from tkinter import ttk

from Tools.SortButton import SortButton

class Werknemerlijst(ttk.Frame):  
    _rijen = []
    _SortKnoppen = []
    
    def __init__(self, parent, werknemers, columns):
        ttk.Frame.__init__(self, parent)
        
        self._Columns = columns
        self._Werknemers = werknemers
        
        for i in range(len(columns)):
            x = 0 + i * .15
            
            self._SortKnoppen.append(SortButton(self, self.Sort, self._Columns[i]))
            self._SortKnoppen[i].place(relx=x, rely=0)
        
        self._CreateRows()
        
    def Sort(self, Name, state):
        #Remove list
        for widget in self._rijen:
            widget[0].destroy()
            widget[1].destroy()
            
        self._rijen = []    

        #Determine which button is pressed and reset the other buttons        
        column = self._SortKnoppen.index(Name)
        
        for i in range(len(self._SortKnoppen)):
            if i is not column:
                self._SortKnoppen[i].State = 'Default'
        
        #Sort list according to which sortingbutton is pressed
        if state == 'Up':
            self._Werknemers.sort(key=lambda elem: elem[column], reverse=True)
        elif state == 'Down':
            self._Werknemers.sort(key=lambda elem: elem[column])
            
        #Recreate list after it is sorted
        self._CreateRows()    
            
    def _CreateRows(self):
        TempColumn = []
        
        for i in range(len(self._Werknemers)):
            y = .05 + i*.05

            for n in range(len(self._Columns)):
                x = n * .15
                
                TempColumn.append(ttk.Label(self, text=self._Werknemers[i][n]))
                
                TempColumn[n].config(justify="left")
                TempColumn[n].place(relx=x, rely=y)
 
            self._rijen.append(TempColumn)
            TempColumn = []
    
class Werknemers(ttk.Frame):
    Layout = "grid"
    Title = "Werknemers"
    
    def __init__(self, parent, controller, SQL):
        ttk.Frame.__init__(self, parent)
        
        self._Lijst = None
        
        columns = ['Naam', 'Leeftijd']
        Werknemers = [['Yoeri Samwel', '03-12-1986'], 
                      ['Jolan Samwel', '06-04-1992'], 
                      ['Fiona van de Haar', '23-04-1994'],
                      ['Remy Samwel', '25-08-1994']]
        
        self._CreateList(Werknemers, columns)
        
    def _CreateList(self, werknemers, columns):        
        self._Lijst = Werknemerlijst(self, werknemers, columns)
        self._Lijst.place(relx=.1, rely=.15, relwidth=.9, relheight=.85)