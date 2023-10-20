import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('blue')
class Window():
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry('400x400')
        self.CalculationType = ctk.StringVar(value='Sourse')
        self.DEFAULT_XS = 0
        self.DEFAULT_YS = 0
        #Labels
        self.L_Sourse_phi_start = 0
        self.L_Sourse_phi_finish = 0
        self.L_Sourse_Xs = 0
        self.L_Sourse_Ys = 0
        self.L_FillType = 0
        self.L_Phi_Min = 0
        self.L_Phi_Max = 90
        #Text
        self.T_Sourse_Xs = 0
        self.T_Sourse_Ys = 0
        self.T_Phi_Min = 0
        self.T_Phi_Max = 0
        #Values
        self.Sourse_Fill = ctk.StringVar(value='N')
        self.Sourse_FillCombobox = 0
        self.StandartWidth = 100
        self.StandartHeight = 28
        self.Phi_Max = 90
        self.Phi_Min = 0
        self.DestroyArr = []
        combobox = ctk.CTkOptionMenu(master=self.window,values=['Sourse','Plane Wave','Radiation Pattern'],
                                     variable=self.CalculationType,fg_color='silver',text_color = 'teal')
        combobox.grid(column = 0,row = 0)
        combobox.configure(command = self.CreateMenu)
    def CreateMenu(self,value):
        if value == 'Sourse':
            L_Sourse_Xs = ctk.CTkLabel(self.window,text=f'Input Xs')
            L_Sourse_Xs.grid(column = 0,row = 1)
            self.DestroyArr.append(L_Sourse_Xs)
            T_Sourse_Xs = ctk.CTkTextbox(self.window,fg_color = 'silver',text_color = 'teal',
                                              width = self.StandartWidth,height=self.StandartHeight)
            T_Sourse_Xs.grid(column = 1,row = 1)
            T_Sourse_Xs.insert("0.0", str(self.DEFAULT_XS))
            self.DestroyArr.append(T_Sourse_Xs)
            #
            L_Sourse_Ys = ctk.CTkLabel(self.window,text=f'Input Ys')
            L_Sourse_Ys.grid(column = 0,row = 2)
            self.DestroyArr.append(L_Sourse_Ys)
            T_Sourse_Ys = ctk.CTkTextbox(self.window,fg_color = 'silver',text_color = 'teal',
                                              width = self.StandartWidth,height=self.StandartHeight)
            T_Sourse_Ys.grid(column = 1,row = 2)
            T_Sourse_Ys.insert("0.0", str(self.DEFAULT_XS))
            self.DestroyArr.append(T_Sourse_Ys)
            #
            L_Phi_Min=ctk.CTkLabel(self.window,text=f'Phi_Min')
            L_Phi_Min.grid(column = 0,row = 3)
            self.DestroyArr.append(L_Phi_Min)
            L_Phi_Max=ctk.CTkLabel(self.window,text=f'Phi_Max')
            L_Phi_Max.grid(column = 2,row = 3)
            self.DestroyArr.append(L_Phi_Max)
            T_Phi_Min = ctk.CTkTextbox(self.window,fg_color = 'silver',text_color = 'teal',
                                            width = self.StandartWidth,height=self.StandartHeight)
            T_Phi_Min.grid(column = 1,row = 3)
            T_Phi_Min.insert("0.0", str(self.Phi_Min))
            self.DestroyArr.append(T_Phi_Min)
            T_Phi_Max = ctk.CTkTextbox(self.window,fg_color = 'silver',text_color = 'teal',
                                            width = self.StandartWidth,height=self.StandartHeight)
            T_Phi_Max.grid(column = 3,row = 3)
            T_Phi_Max.insert("0.0", str(self.Phi_Max))
            self.DestroyArr.append(T_Phi_Max)
            #
            L_FillType=ctk.CTkLabel(self.window,text=f'FillType')
            L_FillType.grid(column = 0,row = 4)
            self.DestroyArr.append(L_FillType)
            Sourse_FillCombobox = ctk.CTkOptionMenu(master=self.window,
                                                         values=['N','linespace'],
                                         variable=self.Sourse_Fill,fg_color='silver',
                                                         text_color = 'teal',width=self.StandartWidth,
                                                         height=self.StandartHeight)
            Sourse_FillCombobox.grid(column = 1,row = 4)
            self.DestroyArr.append(Sourse_FillCombobox)
            # self.T_Sourse_Xs.place(relx=0.1,y = 0)
        elif value == 'Plane Wave':
            self.ClearWindow()
            pass
    def ClearWindow(self):
        for item in self.DestroyArr:
            try:
                item.destroy()
            except: print(item,'not destroyed')
class Epsilon():
    def __init__(self):
        self.a1 = 11
        self.a2 = 22
    def Eps1(self):
        print(self.a1)
    def Eps2(self):
        print(self.a2)
    func_list = [ Eps1,Eps2]
if __name__ == "__main__":
    page = Window()
    page.CreateMenu(page.CalculationType.get())
    func_list = Epsilon.func_list
    A = Epsilon()
    for item in func_list:
        item(A)
