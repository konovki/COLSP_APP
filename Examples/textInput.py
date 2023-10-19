from tkinter import *
import customtkinter

def getText():
    print(textbox.get('1.0', END))

root = customtkinter.CTk()

textbox = customtkinter.CTkTextbox(root)
button = customtkinter.CTkButton(root, command=getText)
textbox.pack(pady=30, padx=20)
button.pack(pady=30, padx=20)

root.mainloop()