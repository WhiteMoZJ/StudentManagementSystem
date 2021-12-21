import tkinter as tk
from level2_menu import *
from pyworkexpand import *
from tkinter.constants import W
import tkinter.messagebox
import pickle
from tkinter.font import names
from typing import Sized, Text
import cv2 as cv
from PWDEncryption import *

window=tk.Tk()
window.title("Student Information Management System")
window.geometry("800x450")
name=tk.StringVar()
stunum=tk.StringVar()
pwd=tk.StringVar()

#Password string check
def check(s):
    b=str(s)
    #global r
    for i in b:
        if ord(i)<48 or (ord(i)>57 and ord(i)<65) or (ord(i)>90 and ord(i)<97) or ord(i)>122:
            return 0
    return 1

#Login in
cnt=0
def login1():
    global cnt
    user_stunum=stunum.get()
    user_pwd=pwd.get()
    if check(user_pwd)== 0:
        tk.messagebox.showerror(message="The input content does not meet the requirements！Please re-enter.")
        pwd.set("")      
    try:
        with open("account.pkl","rb") as user_file:
            users_info = pickle.load(user_file)
    except FileNotFoundError:
        with open("account.pkl","wb") as user_file:
            users_info={"admin":"admin"}
            pickle.dump(users_info,user_file)
    if user_stunum in users_info:
        #Decrypt pwd
        key=list(users_info.keys())[list(users_info.values()).index(users_info[user_stunum])]
        user_pwd_dec=mrsa.Decrypt(users_info[user_stunum],key)

        if user_pwd.encode('utf-8') == user_pwd_dec:
            window.destroy()
            level2()#Turn to the secondary menu
        else:
            if check(user_pwd)== 0:
                pass
            else:
                cnt+=1
                tk.messagebox.showinfo(message="You password is incorrect！You have only %d times。"%(3-cnt))
                pwd.set("")
                if cnt == 3:
                    tk.messagebox.showwarning(message="You havee entered the wrong password 3 times！Please try agian in 3 minutes.")
                    cv.waitKey(180000)#Locked for 3min
                    #Flashback BUG
                    cnt = 0
    else:
        is_sign_up=tk.messagebox.askyesno(message="You are not registered yet！Do you need to register?")
        if is_sign_up:
            zhuce()

#Sign-up menu
def zhuce():
    def sign_up_in_system():
        ns=new_stunum.get()#Get stunum that has been signed up
        np=new_pwd.get()#Get pwd of new-sign-up account
        nf=new_pwd_confirm.get()#Get pwd second inputted
        
        with open("account.pkl","rb") as user_file:
            exist_user_info = pickle.load(user_file)
        if np!=nf:
            tk.messagebox.showerror(message="The password entered is inconsistent with the previous column.Please re-enter it.",parent=window_sign_up)
        if np=='' or nf=='':
            tk.messagebox.showerror(message="Please enter password",parent=window_sign_up)
        elif ns in exist_user_info:
            tk.messagebox.showerror(message="The user has registered. Please do not register again.",parent=window_sign_up)
        else:
            #Encrypt pwd
            mrsa.Create_rsa_key(str(ns))           
            np_enc=mrsa.Encrypt(np)
            
            exist_user_info[ns]= np_enc
            with open("account.pkl","wb") as user_file:
                pickle.dump(exist_user_info,user_file)
            tk.messagebox.showinfo(message="Welcome！You have regestered successfully!")
            window_sign_up.destroy()#Shut down sign-up menu
            window.destroy()
            level2()#Open the secondary menu
            
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry("350x200")
    window_sign_up.title("SignUp")

    new_stunum=tk.StringVar()
    new_stunum.set("2021xxxxxxxxx")
    tk.Label(window_sign_up,text="Student Number：",font=('Arial',9,'bold')).place(x=10,y=10)
    entry_new_stunum=tk.Entry(window_sign_up,textvariable=new_stunum)
    entry_new_stunum.place(x=150,y=10)

    new_pwd=tk.StringVar()
    tk.Label(window_sign_up,text="Password：",font=('Arial',9,'bold')).place(x=10,y=50)
    entry_new_pwd=tk.Entry(window_sign_up,textvariable=new_pwd,show="·")
    entry_new_pwd.place(x=150,y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up,text="Enter password again：",font=('Arial',9,'bold')).place(x=10,y=90)
    entry_pwd_confirm=tk.Entry(window_sign_up,textvariable=(new_pwd_confirm),show="·")
    entry_pwd_confirm.place(x=150,y=90)

    btu_comfirm_sign_up=tk.Button(window_sign_up,text="REGISTER",font=('Arial',13,'bold'),command=sign_up_in_system)
    btu_comfirm_sign_up.place(x=150,y=130)

#Switch EN to CN
def switch_to_Ch():
    window.destroy()
    from pythonworkCh import login_window_CN
    login_window_CN()

#Log-in menu
def login_window_EN():
    l1=tk.Label(window,text="Wellcome to the student information management system",bg="grey",font=('Arial',15,'bold'),width=800,height=2)
    l1.pack()

    l2=tk.Label(window,text="Please input you student number and password",bg="white",font=('Arial',13,'bold'),width=800,height=2)
    l2.pack()

    e1=tk.Label(window,text="Student Number：",font=('Arial',15,'bold')).place(x=150,y=102)
    e3=tk.Label(window,text="Password：",font=('Arial',15,'bold')).place(x=210,y=136)
    e2=tk.Entry(window,show=None,font=30,textvariable=stunum).place(x=325,y=105)
    e4=tk.Entry(window,show="·",font=30,textvariable=pwd)
    e4.place(x=325,y=138)

    b1=tk.Button(window,text="LOG IN",bg="grey",font=('Arial',13,'bold'),width=15,height=2,command=login1)
    b1.place(x=210,y=210)

    b2=tk.Button(window,text="REGISTER",bg="grey",font=('Arial',13,'bold'),width=15,height=2,command=zhuce)
    b2.place(x=430,y=210)

    b3=tk.Button(window,text="Exit",bg="grey",font=('Arial',13,'bold'),width=20,height=2,command=exit)
    b3.place(x=300,y=280)

    b4=tk.Button(window,text="Ch/En",bg="grey",font=('Arial',13,'bold'),width=10,height=1,command=switch_to_Ch)
    b4.place(x=5,y=7)
    
login_window_EN()
window.mainloop()
