import tkinter as tk
from level2_menu import *
from pyworkexpand import *
from tkinter.constants import W
import tkinter.messagebox
import pickle
from tkinter.font import names
from typing import Sized, Text
from time import *
from PWDEncryption import *

window=tk.Tk()
window.title("学生信息管理系统")
window.geometry("800x450")
name=tk.StringVar()
stunum=tk.StringVar()
pwd=tk.StringVar()



#登录
cnt=0#创建计录输入错误密码次数的变量
def login():
    global cnt
    user_stunum=stunum.get()
    user_pwd=pwd.get()
    #检查学号是否符合要求
    if checkstunum(user_stunum) == 0 and user_stunum != "admin":
        tk.messagebox.showerror(message='请输入格式为2021XXYYY，其中XX从01到09，YYY从000到999的学号')
    else:
        #学号格式正确后执行检查该学号对应密码的格式
        if check(user_pwd)== 0:
            tk.messagebox.showerror(message="输入内容不符合要求！请重新输入")
            pwd.set("")           
        try:
            with open("account.pkl","rb") as user_file:
                users_info = pickle.load(user_file)
        except FileNotFoundError:
            with open("account.pkl","wb") as user_file:
                users_info={"admin":"admin"}
                pickle.dump(users_info,user_file)
                print(users_info)
        if user_stunum in users_info:
            if user_pwd == users_info[user_stunum]:
                if user_pwd == "admin":
                    window.destroy()
                    adpage()
                else:
                    window.destroy()
                    level2()#跳转到二级菜单
            else:
                if check(user_pwd)== 0:
                    pass
                else:
                    cnt+=1
                    tk.messagebox.showwarning(message="密码输入错误！还有%d次机会。"%(3-cnt))
                    pwd.set("")
                    if cnt == 3:
                        tk.messagebox.showinfo(message="您已输错密码3次，请于5分钟后再试！")
                        sleep(300)#锁定5min
                        cnt = 0       
        else:
            is_sign_up=tk.messagebox.askyesno(message="您还未注册！是否需要注册？")
            if is_sign_up:
                zhuce()

#注册菜单                        
def zhuce():
    def sign_up_in_system():
        ns=new_stunum.get()#获取被注册的学号
        np=new_pwd.get()#获取新注册账号的密码
        nf=new_pwd_confirm.get()#获取第二次输入的密码
        if checkstunum(ns) == 0:
            tk.messagebox.showerror(message='请输入格式为2021XXYYY，其中XX从01到09，YYY从000到999的学号',parent=window_sign_up)
        #检查学号是否符合要求
        else:
            with open("account.pkl","rb") as user_file:
                exist_user_info = pickle.load(user_file)
            if np!=nf:
                tk.messagebox.showerror(message="输入的密码与上一栏不一致，请重新输入。",parent=window_sign_up)
            elif ns in exist_user_info:
                #如果注册的用户名已经在表格中，则提示
                tk.messagebox.showerror(message="该用户已注册，请勿重复注册。",parent=window_sign_up)
            else:
                exist_user_info[ns]= np
                with open("account.pkl","wb") as user_file:
                    pickle.dump(exist_user_info,user_file)
                tk.messagebox.showinfo(message="欢迎,您已经成功注册！")
                window_sign_up.destroy()#关闭注册页面
                window.destroy()
                level2()#打开二级菜单
                
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry("350x200")
    window_sign_up.title("注册")
    
    #创建注册用户名提示及输入框
    new_stunum=tk.StringVar()
    new_stunum.set("2021xxxxxxxxx")
    tk.Label(window_sign_up,text="用户名：").place(x=10,y=10)
    entry_new_stunum=tk.Entry(window_sign_up,textvariable=new_stunum)
    entry_new_stunum.place(x=150,y=10)

#创建注册密码提示及输入框
    new_pwd=tk.StringVar()
    tk.Label(window_sign_up,text="密码：").place(x=10,y=50)
    entry_new_pwd=tk.Entry(window_sign_up,textvariable=new_pwd,show="·")
    entry_new_pwd.place(x=150,y=50)

#创建注册验证密码提示及输入框
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up,text="请再次输入密码：").place(x=10,y=90)
    entry_pwd_confirm=tk.Entry(window_sign_up,textvariable=(new_pwd_confirm),show="·")
    entry_pwd_confirm.place(x=150,y=90)
#创建注册按钮
    btu_comfirm_sign_up=tk.Button(window_sign_up,text="注册",command=sign_up_in_system)
    btu_comfirm_sign_up.place(x=150,y=130)

#中英文切换
def switch_to_En():
    window.destroy()
    from pythonworkEn import login_window_EN
    login_window_EN()

#登录菜单
def login_window_CN():
    l1=tk.Label(window,text="欢迎来到学生信息管理系统",bg="grey",font=('Arial',17,'bold'),width=800,height=2)
    l1.pack()

    l2=tk.Label(window,text="请输入学号和密码",bg="white",font=('Arial',13,'bold'),width=800,height=2)
    l2.pack()

    e1=tk.Label(window,text="学号：",font=('Arial',15,'bold')).place(x=265,y=105)
    e3=tk.Label(window,text="密码：",font=('Arial',15,'bold')).place(x=265,y=138)
    e2=tk.Entry(window,show=None,font=30,textvariable=stunum).place(x=325,y=108)
    e4=tk.Entry(window,show="·",font=30,textvariable=pwd)
    e4.place(x=325,y=140)

    b1=tk.Button(window,text="登录",bg="grey",font=('Arial',14,'bold'),width=15,height=2,command=login)
    b1.place(x=210,y=210)

    b2=tk.Button(window,text="注册",bg="grey",font=('Arial',14,'bold'),width=15,height=2,command=zhuce)
    b2.place(x=430,y=210)

    b3=tk.Button(window,text="退出",bg="grey",font=('Arial',14,'bold'),width=20,height=2,command=exit)
    b3.place(x=300,y=280)

    b4=tk.Button(window,text="Ch/En",bg="grey",font=('Arial',13,'bold'),width=10,height=1,command=switch_to_En)
    b4.place(x=5,y=7)

login_window_CN()
window.mainloop()
