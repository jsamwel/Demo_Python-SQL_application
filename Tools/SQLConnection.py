# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 18:30:02 2018

@author: JSamwel
"""

import psycopg2
import tkinter as tk

class Connection:
    def __init__(self, Host, user, password, database):        
        self.hostname   = Host
        self.username   = user
        self.password   = password
        self.DB         = database
        
        self.Connected = tk.IntVar()
        self.Error = ''
        
    def InsertQuery(self, Command, Data):
        cur = self.conn.cursor()
        cur.execute(Command, Data)
        
        self.conn.commit()  
        cur.close()
 
    def FetchQuery(self, Command, Data):
        cur = self.conn.cursor()
        cur.execute(Command, Data)
        
        data = cur.fetchall()
        
        cur.close()
        
        return data
    
    def FetchColumn(self, Table, Column):
        cur = self.conn.cursor()
        cur.execute("select %s from %s", (Table, Column))
        
        data = [r[0] for r in self.cur.fetchall()]
        
        cur.close()
        
        return data
    
    def Connect(self):
        # Create connection with database
        try:
            self.conn = psycopg2.connect(database=self.DB, user=self.username, 
                                     password=self.password)            
            
        except psycopg2.OperationalError as e:
            self.Connected.set(0)
            self.Error = e
        else:
            self.Connected.set(1)
            self.Error = ''
        
    def DisConnect(self):
        if self.Connected.get():
            self.conn.close()        