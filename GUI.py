import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from ttkbootstrap.scrolled import ScrolledText
import random as r
class Application(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill="both", expand=True, side=TOP)
        
        style = Style("superhero")
        style.configure('TLabel', font=('Helvetica', 42))
        
        self.Cost_Display = ttk.Frame(self)
        self.Cost_Display.grid(row= 1, column=0, sticky="nsew")
        
        self.Cost_Display_options = ttk.Notebook(self.Cost_Display)
        
        self.Anual = ttk.Label(self,text='Anually',justify='center')
        self.Week = ttk.Label(self,text='Weekly')
        self.Month = ttk.Label(self,text='Monthly')
        
        self.Cost_Display_options.add(self.Anual,text='Monthly')
        self.Cost_Display_options.add(self.Week,text='Weekly')
        self.Cost_Display_options.add(self.Month,text='Anually')
        
        self.Cost_Display_options.pack()
        
        self.Power_Monitor = ttk.Frame(self)
        self.Power_Monitor.grid(row=2, column=0, sticky="nsew")
        
        self.Power_Monitor_meter = ttk.Meter(self.Power_Monitor, bootstyle="info", textright="", subtext="Kw/h", amountused=430, interactive=False,metertype='semi',amounttotal=1000)
        self.Power_Monitor_meter.pack(fill="both", expand=True, side=TOP, pady=30, padx=30)
        
        self.update()
    
    def update(self):
        self.Power_Monitor_meter.configure(amountused=11)
        
if __name__ == "__main__":
    app = ttk.Window("Power Monitor", themename="superhero")
    main = Application(app)
    app.mainloop()