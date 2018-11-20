# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:10:20 2018

@author: JolanSamwel
"""

import matplotlib

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

class GraphPage(tk.Frame):
    Layout = "grid"
    Title = "Graph page"

    def __init__(self, parent, controller, SQL):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Graph Page!")
        label.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")

        toolbarFrame = tk.Frame(master=self)
        toolbarFrame.grid(row=2,column=0, sticky="nsew")
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)