import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from psutil import cpu_percent
# from psutil import sensors_battery
from os.path import exists
import json
from collections import deque
import numpy as np
class Application(ttk.Frame):
    def __init__(self, *args, **kwargs):
        '''
        On initialization, define constants and load 
        settings
        '''
        self.timeconversion = 1/60/60/5
        self.time = 0
        self.average_cache = deque(
            maxlen=1000
            )
        super().__init__(
            *args,
            **kwargs
            )
        self.pack(
            fill="both",
            expand=True,
            side=TOP
            )
        style = Style(
            "superhero"
            )
        self.total_use=0
        self.load_settings()
        
    def update(self):
        '''
        Run An update cycle
        '''
        self.time += self.timeconversion
        self.current_draw = float(
            cpu_percent() * self.cpu_ratio
            )
        self.average_cache.append(
            self.current_draw
            )
        if self.total_use == 0:
            self.total_use = self.time * 250
        else:
            self.total_use += self.current_draw * self.timeconversion
        self.price = self.total_use * self.Rate * 0.01
        self.Cost.configure(
            text=f'£{round(self.price,2)}')
        self.time_monitor_meter.configure(
            amountused=round(
                self.time,
                2
                )
            )
        self.power_monitor_meter.configure(
            amountused=round(
                self.current_draw,
                2)
            )
        self.average.configure(
            text = f'{round(np.mean(self.average_cache),2)}w/h'
                    )
        self.total.configure(
            text=f'{round(self.total_use,2)}w'
                )
        self.Cost.after(
            200,
            self.update
            )
    def mainpage(self):
        '''
        Generates the Main page
        '''
        style = Style(
            self.Mode
            )
        self.Cost_Display = ttk.Frame(
            self,style='dark'
            )
        self.Cost_Display.grid(
            row= 1,
            column=1,
            rowspan=2, 
            sticky="nsew"
            )
        self.Cost_header = ttk.Label(
            self.Cost_Display,
            text="Estimated cost for this session:\n",
            font=('Helvetica', 24),
            bootstyle="inverse-dark"
            )
        self.Cost = ttk.Label(
            self.Cost_Display,
            text="£0.00",
            font=('Helvetica', 24),
            bootstyle="inverse-dark"
            )
        self.average_header = ttk.Label(
            self.Cost_Display,
            text="\n\nAverage system power draw:\n",
            font=('Helvetica', 24),
            bootstyle="inverse-dark"
            )
        self.average = ttk.Label(
            self.Cost_Display,
            text="135.06w",
            font=('Helvetica', 24),
            bootstyle="inverse-dark"
            )
        self.total_header = ttk.Label(
            self.Cost_Display,
            text="\n\nTotal power use this session:\n",
            font=('Helvetica', 24),
            bootstyle="inverse-dark"
            )
        self.total = ttk.Label(
            self.Cost_Display,
            text=f'{self.total_use}w',
            font=('Helvetica', 24),
            bootstyle="inverse-dark"
            )
        self.Cost_header.pack()
        self.Cost.pack()
        self.total_header.pack()
        self.total.pack()
        self.average_header.pack()
        self.average.pack()
        
        self.time_monitor = ttk.Frame(
            self,
            style="default"
            )
        self.time_monitor.grid(
            row=1,
            column=0,
            sticky="nsew"
            )
        self.time_monitor_header = ttk.Label(
            self.time_monitor,
            text='Uptime this Session:'
            )
        self.time_monitor_meter = ttk.Meter(
            self.time_monitor,
            bootstyle="info",
            textright="",
            subtext="Hours",
            amountused=0,
            interactive=False,
            amounttotal=24,
            stripethickness=10
            )
        self.time_monitor_header.pack()
        self.time_monitor_meter.pack(
            fill="both",
            expand=True,
            side=TOP,
            pady=30,
            padx=30)
        
        self.power_monitor = ttk.Frame(
            self,
            style='default'
            )
        self.power_monitor.grid(
            row=2,
            column=0,
            sticky="nsew"
            )
        self.power_monitor_header = ttk.Label(
            self.power_monitor,
            text='Power Usage:'
            )
        self.power_monitor_meter = ttk.Meter(
            self.power_monitor,
            bootstyle="info", 
            textright="", 
            subtext="W/h", 
            amountused=0,
            metertype='semi',
            interactive=False,
            amounttotal=1000,
            subtextstyle="primary"
            )
        self.power_monitor_header.pack()
        self.power_monitor_meter.pack(
            fill="both",
            expand=True,
            side=TOP,
            pady=30,
            padx=30
            )
        
        self.settings = ttk.Frame(
            self,
            style="secondary"
            )
        self.settings.grid(
            column=0,
            row=0,
            columnspan=2, 
            sticky="nsew"
            )
        self.settings_button  = ttk.Button(
            self.settings,
            text='Settings',
            command=self.tosettings
            )
        self.settings_button.pack(
            side=LEFT
            )
        
        self.after(100,self.update)
    def settingspage(self):
        self.mainbar = ttk.Frame(
            self,
            style="secondary"
            )
        self.mainbar.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky="nsew"
            )
        self.home_button  = ttk.Button(
            self.mainbar,
            text='Home',
            command=self.tomain,
            style='danger'
            )
        self.settings_button  = ttk.Button(
            self.mainbar,
            text='Save',
            style='success',
            command=self.update_settings
            )
        self.home_button.pack(
            side=LEFT
            )
        self.settings_button.pack(
            side=LEFT
            )
        self.cpu_ratio_frame = ttk.Frame(
            self
        )
        self.cpu_ratio_frame.grid(
            column=0,
            row=1,
            columnspan=2
            )
        self.cpu_ratio_Label = ttk.Label(
            self.cpu_ratio_frame,
            text='\nFine tune Cpu power draw              \n'
        )
        self.cpu_ratio_slider = ttk.Scale(
            self.cpu_ratio_frame,
            to=100,
            value=self.cpu_ratio
        )
        self.cpu_ratio_Label.pack(
            side=LEFT
        )
        self.cpu_ratio_slider.pack(
            side=RIGHT
        )
        self.theme_select_frame = ttk.Frame(
            self
        )
        self.theme_select_frame.grid(
            column=0,
            row=2,
            columnspan=2
            )
        self.theme_select = ttk.Combobox(
            self.theme_select_frame,
        )
        self.theme_select['values']=['cosmo',
                       'flatly',
                       'journal',
                       'litera',
                       'lumen',
                       'minty',
                       'pulse',
                       'sandstone',
                       'united',
                       'yeti',
                       'morph',
                       'darkly',
                       'cyborg',
                       'superhero',
                       'solar']
        self.theme_select.insert('end',self.Mode)
        self.theme_select_label = ttk.Label(
            self.theme_select_frame,
            text="\nSelect a theme:                 \n"
        )
        self.theme_select_label.pack(side=LEFT)
        self.theme_select.pack(side=RIGHT)
        self.adjust_price_frame = ttk.Frame(
            self
        )
        self.adjust_price_frame.grid(
            column=0,
            row=3,
            columnspan=2
            )
        self.adjust_price = ttk.Entry(
            self.adjust_price_frame
        )
        self.adjust_price.insert('end',self.Rate)
        self.adjust_price_label = ttk.Label(
            self.adjust_price_frame,
            text= '\nAdjust price per Kw/h:         £\n'
        )
        self.adjust_price.pack(side=RIGHT)
        self.adjust_price_label.pack(side=LEFT)
        #enable laptop mode - do last!
    
    def load_settings(self):
        '''
        If there is no config file, loads a window allowing
        the user to input their electricity costs.
        '''
        if not exists('settings.json'):
            self.counties = {
                
            }
            self.input = ttk.Frame(
                self
                )
            self.input.grid(
                row=0,
                column=0,
                sticky="nsew"
                )
            self.manual_label = ttk.Label(
                self.input,
                text='Enter price Per Kwh manually:'
                )
            self.manual_input = ttk.Entry(
                self.input
                )
            self.manual_Button = ttk.Button(
                self.input,
                text = 'Submit',
                command=self.manual_push_cost
                )
            self.manual_label.grid(
                row=0
                )
            self.manual_Button.grid(
                row=2
                )
            self.manual_input.grid(
                row=1
                )
            self.or_label = ttk.Label(
                self.input,
                text='or'
                )
            self.drop_label = ttk.Label(
                self.input,
                text='Select region from List:'
                )
            self.drop_input = ttk.Combobox(
                self.input
                )
            self.drop_Button = ttk.Button(
                self.input,
                text = 'Submit',
                command=self.drop_push_cost
                )
            self.or_label.grid(
                row=3
                )
            self.drop_label.grid(
                row=4
                )
            self.drop_input.grid(
                row=5
                )
            self.drop_Button.grid(
                row=6
                )
        else:
            with open (
                'settings.json',
                'r+',encoding="utf-8"
                ) as options:
                options = json.load(
                    options
                    )
            self.cpu_ratio = options['CPU Ratio']
            self.Rate = float(
                options['Rate']
                )
            self.Mode = options['Mode']
            self.tomain()

    def update_settings(self):
        self.Rate = float(self.adjust_price.get())
        self.Mode = self.theme_select.get()
        self.cpu_ratio = self.cpu_ratio_slider.get()
        settings = {'CPU Ratio':self.cpu_ratio,
                    'Rate':self.Rate,
                    'Mode': self.Mode}
        with open(
            'settings.json',
            'w',
            encoding="utf-8") as path:
            json.dump(
                settings,
                path
                )
    
    def manual_push_cost(self):
        '''
        Loads default settings 
        '''
        settings = {'CPU Ratio':10,
                    'Rate':float(self.manual_input.get()),
                    'Mode': 'superhero'}
        with open(
            'settings.json',
            'w',
            encoding="utf-8") as path:
            json.dump(
                settings,
                path
                )
        self.load_settings()
        
    
    def wipe(self):
        '''
        Destroy all widgets to clear the window
        '''
        for item in self.winfo_children():
            item.destroy()
        
    def drop_push_cost(self):
        pass
    
    def tomain(self):
        '''
        Wipe the page and go to the main screen
        '''
        self.wipe()
        self.mainpage()

    def tosettings(self):
        self.wipe()
        self.settingspage()
if __name__ == "__main__":
    app = ttk.Window("Power Monitor")
    Application(app)
    app.mainloop()
