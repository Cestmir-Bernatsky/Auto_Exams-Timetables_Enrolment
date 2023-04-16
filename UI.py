import time
import datetime
import selenium
from tkinter import *
from selenium import webdriver
import zapis_fce
import sys



def save_info():
    name_info = name.get()
    pass_info = password.get()
    zapis_fce.sign_timetable(name_info, pass_info)
    print(name_info, pass_info)



def end_all():
    sys.exit()

screen = Tk()
screen.geometry("500x500")
screen.title("Zapis")
heading = Label(text = "ZUB", bg = "green", fg = "white", width = "500", height = "2")
heading.pack()


name_text = Label(text = "Přihlaš. údaje",)
password_text = Label(text = "Heslo",)
name_text.place(x= 15, y = 100)
password_text.place(x= 15, y = 200)

name = StringVar()
password = StringVar()

name_entry = Entry(textvariable = name)
password_entry = Entry(textvariable = password)

name_entry.place(x=15, y=125)
password_entry.place(x=15, y=225)




button_konec = Button(screen, text= 'Storno', bg='red', fg='white', width="250", height="2", command=end_all).pack(side=BOTTOM, pady=30)
button_zapis =  Button(screen, text="ZAPSAT", bg="green", width="250", height="2", command=save_info).pack(side=BOTTOM)
# button_zapis.place(x=0, y=275)
# button_konec.place(x=0, y=325)

screen.mainloop()















