import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from ttkbootstrap.scrolled import ScrolledText
import random as r
from psutil import cpu_percent
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import numpy as np
from matplotlib.figure import Figure
class Application(ttk.Frame):
    def __init__(self, *args, **kwargs):
        
        self.counties = {
            
        }
        self.time = 0
        super().__init__(*args, **kwargs)
        self.pack(fill="both", expand=True, side=TOP)
        style = Style("superhero")
        # style.configure('TEntry', font=('Helvetica', 24))
        
        self.input = ttk.Frame(self)
        self.input.grid(row=0,column=0,sticky="nsew")
        self.manual_label = ttk.Label(self.input,text='Enter price Per Kwh manually:')
        self.manual_input = ttk.Entry(self.input)
        self.manual_Button = ttk.Button(self.input,text = 'Submit',command=self.manual_push_cost)
        self.manual_label.grid(row=0)
        self.manual_Button.grid(row=2)
        self.manual_input.grid(row=1)
        self.or_label = ttk.Label(self.input,text='or')
        self.drop_label = ttk.Label(self.input,text='Select region from List:')
        self.drop_input = ttk.Combobox(self.input)
        self.drop_Button = ttk.Button(self.input,text = 'Submit',command=self.drop_push_cost)
        self.or_label.grid(row=3)
        self.drop_label.grid(row=4)
        self.drop_input.grid(row=5)
        self.drop_Button.grid(row=6)
    def update(self):
        self.time += 0.1
        self.time = round(self.time,1)
        self.time_monitor_meter.configure(amountused=self.time)
        self.power_monitor_meter.configure(amountused=cpu_percent() * 10)
        self.Cost.configure(text=f'£{round(float(self.time * self.Rate),2)}')
        self.time_monitor_meter.after(200,self.update)
        
    def mainpage(self):
        self.Cost_Display = ttk.Frame(self)
        self.Cost_Display.grid(row= 1, column=1,rowspan=2, sticky="nsew")
        self.Cost_header = ttk.Label(self.Cost_Display,text="Estimated cost for this session:",font=('Helvetica', 24))
        self.Cost = ttk.Label(self.Cost_Display,text="£0.00",font=('Helvetica', 24))
        self.Cost_header.pack()
        self.Cost.pack()
        
        self.time_monitor = ttk.Frame(self,style="default")
        self.time_monitor.grid(row=1, column=0, sticky="nsew")
        self.time_monitor_header = ttk.Label(self.time_monitor,text='Uptime this Session:')
        self.time_monitor_meter = ttk.Meter(self.time_monitor, bootstyle="info", textright="", subtext="Hours", amountused=0, interactive=False,amounttotal=24,stripethickness=10)
        self.time_monitor_header.pack()
        self.time_monitor_meter.pack(fill="both", expand=True, side=TOP, pady=30, padx=30)
        
        self.power_monitor = ttk.Frame(self,style='default')
        self.power_monitor.grid(row=2, column=0, sticky="nsew")
        self.power_monitor_header = ttk.Label(self.power_monitor,text='Power Usage:')
        self.power_monitor_meter = ttk.Meter(self.power_monitor, bootstyle="info", textright="", subtext="W/h", amountused=0,metertype='semi', interactive=False,amounttotal=1000,subtextstyle="primary")
        self.power_monitor_header.pack()
        self.power_monitor_meter.pack(fill="both", expand=True, side=TOP, pady=30, padx=30)
        
        self.settings = ttk.Frame(self,style="secondary")
        self.settings.grid(column=0,row=0,columnspan=2, sticky="nsew")
        self.settings_button  = ttk.Button(self.settings,text='Settings')
        self.settings_button.pack(side=LEFT)
        
        self.after(100,self.update)
    
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
            item.destroy()
        self.mainpage()
        
    def drop_push_cost(self):
        pass
if __name__ == "__main__":
    app = ttk.Window("Power Monitor", themename="superhero")
    Application(app)
    app.mainloop()
