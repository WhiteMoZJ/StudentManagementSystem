# from _typeshed import Self

import tkinter as tk

import tkinter.messagebox

import pickle

from tkinter.font import names

from typing import Text

window=tk.Tk()

window.title("学生信息管理系统")

window.geometry("800x450")
name=tk.StringVar()

stunum=tk.StringVar()

pwd=tk.StringVar()

def login():
    user_stunum=stunum.get()
    user_pwd=pwd.get()
    try:
        with open("users_info.pickle","rb") as user_file:
            users_info = pickle.load(user_file)
    except FileNotFoundError:
        with open("users_info.pickle","wb") as user_file:
            users_info={"admin":"admin"}
            pickle.dump(users_info,user_file)
    if user_stunum in users_info:
        if user_pwd == users_info[user_stunum]:
            tk.messagebox.showinfo(message="欢迎"+user_stunum)
        else:
            tk.messagebox.showerrror("密码输入错误！请重试。")
    else:
        is_sign_up=tk.messagebox.askyesno(message="您还未注册！")
        if is_sign_up:
            zhuce()

def zhuce(self):
    self.root.destroy()
    tk.RegisterPage()

l1=tk.Label(window,text="欢迎来到学生信息管理系统",bg="grey",font=("Ariaal",13),width=800,height=2)

l1.pack()

l2=tk.Label(window,text="请输入姓名，学号和密码",bg="white",font=13,width=800,height=2)

l2.pack()

e1=tk.Label(window,text="学号：",font=15).place(x=275,y=98)

e3=tk.Label(window,text="密码：",font=15).place(x=275,y=138)

e2=tk.Entry(window,show=None,font=30,textvariable=stunum).place(x=325,y=98)

e4=tk.Entry(window,show="·",font=30,textvariable=pwd).place(x=325,y=138)

b1=tk.Button(window,text="登录",bg="grey",font=13,width=20,height=2,command=login)
b1.place(x=205,y=210)

b2=tk.Button(window,text="注册",bg="grey",font=13,width=20,height=2,command=zhuce)
b2.place(x=405,y=210)

window.mainloop()
