import tkinter as tk
from level2_menu import *
from pyworkexpand import *
from tkinter.constants import W
import tkinter.messagebox
import pickle
from tkinter.font import names
from typing import Sized, Text
from time import *


window=tk.Tk()

window.title("Student Information Management System")

window.geometry("800x450")
name=tk.StringVar()

stunum=tk.StringVar()

pwd=tk.StringVar()

#r=1
def check(s):
    b=str(s)
    #global r
    for i in b:
        if ord(i)<48 or (ord(i)>57 and ord(i)<65) or (ord(i)>90 and ord(i)<97) or ord(i)>122:
            #r=0
            #tk.messagebox.showerror(message="输入内容不符合要求！请重新输入")
            return 0
            #
    return 1
    #if r==1:
    #    pass


cnt=0
def login1():
    global cnt
    user_stunum=stunum.get()
    user_pwd=pwd.get()
    if check(user_pwd)== 0:
        tk.messagebox.showerror(message="The input content does not meet the requirements！Please re-enter.")
        pwd.set("")
        
    try:
        with open("new.txt","rb") as user_file:
            users_info = pickle.load(user_file)
    except FileNotFoundError:
        with open("new.txt","wb") as user_file:
            users_info={"admin":"admin"}
            pickle.dump(users_info,user_file)
            # pickle.dump('\r\n')
    if user_stunum in users_info:
        if user_pwd == users_info[user_stunum]:
            level2()#跳转到二级菜单
        else:
            if check(user_pwd)== 0:
                pass
            else:
                cnt+=1
                tk.messagebox.showwarning(message="You password is incorrect！You have only %d times。"%(3-cnt))
                pwd.set("")
                if cnt == 3:
                    tk.messagebox.showinfo(message="You havee entered the wrong password 3 times！Please try agian in five minutes.")
                    sleep(300)#锁定5min
                    cnt = 0
        
    else:
        is_sign_up=tk.messagebox.askyesno(message="You are not registered yet！Do you need to register?")
        if is_sign_up:
            zhuce()
def zhuce():

    def sign_up_in_system():
        ns=new_stunum.get()#获取被注册的学号
        np=new_pwd.get()#获取新注册账号的密码
        nf=new_pwd_confirm.get()#获取第二次输入的密码
        with open("new.txt","rb") as user_file:
            exist_user_info = pickle.load(user_file)
        if np!=nf:
            tk.messagebox.showerror(message="The password entered is inconsistent with the previous column.Please re-enter it.")
        elif ns in exist_user_info:
            tk.messagebox.showerror(message="The user has registered. Please do not register again.")
        else:
            exist_user_info[ns]= np
            with open("new.txt","wb") as user_file:
                pickle.dump(exist_user_info,user_file)
            tk.messagebox.showinfo(message="Welcome！You have regestered sucessfully!")
            window_sign_up.destroy()#关闭注册页面
            level2()
            
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry("350x200")
    window_sign_up.title("注册")

    new_stunum=tk.StringVar()
    new_stunum.set("2021xxxxxxxxx")
    tk.Label(window_sign_up,text="Student Number：").place(x=10,y=10)
    entry_new_stunum=tk.Entry(window_sign_up,textvariable=new_stunum)
    entry_new_stunum.place(x=150,y=10)

    new_pwd=tk.StringVar()
    tk.Label(window_sign_up,text="Password：").place(x=10,y=50)
    entry_new_pwd=tk.Entry(window_sign_up,textvariable=new_pwd,show="·")
    entry_new_pwd.place(x=150,y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up,text="Please enter you password again：").place(x=10,y=90)
    entry_pwd_confirm=tk.Entry(window_sign_up,textvariable=(new_pwd_confirm),show="·")
    entry_pwd_confirm.place(x=150,y=90)

    btu_comfirm_sign_up=tk.Button(window_sign_up,text="REGISTER",command=sign_up_in_system)
    btu_comfirm_sign_up.place(x=150,y=130)


def switch_to_Ch():
    window.destroy()
    import pythonworkCh

def login_window():

    l1=tk.Label(window,text="Wellcome to the student information management system",bg="grey",font=("Ariaal",13),width=800,height=2)
    l1.pack()

    l2=tk.Label(window,text="Please input you student number and password",bg="white",font=13,width=800,height=2)
    l2.pack()

    e1=tk.Label(window,text="Student Number：",font=15).place(x=195,y=98)
    e3=tk.Label(window,text="Password：",font=15).place(x=245,y=138)
    e2=tk.Entry(window,show=None,font=30,textvariable=stunum).place(x=325,y=98)
    e4=tk.Entry(window,show="·",font=30,textvariable=pwd)
    e4.place(x=325,y=138)

    b1=tk.Button(window,text="Login",bg="grey",font=13,width=20,height=2,command=login1)
    b1.place(x=205,y=210)

    b2=tk.Button(window,text="Register",bg="grey",font=13,width=20,height=2,command=zhuce)
    b2.place(x=405,y=210)

    b3=tk.Button(window,text="Exit",bg="grey",font=13,width=20,height=2,command=exit)
    b3.place(x=305,y=280)

    b4=tk.Button(window,text="Ch/En",bg="grey",font=13,width=10,height=1,command=switch_to_Ch)
    b4.place(x=5,y=7)
    
login_window()
window.mainloop()
