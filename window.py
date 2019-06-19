from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

'''
def open_img():
    #x = openfn()
  #  print(x)
    x ="IgQJzyDOdpU.jpg"
    img = Image.open(x)
   # img = img.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root1,image=img)
    panel.image = img
    panel.place(x=10,y =10)
def printtext():
    sex_checkbutton.destroy()
    male_checkbutton.destroy()
    female_checkbutton.destroy()
    bd1.destroy()
    bd2.destroy()
    phone_radio1.destroy()
    phone_radio2.destroy()
    input_ID.destroy()
    pointPhone.destroy()
    pointBD.destroy()
    pointGroupID.destroy()
    pointBook.destroy()
    book1.destroy()
    book2.destroy()
    input_Nums.destroy()
    input_num.destroy()
    import botv0
    botv0.ReturnUserInfo([groupID.get(),numposts.get(),needsex.get(),BDate.get(),needPhone.get(),openBook.get()])
'''
class Window:
    def __init__(self):
        #todo:количество обрабатываемых постов расширить для >100
        #todo:добавить минимальный, максимальный возраст
        global needsex#1 - пацан, 0 - тёлка, 2 - не ебёт
        global groupID
        global BDate# 0 - полная дата, 1 - не ебёт
        global needPhone # 0 - не ебёт, 1 - обязательно
        global openBook
        global numposts
        root1 = Toplevel()
        root1.geometry("600x350")
        '''rudioButton'''
        needsex = IntVar()
        male_checkbutton = Radiobutton(root1,text="нужен пацан", value=1, variable=needsex, padx=15, pady=10)
        male_checkbutton.place(x = 330,y= 210)
        male_checkbutton.configure(state = DISABLED)

        female_checkbutton = Radiobutton(root1,text="нужна девушка", value=0, variable=needsex, padx=15, pady=10)
        female_checkbutton.place(x= 330, y = 240)
        female_checkbutton.configure(state = DISABLED)

        sex_checkbutton = Radiobutton(root1,text="не важно", value=2, variable=needsex, padx=15, pady=10)
        sex_checkbutton.place(x= 330, y = 270)
        sex_checkbutton.configure(state = DISABLED)

        BDate = IntVar()
        bd1 = Radiobutton(root1,text="ДА", value=0, variable=BDate, padx=15, pady=10)
        bd1.place(x= 140, y = 100 )

        bd2 = Radiobutton(root1,text="не важно", value=1, variable=BDate, padx=15, pady=10)
        bd2.place(x= 140, y = 130 )

        needPhone = IntVar()
        phone_radio1 = Radiobutton(root1,text="ДА", value=1, variable= needPhone, padx=15, pady=10)
        phone_radio1.place(x=140, y=170)
        phone_radio1.configure(state = DISABLED)
        phone_radio2 = Radiobutton(root1,text="не важно", value=0, variable= needPhone, padx=15, pady=10)
        phone_radio2.place(x=140, y=200)
        phone_radio2.configure(state=DISABLED)

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
        input_ID.insert(0,"-64529860")

        numposts = StringVar()
        input_num = Entry(root1,width = 10, textvariable = numposts)
        input_num.place(x=350,y = 40)
        input_num.insert(0,"100")
        '''Label'''
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
        btn = Button(root1, text='Начать поиск').place(x=600,y=150)

def Creator():
    app = Window()
