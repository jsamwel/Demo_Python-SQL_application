# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 10:00:46 2018

@author: JolanSamwel
"""

import tkinter as tk

class InvoerRij:
    def __init__(self, Frame, x, y):
        self.Frame = Frame
        
        self.Werknemer = tk.Label(self.Frame, text="Yoeri Samwel")
        self.Werknemer.place(relx=x, rely=y)
        
        self.StartTijd = tk.Entry(self.Frame)
        self.StartTijd.place(relx=x+.15, rely=y)
        
class UrenRegistratie(tk.Frame):
    def __init__(self, parent, controller, SQL):
        tk.Frame.__init__(self, parent)
        
        self.InvoerRijen = []
        
        self.LabelStartTijd = tk.Label(self, text="Start tijd")
        self.LabelStartTijd.place(relx=.25, rely=.05)
        
        Rij1 = InvoerRij(self, .1, .1)
        Rij2 = InvoerRij(self, .1, .15)
        
        #for I in range(5):