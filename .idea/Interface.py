import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('blue')
class Window():
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry('400x400')
        self.CalculationType = ctk.StringVar(value='Sourse')
        self.L_Sourse_phi_start = 0
        self.L_Sourse_phi_finish = 0
        self.DEFAULT_XS = 0
        self.DEFAULT_YS = 0
        self.L_Sourse_Xs = 0
        self.T_Sourse_Xs = 0
        self.L_Sourse_Ys = 0
        self.T_Sourse_Ys = 0
        self.Sourse_Fill = ctk.StringVar(value='N')
        self.Sourse_FillCombobox = 0

        combobox = ctk.CTkOptionMenu(master=self.window,values=['Sourse','Plane Wave','Radiation Pattern'],
                                     variable=self.CalculationType,fg_color='silver',text_color = 'teal')
        combobox.grid(column = 0,row = 0)
        combobox.configure(command = self.CreateMenu)

    def CreateMenu(self,value):
        if value == 'Sourse':
            if self.L_Sourse_Xs != 0:
                self.L_Sourse_Xs.destroy()
            self.L_Sourse_Xs = ctk.CTkLabel(self.window,text=f'Input Xs')
            # self.L_Sourse_Xs.pack(padx=0,pady = 0,anchor = ctk.W)
            self.L_Sourse_Xs.grid(column = 0,row = 1)
            self.T_Sourse_Xs = ctk.CTkTextbox(self.window,width = 100,height=25,fg_color = 'silver',text_color = 'teal')
            self.T_Sourse_Xs.grid(column = 1,row = 1)
            self.T_Sourse_Xs.insert("0.0", str(self.DEFAULT_XS))
            #
            self.L_Sourse_Ys = ctk.CTkLabel(self.window,text=f'Input Ys')
            self.L_Sourse_Ys.grid(column = 0,row = 2)
            self.T_Sourse_Ys = ctk.CTkTextbox(self.window,width = 100,height=25,fg_color = 'silver',text_color = 'teal')
            self.T_Sourse_Ys.grid(column = 1,row = 2)
            self.T_Sourse_Ys.insert("0.0", str(self.DEFAULT_XS))
            #
            ctk.CTkLabel(self.window,text=f'FillType').grid(column = 0,row = 3)
            self.Sourse_FillCombobox = ctk.CTkOptionMenu(master=self.window,
                                                         values=['N','linespace'],
                                         variable=self.Sourse_Fill,fg_color='silver',text_color = 'teal')
            self.Sourse_FillCombobox.grid(column = 1,row = 3)
            # self.T_Sourse_Xs.place(relx=0.1,y = 0)
        else:
            self.window.de



if __name__ == "__main__":
    page = Window()
    page.window.mainloop()