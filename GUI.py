import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from ttkbootstrap.scrolled import ScrolledText
import random as r
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import numpy as np
from matplotlib.figure import Figure
class Application(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill="both", expand=True, side=TOP)
        style = Style("superhero")
        style.configure('TLabel', font=('Helvetica', 24))
        
        self.manual = ttk.Frame(self)
        self.manual.grid(row=0,column=0,sticky="nsew")
        self.manual_label = ttk.Label(self.manual,text='Enter price Per Kwh manually:')
        self.manual_input = ttk.Entry(self.manual)
        self.manual_Button = ttk.Button(self.manual,text = 'Submit',command=self.manual_push_cost)
        self.manual_label.grid(row=0)
        self.manual_Button.grid(row=2)
        self.manual_input.grid(row=1)
    def update(self):
        value = r.randint(0,200)
        self.Power_Monitor_meter.configure(amountused=value)
        self.Cost.configure(text=f'£{round(float(value * self.Rate),2)}')
        self.Power_Monitor_meter.after(200,self.update)
        
    def mainpage(self):
        self.Cost_Display = ttk.Frame(self)
        self.Cost_Display.grid(row= 1, column=0, sticky="nsew")
        self.Cost_header = ttk.Label(self.Cost_Display,text="Cost:")
        self.Cost = ttk.Label(self.Cost_Display,text="£0.00")
        self.Cost_header.pack()
        self.Cost.pack()
        
        self.Power_Monitor = ttk.Frame(self)
        self.Power_Monitor.grid(row=2, column=0, sticky="nsew")
        
        self.Power_Monitor_meter = ttk.Meter(self.Power_Monitor, bootstyle="info", textright="", subtext="Kw/h", amountused=0, interactive=False,metertype='semi',amounttotal=1000)
        self.Power_Monitor_meter.pack(fill="both", expand=True, side=TOP, pady=30, padx=30)
        
        self.Power_Monitor_meter.after(1000,self.update)
    
    def manual_push_cost(self):
        self.Rate = float(self.manual_input.get())
        self.wipe()
        
    
    def wipe(self):
        windows = self.winfo_children()
        print(windows)
        for item in windows:
            if item.winfo_children():
                windows.extend(item.winfo_children())
        for item in windows:
            print('passed')
            item.destroy()
        self.mainpage()
if __name__ == "__main__":
    app = ttk.Window("Power Monitor", themename="superhero")
    Application(app)
    app.mainloop()
