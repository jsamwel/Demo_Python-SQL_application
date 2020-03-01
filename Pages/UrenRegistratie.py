import sys
sys.path.insert(0, sys.path[0]+'../')

import calendar

from tkinter import ttk

from Tools.CalendarDialog import Calendar
from Tools.TimeEntry import TimeEntry

class InvoerRij:
    def __init__(self, Frame, Werknemer, x, y, RegOld=None):        
        self.Frame = Frame
        self.Updated = 0
        self._Werknemer = Werknemer[0]
        
        self.Werknemer = ttk.Label(self.Frame, text=self._Werknemer)
        self.Werknemer.place(relx=x, rely=y)
        
        self.StartTijd = TimeEntry(self.Frame)
        self.StartTijd.place(relx=x+.1, rely=y)
        
        self.StopTijd = TimeEntry(self.Frame)
        self.StopTijd.place(relx=x+.18, rely=y)
        
        if RegOld:            
            self.Updated = 1
            
            self.StartTijd.Time = RegOld[3].strftime('%H:%M')
            self.StopTijd.Time = RegOld[4].strftime('%H:%M')
        
    def GetData(self):        
        return [self._Werknemer, self.StartTijd.Time, self.StopTijd.Time]
    
    def Destroy(self):
        self.Werknemer.destroy()
        self.StartTijd.destroy()
        self.StopTijd.destroy()
        
            
class UrenRegistratie(ttk.Frame):
    Layout = "grid"
    Title = "Uren registratie"
    
    def __init__(self, parent, controller, SQL):
        ttk.Frame.__init__(self, parent)
        
        self.SQL = SQL     
        
        self._Datum = calendar.datetime.date.today()
           
        self._Werknemers = None
        self._InvoerRijen = {}  

        self._BuildLabelsButtons()
        self._BuildPage()   
        
        # Update page when SQL connection changes
        controller.SQL.TKConnected.trace(mode="w", callback=self._SQLConnectionChange)
      
    def _BuildPage(self):
        # Adds every employee that was active on the selected date to the page
        
        # Remove the existing entries
        if self._InvoerRijen:
            for i in self._InvoerRijen:
                self._InvoerRijen[i].Destroy()                
        
        
        # Retrieve the active employees and add the entries for the employees to the page
        WerknemerQuery = """select name from employees 
                            where startdate < %s and (enddate is null or enddate >= %s)"""
        RegistratieQuery = """select * from uurregistratie 
                            where date = %s"""
        
        if self.SQL.Connected:
            self._Werknemers = self.SQL.FetchQuery(WerknemerQuery, [self._Datum.strftime('%d-%m-%Y'), self._Datum.strftime('%d-%m-%Y')])
            self._UurRegOld = self.SQL.FetchQuery(RegistratieQuery, [self._Datum.strftime('%d-%m-%Y')])
            
            for F in range(len(self._Werknemers)):
                RegOld = None
                
                x = .05
                y = .1 + F * .05
                            
                for U in self._UurRegOld:
                    if U[2] == self._Werknemers[F][0]:
                        RegOld = U                    
                
                self._InvoerRijen[self._Werknemers[F]] = InvoerRij(self, self._Werknemers[F], x, y, RegOld)
        
    def _BuildLabelsButtons(self):                 
        self._CalendarFrame = None
        
        self._ButtonSave = ttk.Button(self, text='Save', command=self._Save)
        self._ButtonSave.place(relx=.4, rely=.02)
        
        self._ButtonMoveDateToCurrent = ttk.Button(self, text='Today', command=self._MoveDateToCurrent)
        self._ButtonMoveDateToCurrent.place(relx=.15, rely=.02, relheight=.03)
        
        self._LabelStartTijd = ttk.Label(self, text='Start tijd')
        self._LabelStartTijd.place(relx=.15, rely=.06)
        
        self._LabelStopTijd = ttk.Label(self, text='Stop tijd')
        self._LabelStopTijd.place(relx=.23, rely=.06)
         
        self._LabelDatum = ttk.Label(self, text='Date:')
        self._LabelDatum.place(relx=.05, rely=.02, relwidth=.03, relheight=.03)       
            
        self._ButtonDatum = ttk.Button(self, text=self._Datum)
        self._ButtonDatum.config(command=self._ToggleCalendar)
        self._ButtonDatum.place(relx=.08, rely=.02, relheight=.03)
        
    def _ToggleCalendar(self):
        if self._CalendarFrame == None:
            self._CalendarFrame = Calendar(firstweekday=calendar.MONDAY, 
                                           callback=self._DestroyCalendar,
                                           month=self._Datum.month)
            
            self._CalendarFrame.place(in_=self, relx=.03, rely=.05) 
            self.bind("<Button-1>", self._DestroyCalendar)                                      
        else: 
            self._DestroyCalendar()           
                   
    def _DestroyCalendar(self, event=None):
        if self._CalendarFrame.selection is not None:
                self._Datum = self._CalendarFrame.selection.date()
                self._ButtonDatum.config(text=self._Datum)
                self._BuildPage()
        
        self.unbind("<Button-1>")   
        self._CalendarFrame.destroy()
        self._CalendarFrame = None
        
    def _MoveDateToCurrent(self):
        self._Datum = calendar.datetime.date.today()
        
        self._ButtonDatum.config(text=self._Datum)
        
        self._BuildPage()
        
    def _Save(self):
        UpdateQuery = """UPDATE uurregistratie 
                        SET starttime = %s, endtime = %s 
                        WHERE date = %s and employee = %s"""
        InsertQuery = """INSERT INTO uurregistratie
                        VALUES(DEFAULT, %s, %s, %s, %s)"""                           
                                    
        if self.SQL.Connected:
            for rij in self._InvoerRijen:
                Data = self._InvoerRijen[rij].GetData()
                
                if self._InvoerRijen[rij].Updated:    
                    self.SQL.InsertQuery(UpdateQuery, [Data[1], Data[2], self._Datum.strftime('%Y-%m-%d'), Data[0]])                    
                else:                 
                    self.SQL.InsertQuery(InsertQuery, [self._Datum.strftime('%Y-%m-%d'), Data[0], Data[1], Data[2]])   
                    
            self._BuildPage()
            
    def _SQLConnectionChange(self, *args, **kw):               
        self._BuildPage()