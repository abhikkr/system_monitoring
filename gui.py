import tkinter

import customtkinter
from tkinter import *
from tkinter import ttk

import check_cpu
from check_cpu import *


#frame
app = tkinter.Tk()
app.geometry("800x720")
app.config(background="black")
app.title("test")

#system setting
customtkinter.set_default_color_theme("green")

#ui elements
def ram_use():
    t = check_cpu.ram_usage()
    ui_label.configure(text=str(t)+"%")
    ui_label.after(1000,ram_use)

def cpu_use():
    u = check_cpu.monitor_cpu_usage()
    ui_label_cpu.configure(text=str(u) + "%")
    ui_label_cpu.after(1000, cpu_use)

ui_label_title = customtkinter.CTkLabel(app,text="test product_ram",text_color="white",font=("arial",45))
# ui_label_title.grid(row=1,column=1)
ui_label_title.pack()
ui_label = customtkinter.CTkLabel(app,text=".......",font=("italic",30))
# ui_label.grid(row=2,column=1)
ui_label.pack()
ui_button = customtkinter.CTkButton(app,text="button",command=ram_use)
# ui_button.grid(row=3,column=1)
ui_button.pack()

#cpu uselabel
ui_label_title_cpu = customtkinter.CTkLabel(app,text="test product_cpu",text_color="white",font=("arial",45))
# ui_label_title_cpu.grid(row=1,column=2,padx=50,  pady=5)
ui_label_title_cpu.pack()
ui_label_cpu = customtkinter.CTkLabel(app,text="-----------",font=("italic",30))
# ui_label.grid(row=2,column=2)
ui_label_cpu.pack()
ui_button_cpu = customtkinter.CTkButton(app,text="button_cpu",command=cpu_use)
# ui_button_cpu.grid(row=3,column=2)
ui_button_cpu.pack()
# time_source()
app.mainloop()