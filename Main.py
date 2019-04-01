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
from Pages.SettingsPage import SettingsPage

from Tools.SQLConnection import Connection

class Main(themed_tk.ThemedTk):
    def __init__(self): 
        super().__init__()         
        # set the state of the window and add functionility to the escape button and the close button          
        self.state('zoomed')
        self.protocol("WM_DELETE_WINDOW", self._Quit)
        self.bind("<Escape>", self._Quit)  
        
        # Select style for ttk
        # print(self.get_themes())
        self.set_theme('arc')
       
        # Frames for the pages and the navigation
        self.container = ttk.Frame(self)        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.place(relx=0.15, rely=0, relwidth=.85, relheight=1)
        
        self.NavigationFrame = ttk.Frame(self)        
        self.NavigationFrame.place(relx=0, rely=0 , relwidth=.15, relheight=1)
        
        # Call functions for SQL and creating the pages
        self._CreateSQLConnection()
        self._CreatePages()
        self._CreateMenu()
        
        # Set the default page
        self.ShowFrame(StartPage)
        
    def _CreateSQLConnection(self):
        # Create SQl connection
        hostname    = 'localhost'
        user        = 'postgres'
        password    = 'WWPostgres'
        database    = 'DataDevelopment'
        
        self.SQL = Connection(hostname, user, password, database)
        self.SQL.Connect()         
        
    def _CreatePages(self):
        # Create pages and navigation buttons  
        self.Pages = (StartPage, GraphPage, UrenRegistratie, Werknemers, SettingsPage)
        self.NavigationButtons = {}        
        self.frames = {}
        
        for I in range(len(self.Pages)):
            # Navigation command for the button
            action = lambda x = self.Pages[I]: self.ShowFrame(x)   
            
            # Location for the button
            y = .05 + I * .04            
            
            # Create the page
            frame = self.Pages[I](self.container, self, self.SQL)
            
            self.frames[self.Pages[I]] = frame
                        
            if frame.Layout == "place":
                frame.place(relwidth=1, relheight=1)
            elif frame.Layout == "grid":                
                frame.grid(row=0, column=0, sticky="nsew")
            
            # Create button for the page 
            # Excludes the settingspage from the navigationbar
            if self.Pages[I] is not SettingsPage:
                self.NavigationButtons[I] = (ttk.Button(self.NavigationFrame, text=self.Pages[I].Title))                      
                self.NavigationButtons[I].config(command=action)
                self.NavigationButtons[I].place(relx=0, rely=y, relwidth=1, relheight=.04)  
            
    def _CreateMenu(self):
        self._Menubar = tk.Menu(self)
        
        # Add file menu
        self._filemenu = tk.Menu(self._Menubar, tearoff=0)        
        self._filemenu.add_command(label="Settings", command= lambda x = SettingsPage: self.ShowFrame(x))
        self._filemenu.add_separator()        
        self._filemenu.add_command(label="Exit", command=self._Quit)        
        self._Menubar.add_cascade(label="File", menu=self._filemenu)
        
        # Add help menu
        self._helpmenu = tk.Menu(self._Menubar, tearoff=0)
        self._helpmenu.add_command(label="Help Index", command=None)
        self._helpmenu.add_command(label="About...", command=None)
        self._Menubar.add_cascade(label="Help", menu=self._helpmenu)
        
        self.config(menu=self._Menubar)
   
    def ShowFrame(self, cont):
        # Function for navigating between pages
        frame = self.frames[cont]
        frame.tkraise()
        
        # If not connected, try to reconnect with page refresh
        if not self.SQL.Connected:
            self.SQL.Connect()
        
    def _Quit(self, event=None):
        # Function that handles the closing of the app
        self.SQL.DisConnect()
        self.destroy()
 
if __name__ == '__main__':  
    app = Main()
    app.mainloop()   