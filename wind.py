from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

global collectedInfo
collectedInfo= []
global numUser
numUser = 0
def callback(url):
    import webbrowser
    webbrowser.open_new(url)
def DownloadJPG(imgURL):
    import requests
    img = imgURL
    p = requests.get(img)
    out = open("C:\\Users\\User\\PycharmProjects\\VKAGAIN\img.jpg", "wb")
    out.write(p.content)
    out.close()
    x= "img.jpg"
    img1 = Image.open(x)
    img1 = img1.resize((400, 400), Image.ANTIALIAS)
    global panel
    panel.destroy()
    img1 = ImageTk.PhotoImage(img1)
    panel = Label(image=img1)
    panel.image = img1
    panel.place(x=10, y=10)
    return 0
def ShowInfo():
    global link
    global labelName
    global post
    posttext = ''
    for i  in range(collectedInfo[numUser][2].__len__()):
        if (ord(collectedInfo[numUser][2][i]) in range(65536)):#🙏
            posttext+=collectedInfo[numUser][2][i]

    subStrOld = "\n"
    lenStrOld = len(subStrOld)
    while posttext.find(subStrOld) > 0:
        i = posttext.find(subStrOld)
        posttext = posttext[:i] +  posttext[i + lenStrOld:]
    for i in range(posttext.__len__()):
        if i % 45 == 0:
            posttext = posttext[:i] +"\n"+ posttext[i:]
    post.configure(text = posttext)
    DownloadJPG(collectedInfo[numUser][1][1])
    link.configure(text=collectedInfo[numUser][0])
    link.bind("<Button-1>", lambda e: callback(collectedInfo[numUser][0]))
    labelName.configure(text=collectedInfo[numUser][1][0] + "("+str(collectedInfo[numUser][3])+")")

def NEXT():
    global numUser
    global b0
    global curr
    b0.configure(state = NORMAL)
    numUser+=1
    curr.configure(text=str(numUser + 1) + "/" + collectedInfo[0][-1])
    ShowInfo()
    if(numUser+1 == collectedInfo.__len__()):
        global b1
        b1.configure(state=DISABLED)
def BACK():
    global curr
    global numUser
    global b1
    b1.configure(state=NORMAL)
    numUser -= 1
    curr.configure(text=str(numUser + 1) + "/" + collectedInfo[0][-1])
    ShowInfo()
    if (numUser == 0):
        global b0
        b0.configure(state=DISABLED)
def OnlineSearching():
    import botv0
    global collectedInfo
    global b1
    global b0
    global numUser
    global link
    global labelName
    global curr
    global sex
    b1.configure(state = DISABLED)
    if(sex == 0):
        collectedInfo = botv0.ReturnUserInfo("female")
    else:
        collectedInfo = botv0.ReturnUserInfo("male")
    if(collectedInfo != []):
        ShowInfo()
        b1.destroy()
        b1 = Button(text='Вперёд', command=NEXT)
        b1.place(x=500, y=10)
        b0 = Button(text='Назад', command=BACK)
        b0.place(x=440, y=10)
        b0.configure(state = DISABLED)
        curr.configure(text = str(numUser+1)+"/" +collectedInfo[0][-1])
        if(collectedInfo.__len__() == 1):
            b1.configure(state = DISABLED)

def OnlineSearching1():
    import threading
    t = threading.Thread(target=OnlineSearching)
    t.daemon = True
    t.start()
    return 0

global sex
sex = 0
def SwitchPhoto():
    global sex
    if(sex == 1):
        sex = 0
        x = "girl.jpg"
    else:
        sex = 1
        x = "man.jpg"
    img1 = Image.open(x)
    img1 = img1.resize((400, 400), Image.ANTIALIAS)
    global panel
    img1 = ImageTk.PhotoImage(img1)
    panel.configure(image=img1)
    panel.image = img1
    panel.place(x=10, y=10)
    return 0
def CreateWindow():
    root = Tk()
    root.geometry("800x500")
    root.resizable(width=True, height=True)

    '''запихиваем менюшку'''
    mainmenu = Menu()
    root.config(menu = mainmenu)
    import window
    mainmenu.add_command(label='Настройки', command = window.Creator)


    x = "girl.jpg"
    img = Image.open(x)
    img = img.resize((400, 400), Image.ANTIALIAS)
    global panel
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x=10, y=10)
    panel.bind("<Button-1>", lambda e: SwitchPhoto())
    global labelName
    labelName = Label(text="")
    labelName.place(x=440, y=40)

    global link
    link = Label(text="", fg="blue", cursor="hand2")
    link.place(x=440, y=70)
    global b1
    b1 = Button(root, text='Начать поиск',command = OnlineSearching1)#
    b1.place(x=440, y=10)
    global pointAllSearching
    pointAllSearching = Label(text="")
    pointAllSearching.place(x=10, y=450)
    global pointSearching
    pointSearching = Label(text="")
    pointSearching.place(x=10, y=480)

    global curr
    curr = Label(text = '')
    curr.place(x=10,y=420)

    global post
    post = Label(text ='')
    post.place(x=440,y=100)
    root.mainloop()

