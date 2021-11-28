import tkinter as tk
from tkinter.constants import W
import tkinter.messagebox
import pickle
from tkinter.font import names
from typing import Sized, Text
from time import *

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
                tk.messagebox.showerror(message="密码输入错误！请重试。")
                tk.messagebox.showinfo(message="您已输错密码3次，请于5分钟后再试！")
                sleep(300)
        
        else:
            is_sign_up=tk.messagebox.askyesno(message="您还未注册！是否需要注册？")
            if is_sign_up:
                zhuce()
def zhuce():

    def sign_up_in_system():
        ns=new_stunum.get()
        np=new_pwd.get()
        nf=new_pwd_confirm.get()
        with open("users_info.pickle","rb") as user_file:
            exist_user_info = pickle.load(user_file)
        if np!=nf:
            tk.messagebox.showerror(message="输入的密码与上一栏不一致，请重新输入。")
        elif ns in exist_user_info:
            tk.messagebox.showerror(message="该用户已注册，请勿重复注册。")
        else:
            exist_user_info[ns]= np
            with open("users_info.pickle","wb") as user_file:
                pickle.dump(exist_user_info,user_file)
            tk.messagebox.showinfo(message="欢迎，您已经成功注册！")
            window_sign_up.destroy()
            
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry("350x200")
    window_sign_up.title("注册")

    new_stunum=tk.StringVar()
    new_stunum.set("2021xxxxxxxxx")
    tk.Label(window_sign_up,text="用户名：").place(x=10,y=10)
    entry_new_stunum=tk.Entry(window_sign_up,textvariable=new_stunum)
    entry_new_stunum.place(x=150,y=10)

    new_pwd=tk.StringVar()
    tk.Label(window_sign_up,text="密码：").place(x=10,y=50)
    entry_new_pwd=tk.Entry(window_sign_up,textvariable=new_pwd,show="·")
    entry_new_pwd.place(x=150,y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up,text="请再次输入密码：").place(x=10,y=90)
    entry_pwd_confirm=tk.Entry(window_sign_up,textvariable=(new_pwd_confirm),show="·")
    entry_pwd_confirm.place(x=150,y=90)

    btu_comfirm_sign_up=tk.Button(window_sign_up,text="注册",command=sign_up_in_system)
    btu_comfirm_sign_up.place(x=150,y=130)



l1=tk.Label(window,text="欢迎来到学生信息管理系统",bg="grey",font=("Ariaal",13),width=800,height=2)

l1.pack()

l2=tk.Label(window,text="请输入学号和密码",bg="white",font=13,width=800,height=2)

l2.pack()

e1=tk.Label(window,text="学号：",font=15).place(x=275,y=98)

e3=tk.Label(window,text="密码：",font=15).place(x=275,y=138)

e2=tk.Entry(window,show=None,font=30,textvariable=stunum).place(x=325,y=98)

e4=tk.Entry(window,show="·",font=30,textvariable=pwd).place(x=325,y=138)

b1=tk.Button(window,text="登录",bg="grey",font=13,width=20,height=2,command=login)
b1.place(x=205,y=210)

b2=tk.Button(window,text="注册",bg="grey",font=13,width=20,height=2,command=zhuce)
b2.place(x=405,y=210)

b3=tk.Button(window,text="退出",bg="grey",font=13,width=20,height=2,command=exit)
b3.place(x=305,y=280)
window.mainloop()
