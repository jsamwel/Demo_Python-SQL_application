# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:11:23 2018

@author: JolanSamwel
"""

import sys
sys.path.insert(0, sys.path[0]+'../')

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
            for i in range(len(self._Columns)):
                widget[i].destroy()
            
        self._rijen = []    

        #Determine which button is pressed and reset the other buttons        
        column = self._SortKnoppen.index(Name)
        
        for i in range(len(self._SortKnoppen)):
            if i is not column:
                self._SortKnoppen[i].State = 'Default'
        
        #Sort list according to which sortingbutton is pressed
        if state == 'Up':
            self._Werknemers.sort(key=lambda elem: elem[column])
        elif state == 'Down':
            self._Werknemers.sort(key=lambda elem: elem[column], reverse=True)
            
        #Recreate list after it is sorted
        self._CreateRows()    
            
    def _CreateRows(self):
        TempColumn = []
        
        for i in range(len(self._Werknemers)):
            y = .05 + i*.05

            for n in range(len(self._Columns)):
                x = n * .15
                
                TempColumn.append(ttk.Label(self, text=self._Werknemers[i][n+1]))
                
                TempColumn[n].config(justify="left")
                TempColumn[n].place(relx=x, rely=y)
 
            self._rijen.append(TempColumn)
            TempColumn = []
    
class Werknemers(ttk.Frame):
    Layout = "grid"
    Title = "Werknemers"
    
    def __init__(self, parent, controller, SQL):
        ttk.Frame.__init__(self, parent)
        
        self.SQL = SQL
        
        self._Lijst = None
        self._Werknemers = None
        
        # Update page when SQL connection changes
        controller.SQL.TKConnected.trace(mode="w", callback=self._SQLConnectionChange)
        
        self._CreateList()
        
    def _CreateList(self): 
        # Retrieve the active employees and add the entries for the employees to the page
        WerknemerQuery = """select * from employees where enddate is null"""
        
        columns = ['Naam', 'Geboren']
        
        if self.SQL.Connected:
            self._Werknemers = self.SQL.FetchQuery(WerknemerQuery)
        
            self._Lijst = Werknemerlijst(self, self._Werknemers, columns)
            self._Lijst.place(relx=.1, rely=.15, relwidth=.9, relheight=.85)
        
    def _SQLConnectionChange(self, *args, **kw):               
        self._CreateList()