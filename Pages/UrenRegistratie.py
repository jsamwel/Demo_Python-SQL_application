import calendar

import tkinter as tk
from tkinter import ttk

from Tools.CalendarDialog import Calendar
from Tools.TimeEntry import TimeEntry

class InvoerRij:
    def __init__(self, Frame, Werknemer, x, y, ShowLabels=False):        
        self.Frame = Frame
        
        self.Werknemer = tk.Label(self.Frame, text=Werknemer)
        self.Werknemer.place(relx=x, rely=y)
        
        self.StartTijd = TimeEntry(self.Frame, x+.1, y)
        
    def GetData(self):
        return self.StartTijd.get()
            
class UrenRegistratie(tk.Frame):
    Layout = "grid"
    Title = "Uren registratie"
    
    def __init__(self, parent, controller, SQL):
        tk.Frame.__init__(self, parent)       
        
        self.bind("<Button-1>", self._DestroyCalendar)  
        
        self._Datum = calendar.datetime.date.today()        
        self._CalendarFrame = None 
        
        self._Werknemers = None
        self._InvoerRijen = {}  

        self._BuildPage()        
      
    def _BuildPage(self):
        self._Werknemers = ('Yoeri Samwel','Jolan Samwel' , 'Fiona van de Haar')
        
        self._LabelStartTijd = tk.Label(self, text='Start tijd')
        self._LabelStartTijd.place(relx=.15, rely=.06)
        
        self._LabelDatum = ttk.Label(self, text='Date:')
        self._LabelDatum.place(relx=.05, rely=.02, relwidth=.03, relheight=.03)       
            
        self._ButtonDatum = ttk.Button(self, text=self._Datum)
        self._ButtonDatum.config(command=self._ShowCalendar)
        self._ButtonDatum.place(relx=.08, rely=.02, relheight=.03)
           
        for F in range(len(self._Werknemers)):
            x = .05
            y = .1 + F * .05
            
            self._InvoerRijen[self._Werknemers[F]] = InvoerRij(self, self._Werknemers[F], x, y)
        
    def _ShowCalendar(self):
        if self._CalendarFrame == None:
            self._CalendarFrame = Calendar(firstweekday=calendar.MONDAY, callback=self._DestroyCalendar)
            self._CalendarFrame.place(in_=self, relx=.03, rely=.05)                                       
        else: 
            self._DestroyCalendar()           
                   
    def _DestroyCalendar(self, event=None):
        if self._CalendarFrame.selection is not None:
                self._Datum = self._CalendarFrame.selection.date()
                self._ButtonDatum.config(text=self._Datum)
                
        self._CalendarFrame.destroy()
        self._CalendarFrame = None