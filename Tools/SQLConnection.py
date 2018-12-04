# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 18:30:02 2018

@author: JSamwel
"""

import psycopg2

class Connection:
    def __init__(self, Host, user, password, database):        
        self.hostname = Host
        self.username = user
        self.password = password
        self.DB = database
        
        self.Connected = 0
        
    def InsertQuery(self, Command):     
        self.cur.execute(Command)
        
        self.conn.commit()        
 
    def FetchQuery(self, Command):
        self.cur.execute(Command)
        
        return self.cur.fetchall()
    
    def FetchColumn(self, Table, Column):
        self.cur.execute("select %s from %s", (Table, Column))
        
        return [r[0] for r in self.cur.fetchall()]
    
    def Connect(self):
        # Create connection with database
        try:
            self.conn = psycopg2.connect(database=self.DB, user=self.username, 
                                     password=self.password)
            
            self.cur = self.conn.cursor()
            self.Connected = 1
        except:
            self.Connected = 0
        
    def DisConnect(self):
        if self.Connected:
            self.conn.close()        