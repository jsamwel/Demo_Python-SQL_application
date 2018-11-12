# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:55:31 2018

@author: JolanSamwel
"""

import tkinter as tk

from UrenRegistratie import UrenRegistratie
from SQLConnection import Connection

class Main():
    def __init__(self, Frame): 
        #Master frame on which everything will be placed
        MainFrame = tk.Frame(Frame)
        MainFrame.pack(expand=True,fill="both")
                
        #Frames for the pages and the navigation
        container = tk.Frame(MainFrame)
        NavigationFrame = tk.Frame(MainFrame, bg="white")
        
        container.place(relx=0.15, rely=0 , relwidth=.85, relheight=1)
        NavigationFrame.place(relx=0, rely=0 , relwidth=.15, relheight=1)
        
        #Created navigation
        button = tk.Button(MainFrame, text="Home",
                            command=lambda: self.show_frame(StartPage))
        button2 = tk.Button(MainFrame, text="Visit Page 1",
                            command=lambda: self.show_frame(PageOne))
        button3 = tk.Button(MainFrame, text="Uren registratie",
                            command=lambda: self.show_frame(UrenRegistratie))
        
        button.place(in_=NavigationFrame, relx=0, rely=.05)
        button2.place(in_=NavigationFrame, relx=0, rely=.1)
        button3.place(in_=NavigationFrame, relx=0, rely=.15)
        
        ConnectionLabel = tk.Label(MainFrame, text="", bg="white")
        ConnectionLabel.place(in_=NavigationFrame, relx=0, rely=0)
        
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
        
        #Create the pages of the GUI
        self.frames = {}

        for F in (StartPage, PageOne, UrenRegistratie):

            frame = F(container, self, self.SQL)

            self.frames[F] = frame
            
            frame.place(relwidth=1, relheight=1)
                        
        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):
    def __init__(self, parent, controller, SQL):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Start Page")
        label.place(relx=.1, rely=.1)

class PageOne(tk.Frame):
    def __init__(self, parent, controller, SQL):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Page One!!!")
        label.place(relx=.1, rely=.1)

root = tk.Tk()
root.geometry("800x700+300+300")
app = Main(root)
root.mainloop()   
app.SQL.DisConnect() 