# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:55:31 2018

@author: JolanSamwel
"""

import tkinter as tk
from tkinter import ttk
from ttkthemes import themed_tk

from Pages.UrenRegistratie import UrenRegistratie
from Pages.GraphPage import GraphPage
from Pages.StartPage import StartPage
from Pages.Werknemers import Werknemers

from Tools.SQLConnection import Connection

class Main(themed_tk.ThemedTk):
    def __init__(self): 
        super().__init__() 
        #self.Frame.root.geometry("800x400+100+100")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", self._Quit)
        
        #Select style for ttk
        #print(self.get_themes())
        self.set_theme('clam')
       
        #Frames for the pages and the navigation
        self.container = ttk.Frame(self)        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.place(relx=0.15, rely=0, relwidth=.85, relheight=1)
        
        self.NavigationFrame = ttk.Frame(self)        
        self.NavigationFrame.place(relx=0, rely=0 , relwidth=.15, relheight=1)
        
        self._CreateSQLConnection()
        self._CreatePages()
        
        self.ShowFrame(StartPage)
        
    def _CreateSQLConnection(self):
         #Create SQl connection
        hostname    = 'localhost'
        user        = 'postgres'
        password    = 'WWPostgres'
        database    = 'DataDevelopment'
        
        self.SQL = Connection(hostname, user, password, database)
        self.SQL.Connect()         
        
    def _CreatePages(self):
        #Create pages and navigation buttons  
        self.Pages = (StartPage, GraphPage, UrenRegistratie, Werknemers)
        self.NavigationButtons = {}        
        self.frames = {}
        
        self.QuitButton = ttk.Button(self.NavigationFrame, text="Exit")
        self.QuitButton.config(command=self._Quit)
        self.QuitButton.place(relx=0, rely=.95, relwidth=1)
        
        self.ConnectionLabel = ttk.Label(self.NavigationFrame, text="")
        self.ConnectionLabel.config(anchor="center")
        self.ConnectionLabel.place(relx=0, rely=.01, relwidth=1)
        
        if self.SQL.Connected:       
            self.ConnectionLabel.config(text="Connected", foreground="black")
        else:
            self.ConnectionLabel.config(text="Not connected", foreground="red")
            
        for I in range(len(self.Pages)):
            #Navigation command for the button
            action = lambda x = self.Pages[I]: self.ShowFrame(x)   
            
            #Location for the button
            y = .05 + I * .04            
            
            #Create the page
            frame = self.Pages[I](self.container, self, self.SQL)
            
            self.frames[self.Pages[I]] = frame
                        
            if frame.Layout == "place":
                frame.place(relwidth=1, relheight=1)
            elif frame.Layout == "grid":                
                frame.grid(row=0, column=0, sticky="nsew")
            
            #Create button for the page            
            self.NavigationButtons[I] = (ttk.Button(self.NavigationFrame, text=self.Pages[I].Title))                      
            self.NavigationButtons[I].config(command=action)
            self.NavigationButtons[I].place(relx=0, rely=y, relwidth=1)  
   
    def ShowFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def _Quit(self, event=None):
        self.SQL.DisConnect()
        self.destroy()
 
if __name__ == '__main__':  
    app = Main()
    app.mainloop()   