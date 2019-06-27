from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from tkinter import messagebox as mb

import wind
global windowCreated
windowCreated = False
def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def Creator():
    def DestroyCaller():
        global windowCreated
        windowCreated = False
        root1.destroy()
    def Blocker():
        if(BDate.get() == 1):
            minAge_entry.configure(state = DISABLED)
            maxAge_entry.configure(state = DISABLED)
        else:
            minAge_entry.configure(state = NORMAL)
            maxAge_entry.configure(state = NORMAL)
    def SavingParams():
        if(( isint(groupID.get())) and(isint(numposts.get()))):
            if(int(numposts.get()) > 0):
                if(BDate.get() == 0):
                    if ( (isint(minAge.get())) and (isint(maxAge.get()))):
                       if not ( (int(minAge.get()) > 0) and (int(maxAge.get())) >0):
                            mb.showerror("Ошибка", "возраст > 0")
                            return 0
                    else:
                        mb.showerror("Ошибка", "некорректно указан возраст")
                        return 0
                wind.SearchingParams[3] = BDate.get()
                wind.SearchingParams[1] = numposts.get()
                wind.SearchingParams[0] = groupID.get()
                if (needsex.get() == 0):
                    wind.SearchingParams[2] = "female"
                if (needsex.get() == 1):
                    wind.SearchingParams[2] = "male"
                if(needsex.get() == 2):
                    wind.SearchingParams[2] = "none"
                if(needPhone.get() == 1):
                    wind.SearchingParams[6] = True
                else:
                    wind.SearchingParams[6] = False
                wind.SearchingParams[4] = minAge.get()
                wind.SearchingParams[5] = maxAge.get()
                DestroyCaller()
            else:
                mb.showerror("Ошибка", "количество постов > 0")
        else:
            mb.showerror("Ошибка", "Должно быть введено число")
    #todo:количество обрабатываемых постов расширить для >100, но вот так-то опдумал а надо ли
    global windowCreated
    if(windowCreated == False):
        windowCreated = True
    else:
        return 0
    root1 = Toplevel()
    root1.geometry("600x350")
    root1.protocol("WM_DELETE_WINDOW", DestroyCaller)#запретим пользователю создавать больше 1 окна настроек
    '''rudioButton'''
    needsex = IntVar()
    if(wind.SearchingParams[2] == "female"):
        needsex.set(0)
    if (wind.SearchingParams[2] == "male"):
        needsex.set(1)
    if(wind.SearchingParams[2] == "none"):
        needsex.set(2)
    male_checkbutton = Radiobutton(root1,text="нужен пацан", value=1, variable=needsex, padx=15, pady=10)
    male_checkbutton.place(x = 330,y= 210)

    female_checkbutton = Radiobutton(root1,text="нужна девушка", value=0, variable=needsex, padx=15, pady=10)
    female_checkbutton.place(x= 330, y = 240)

    sex_checkbutton = Radiobutton(root1,text="не важно", value=2, variable=needsex, padx=15, pady=10)
    sex_checkbutton.place(x= 330, y = 270)

    BDate = BooleanVar()
    if(wind.SearchingParams[3] == False):
        BDate.set(0)
    else:
        BDate.set(1)
    bd1 = Radiobutton(root1,text="ДА", value=0, variable=BDate, padx=15, pady=10)
    bd1.place(x= 140, y = 100 )
    bd1.configure(command = Blocker)

    bd2 = Radiobutton(root1,text="не важно", value=1, variable=BDate, padx=15, pady=10)
    bd2.place(x= 140, y = 130 )
    bd2.configure(command=Blocker)
    needPhone = IntVar()
    if(wind.SearchingParams[6] == False):
        needPhone.set(0)
    else:
        needPhone.set(1)
    phone_radio1 = Radiobutton(root1,text="ДА", value=1, variable= needPhone, padx=15, pady=10)
    phone_radio1.place(x=140, y=170)
    phone_radio2 = Radiobutton(root1,text="не важно", value=0, variable= needPhone, padx=15, pady=10)
    phone_radio2.place(x=140, y=200)

    openBook = IntVar()
    book1 = Radiobutton(root1,text="ДА", value=1, variable= openBook, padx=15, pady=10)
    book1.place(x=140, y=250)
    book1.configure(state = DISABLED)
    book2 = Radiobutton(root1,text="не важно", value=0, variable= openBook, padx=15, pady=10)
    book2.place(x=140, y=280)
    book2.configure(state = DISABLED)

    '''entry'''
    groupID = StringVar()
    input_ID = Entry(root1,width = 50, textvariable = groupID)
    input_ID.place(x=20,y = 40)
    input_ID.insert(0,str(wind.SearchingParams[0]))

    numposts = StringVar()
    input_num = Entry(root1,width = 10, textvariable = numposts)
    input_num.place(x=350,y = 40)
    input_num.insert(0,str(wind.SearchingParams[1]))

    minAge = StringVar()
    minAge_entry = Entry(root1, width=3, textvariable=minAge)
    minAge_entry.place(x=260, y=110)
    minAge_entry.insert(0, str(wind.SearchingParams[4]))

    maxAge = StringVar()
    maxAge_entry = Entry(root1, width=3, textvariable= maxAge)
    maxAge_entry.place(x=290, y=110)
    maxAge_entry.insert(0, str(wind.SearchingParams[5]))
    Blocker()
    '''Label'''
    tire = Label(root1, text="-")
    tire.place(x=280, y=110)

    pointGroupID = Label(root1,text = "ID группы:")
    pointGroupID.place(x=20,y=10)

    pointBD = Label(root1,text = "Известен возраст:")
    pointBD.place(x=10,y=120)

    pointPhone = Label(root1,text ="Указан телефон:")
    pointPhone.place(x=10,y=200)

    pointBook = Label(root1,text = "Открытая книга:")
    pointBook.place(x=10,y=280)

    input_Nums = Label(root1,text = "Постов обработать:")
    input_Nums.place(x=340,y=10)
    ''''''
    btn = Button(root1, text='Сохранить', command =SavingParams).place(x=500, y=150)