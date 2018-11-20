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

from Tools.SQLConnection import Connection

class Main():
    def __init__(self, Frame): 
        self.Frame = Frame 
        #self.Frame.root.geometry("800x400+100+100")
        self.Frame.attributes("-fullscreen", True)
        self.Frame.bind("<Escape>", self._Quit)
        
        #Select style for ttk
        #'winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative'
        style = ttk.Style()
        style.theme_use('clam')
        #self.Frame.set_theme("equilux") 
       
        #Frames for the pages and the navigation
        self.container = ttk.Frame(self.Frame)
        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.NavigationFrame = ttk.Frame(self.Frame)
        
        self.container.place(relx=0.15, rely=0 , relwidth=.85, relheight=1)
        self.NavigationFrame.place(relx=0, rely=0 , relwidth=.15, relheight=1)
        
        self._CreateSQLConnection()
        self._CreatePages()
        
        self.show_frame(StartPage)
        
    def _CreateSQLConnection(self):
         #Create SQl connection
        hostname = 'localhost'
        hostname = 'postgres'
        password = 'WWPostgres'
        database = 'DataDevelopment'
        
        self.SQL = Connection(hostname, hostname, password, database)
        self.SQL.Connect()         
        
    def _CreatePages(self):
        #Create pages and navigation buttons  
        self.Pages = (StartPage, GraphPage, UrenRegistratie)
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
            action = lambda x = self.Pages[I]: self.show_frame(x)   
            
            #Location for the button
            y = 35 + I * 28            
            
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
            self.NavigationButtons[I].place(relx=0, y=y, relwidth=1)  
   
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def _Quit(self, event=None):
        self.SQL.DisConnect()
        self.Frame.destroy()
 
if __name__ == '__main__':       
    #root = tk.Tk()
    root = themed_tk.ThemedTk()
    
    app = Main(root)
    root.mainloop()   