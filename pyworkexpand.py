import tkinter as tk
from tkinter import Pack, Place, font, mainloop
from tkinter.constants import BUTT, W
import csv
from print_personal_information import *
import tkinter.messagebox
import re
from personal_sum_and_avg import *
from import_by_hand import *
from DataManage import *


def checkspn(s):
    key = s
    p1 = r"\b13\d{9}\b"
    pattern1 = re.compile(p1)
    c1 = pattern1.findall(key)
    if len(c1)==0:
        return 0

def impgad():    
    window=tk.Toplevel()
    window.geometry("800x450")
    window.title("成绩录入")

    scrmath=tk.Variable()
    scrEgh=tk.Variable()
    scrch=tk.Variable()
    scrcmp=tk.Variable()
    scrpy=tk.Variable()
    sn=tk.Variable()
    spn=tk.Variable()

    def commit():
        #提交录入信息之前先检查各类信息是否符合要求
        gsn=sn.get()#获取学生姓名   snn=student name
        gspn = spn.get()#获取学生电话号码  spn=student phone number
        gscrmath=scrmath.get()#获取数学成绩
        gscrEgh=scrEgh.get()#获取英语读写译成绩
        gscrch=scrch.get()#获取大学化学成绩
        gscrcmp=scrcmp.get()#获取大学计算机基础基础
        gscrpy=scrpy.get()#获取python程序设计成绩
        
        #以下代码没有任何作用 BUG
        if len(gspn) == 0 and len(gsn) == 0:
            tk.messagebox.showerror(message='请输入电话号码和姓名')
        elif len(gsn) == 0:
            tk.messagebox.showerror(message='请输入您的姓名')
        elif len(gspn) == 0:
            tk.messagebox.showerror(message='请输入您的电话号码')
        elif checkspn(gspn) == 0:
            tk.messagebox.showerror(message='请输入以13开头，一共有11位数的电话号码')
        else:
            for i in (gscrmath,gscrEgh,gscrch,gscrcmp,gscrpy):
                if checkgrade(i)==1:
                    #成绩输入不符合事实
                    tk.messagebox.showerror(message='不要胡乱输入成绩哟，小朋友。')
                else:
                    ibh(gscrmath,gscrEgh,gscrch,gscrcmp,gscrpy,gsn,gspn)
                    break
                    #手动导入成绩数据
#经测试 无法使用
    def clean1():
        scrmath.bind('<Button-1>',scrmath.set(""))

    def clean2():
        scrEgh.bind('<Button-1>',scrEgh.set(""))

    def clean3():
        scrch.bind('<Button-1>',scrch.set(""))

    def clean4():
        scrcmp.bind('<Button-1>',scrcmp.set(""))

    def clean5():
        scrpy.bind('<Button-1>',scrpy.set(""))
    def clean6():
        spn.bind('<Button-1>',spn.set(""))
        
    tk.Label(window,text="请认真录入以下成绩和信息",bg="grey",font=("华文行楷",13),width=800,height=2).pack()

    tk.Label(window,text="高等数学：",font=20).place(x=100,y=90)
    tk.Entry(window,font=30,textvariable=scrmath).place(x=200,y=93)
    tk.Button(window,text="重置",bg="grey",font=13,width=10,height=1).place(x=410,y=90).bind('<Button-1>',scrmath.set(""))#重置高等数学成绩

    tk.Label(window,text="英语读写译：",font=20).place(x=84,y=140)
    tk.Entry(window,font=30,textvariable=scrEgh).place(x=200,y=143)
    #tk.Button(window,text="重置",bg="grey",font=13,width=10,height=1,command=clean2).place(x=410,y=140)#重置英语读写译成绩

    tk.Label(window,text="大学化学：",font=20).place(x=100,y=190)
    tk.Entry(window,font=30,textvariable=scrch).place(x=200,y=193)
    tk.Button(window,text="重置",bg="grey",font=13,width=10,height=1).place(x=410,y=190).bind('<Button-1>',scrch.set(""))#重置大学化学成绩

    tk.Label(window,text="大学计算机基础：",font=20).place(x=40,y=240)
    tk.Entry(window,font=30,textvariable=scrcmp).place(x=200,y=243)
    #tk.Button(window,text="重置",bg="grey",font=13,width=10,height=1,command=clean4).place(x=410,y=240)#重置大学计算机基础成绩

    tk.Label(window,text="python程序设计：",font=20).place(x=40,y=290)
    tk.Entry(window,font=30,textvariable=scrpy).place(x=200,y=293)
    #tk.Button(window,text="重置",bg="grey",font=13,width=10,height=1,command=clean5).place(x=410,y=290)#重置python程序设计成绩

    tk.Label(window,text="姓名：",font=20).place(x=100,y=50)
    tk.Entry(window,font=30,textvariable=sn).place(x=150,y=50)

    tk.Label(window,text='电话号码:',font=20).place(x=350,y=50)
    tk.Entry(window,font=30,textvariable=spn).place(x=440,y=50)
    #tk.Button(window,text="重置",bg="grey",font=13,width=10,height=1,command=clean6).place(x=600,y=50)#重置电话号码
    
    b6=tk.Button(window,text="提交",font=13,width=20,height=2,command=commit).place(x=400,y=583)
  

#学生个人成绩（分科）
def searchpergad():
    def search():
        ppi(stunum.get())
    window=tk.Toplevel()
    window.geometry("800x450")
    window.title("查询个人成绩")

    stunum=tk.Variable()
    # gstunum = stunum.get()
    tk.Label(window,text="请输入您的学号用以查询各科成绩",bg="grey",font=("Ariaal",13),width=800,height=2).pack()
    tk.Label(window,text="请输入学号：",font=20,width=20,height=2).place(x=75,y=80)
    tk.Entry(window,font=30,textvariable=stunum).place(x=230,y=90)
    tk.Button(window,text="查询",font=13,width=10,height=1,command=search).place(x=500,y=85)

#学生个人成绩的总分和平均分
def stpergad():
    # gstunum = 0
    def searchsum():
        psaa(stunum.get())
    window=tk.Toplevel()
    window.geometry("800x450")
    window.title("统计个人成绩")

    stunum=tk.Variable()
    tk.Label(window,text="请输入您的学号用以查询总分成绩及平均成绩",bg="grey",font=("Ariaal",13),width=800,height=2).pack()
    tk.Label(window,text="请输入学号：",font=20,width=20,height=2).place(x=75,y=80)
    tk.Entry(window,font=30,textvariable=stunum).place(x=230,y=90)
    tk.Button(window,text="查询",font=13,width=10,height=1,command=searchsum).place(x=500,y=85)

#学生所有（总评）成绩
def stallgad():
    def searchall():
        ID = stunum.get()
        insert(ID)
    window=tk.Toplevel()
    window.geometry("800x450")
    window.title("统计总评成绩")

    stunum=tk.Variable()
    tk.Label(window,text="请输入您的学号用以查询总评成绩",bg="grey",font=("Ariaal",13),width=800,height=2).pack()

    tk.Label(window,text="请输入学号：",font=20,width=20,height=2).place(x=75,y=80)
    tk.Entry(window,font=30,textvariable=stunum).place(x=230,y=90)
    tk.Button(window,text="查询",font=13,width=10,height=1,command=searchall).place(x=500,y=85)

#管理员页面
def adpage():
    window = tk.Tk()
    window.geometry("800x450")
    window.title("管理员")
    stunum = tk.Variable()
  
    def adsearch():
        ID = stunum.get()
        insert(ID)
    def MainList():
        File_Read_Save()
       
    tk.Label(window,text="请输入您要查询的学生的学号",bg="white",font=("华文行楷",20)).pack()
    tk.Label(window,text="请输入学号：",font=20,width=20,height=2).place(x=75,y=80)
    tk.Entry(window,font=30,textvariable=stunum).place(x=325,y=60)
    tk.Button(window,text="查询个人成绩",font=13,width=15,height=1,command=adsearch).place(x=325,y=400)
    tk.Button(window,text="显示总成绩表",font=13,width=15,height=1,command=MainList).place(x=325,y=400)
    
#检查学号格式
def checkstunum(s):
    key = s
    p1 = r"\b20210[1-9]\d{3}\b"
    pattern1 = re.compile(p1)
    c1 = pattern1.findall(key)
    if len(c1)==0:
        return 0
        
#密码输入字符检查
def check(s):
    b=str(s)
    #global r
    for i in b:
        if ord(i)<48 or (ord(i)>57 and ord(i)<65) or (ord(i)>90 and ord(i)<97) or ord(i)>122:
            return 0
    return 1

def checkgrade(s):
    key = s
    p1 = r"\b\d|[1-9]\d|100\b"
    pattern1 = re.compile(p1)
    c1 = pattern1.findall(key)
    if len(c1) == 0:
        return 1
    else:
        return 0
