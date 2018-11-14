# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:55:31 2018

@author: JolanSamwel
"""

import tkinter as tk
from tkinter import ttk

from UrenRegistratie import UrenRegistratie
from GraphPage import GraphPage
from StartPage import StartPage

from SQLConnection import Connection

class Main():
    def __init__(self, Frame): 
        self.Frame = Frame
        
        #Master frame on which everything will be placed
        MainFrame = tk.Frame(self.Frame)
        MainFrame.pack(expand=True,fill="both")
                
        #Frames for the pages and the navigation
        container = tk.Frame(MainFrame)
        NavigationFrame = tk.Frame(MainFrame, bg="white")
        
        container.place(relx=0.15, rely=0 , relwidth=.85, relheight=1)
        NavigationFrame.place(relx=0, rely=0 , relwidth=.15, relheight=1)
        
        ConnectionLabel = tk.Label(NavigationFrame, text="", bg="white")
        ConnectionLabel.place(relx=0, rely=0, relwidth=1)
                
        #Create SQl connection
        hostname = 'localhost'
        hostname = 'postgres'
        password = 'WWPostgres'
        database = 'DataDevelopment'
        
        self.SQL = Connection(hostname, hostname, password, database)
        self.SQL.Connect()  
        
        if self.SQL.Connected:       
            ConnectionLabel.config(text="Connected", fg="black")
        else:
            ConnectionLabel.config(text="Not connected", fg="red")
        
        #Create pages and navigation buttons  
        self.Pages = (StartPage, GraphPage, UrenRegistratie)
        self.NavigationButtons = {}        
        self.frames = {}
            
        for I in range(len(self.Pages)):
            #Navigation command for the button
            action = lambda x = self.Pages[I]: self.show_frame(x)   
            
            #Location for the button
            y = 30 + I * 28            
            
            #Create the page
            frame = self.Pages[I](container, self, self.SQL)
            
            self.frames[self.Pages[I]] = frame
            
            if frame.Layout == "place":
                frame.place(relwidth=1, relheight=1)
            elif frame.Layout == "grid":
                frame.pack(expand=True,fill="both")
            
            #Create button for the page            
            self.NavigationButtons[I] = (tk.Button(NavigationFrame, text=self.Pages[I].Title))                      
            self.NavigationButtons[I].config(command=action)
            self.NavigationButtons[I].place(relx=0, y=y, relwidth=1)
                                
        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
root = tk.Tk()
root.geometry("800x400+100+100")
root.configure()
app = Main(root)
root.mainloop()   
app.SQL.DisConnect() 