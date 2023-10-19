import tkinter as tk

import customtkinter as ctk
global label1
def CreateMenu(value):
    global label1
    print('Call')
    label1 = ctk.CTkLabel(app,text=f'Para')
    label1.pack(padx=300,pady = 5,anchor = ctk.W)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('blue')
app = ctk.CTk()
app.geometry('800x404')


CalculationType = ctk.StringVar(value='Sourse')
combobox = ctk.CTkOptionMenu(master=app,values=['Sourse','Plane Wave','Radiation Pattern'],
                            variable=CalculationType,fg_color='silver',text_color = 'teal')
combobox.pack(padx=10,pady = 5,anchor = ctk.W)
combobox.configure(command = CreateMenu)
combobox.place()
app.mainloop()