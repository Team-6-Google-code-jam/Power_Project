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
        # style.configure('TLabel', font=('Helvetica', 24))
        
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
        
        self.graph_display = ttk.Frame(self)
        self.graph_display.grid(row= 1, column=1, sticky="nsew")
        self.graph_header = ttk.Label(self.graph_display,text="Cost:")
        self.graph_header.pack()
        self.graph = Figure(figsize = (5,4), dpi = 100)
        self.ax = self.graph.add_subplot()
        t = np.arange(0, 3, .01)
        self.line, = self.ax.plot(t, 2 * np.sin(2 * np.pi * t))
        self.ax.set_xlabel("time [s]")
        self.ax.set_ylabel("f(t)")
        self.canvas = FigureCanvasTkAgg(self.graph, master=self.graph_display)
        self.canvas.draw()
        self.Power_Monitor_meter.after(1000,self.update)
    def update(self):
        value = r.randint(0,200)
        self.Power_Monitor_meter.configure(amountused=value)
        self.Cost.configure(text=f'£{round(float(value * 0.27),2)}')
        self.Power_Monitor_meter.after(200,self.update)
        

if __name__ == "__main__":
    app = ttk.Window("Power Monitor", themename="superhero")
    Application(app)
    app.mainloop()

# import tkinter

# import numpy as np

# # Implement the default Matplotlib key bindings.
# from matplotlib.backend_bases import key_press_handler
# from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
#                                                NavigationToolbar2Tk)
# from matplotlib.figure import Figure

# root = tkinter.Tk()
# root.wm_title("Embedding in Tk")

# fig = Figure(figsize=(5, 4), dpi=100)
# t = np.arange(0, 3, .01)
# ax = fig.add_subplot()
# line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
# ax.set_xlabel("time [s]")
# ax.set_ylabel("f(t)")

# canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
# canvas.draw()

# # pack_toolbar=False will make it easier to use a layout manager later on.
# toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
# toolbar.update()

# canvas.mpl_connect(
#     "key_press_event", lambda event: print(f"you pressed {event.key}"))
# canvas.mpl_connect("key_press_event", key_press_handler)

# button_quit = tkinter.Button(master=root, text="Quit", command=root.destroy)


# def update_frequency(new_val):
#     # retrieve frequency
#     f = float(new_val)

#     # update data
#     y = 2 * np.sin(2 * np.pi * f * t)
#     line.set_data(t, y)

#     # required to update canvas and attached toolbar!
#     canvas.draw()


# slider_update = tkinter.Scale(root, from_=1, to=5, orient=tkinter.HORIZONTAL,
#                               command=update_frequency, label="Frequency [Hz]")

# # Packing order is important. Widgets are processed sequentially and if there
# # is no space left, because the window is too small, they are not displayed.
# # The canvas is rather flexible in its size, so we pack it last which makes
# # sure the UI controls are displayed as long as possible.
# button_quit.pack(side=tkinter.BOTTOM)
# slider_update.pack(side=tkinter.BOTTOM)
# toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
# canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

# tkinter.mainloop()