# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 18:30:02 2018

@author: JSamwel
"""

import psycopg2
from threading import Thread
import tkinter as tk

class Connection:
    def __init__(self, Host, user, password, database):        
        self.hostname   = Host
        self.username   = user
        self.password   = password
        self.DB         = database
        
        self.TKConnected    = tk.IntVar()
        self._Connected     = False
        self._Connecting    = False
        self.Error          = ''
        
    def InsertQuery(self, Command, Data):
        # Function for inserting/updating data in the SQL database
        
        if self.Connected:
            try:
                cur = self.conn.cursor()
                cur.execute(Command, Data)
                
                self.conn.commit()  
                cur.close()
                
            except psycopg2.OperationalError as e:
                self.Connected.set(0)
                self.Error = e
 
    def FetchQuery(self, Command, Data=[]):
        # Function for retrieving data from the SQL database
        
        if self.Connected:
            try:
                cur = self.conn.cursor()
                cur.execute(Command, Data)
                
                data = cur.fetchall()
                
                cur.close()
                
                return data
            
            except psycopg2.OperationalError as e:
                self.Connected.set(0)
                self.Error = e
                return None
        else:
            return None
    
    def FetchColumn(self, Table, Column):
        # Function for retrieving a single column from the SQL database, returns
        # a list with one dimension
        
        if self.Connected:
            try:
                cur = self.conn.cursor()
                cur.execute("select %s from %s", (Table, Column))
                
                data = [r[0] for r in self.cur.fetchall()]
                
                cur.close()
                
                return data
            
            except psycopg2.OperationalError as e:
                self.Connected.set(0)
                self.Error = e
                return None
        
        else:
            return None
    
    def Connect(self):
        # Start a seperate thread to prevent that the program becomes unresponsive when
        # there isn't a SQL connection
        if not self._Connecting:
            threaded = Thread(target=self.ConnectThread)
            # This thread dies when main thread (only non-daemon thread) exits.
            threaded.daemon = True  
            threaded.start() 
            
        self.Connected = self._Connected
            
    def ConnectThread(self):
        # Create connection with database
        self._Connecting = True
        
        try:
            self.conn = psycopg2.connect(database=self.DB, user=self.username, 
                                     password=self.password)            
            
        except psycopg2.OperationalError as e:
            self._Connected = False            
            self.Error = e            
        else:
            self._Connected = True
            self.Error = '' 
            
        self._Connecting = False
            
    @property    
    def Connected(self):
        return self.TKConnected.get()
        
    @Connected.setter
    def Connected(self, value):
        self.TKConnected.set(value)
        
    def DisConnect(self):
        # Closes the connection when a connection has been made
        if self.Connected:
            self.conn.close()        