import tkinter as tk
from tkinter import Place, font
from tkinter.constants import BUTT
import csv

    
def commit():
    pass
def impgad():
    def clean():
        set("")
    window=tk.Tk()
    window.geometry("800x450")
    window.title("成绩录入")

    scrmath=tk.Variable()
    scrEgh=tk.Variable()
    scrch=tk.Variable()
    scrcmp=tk.Variable()
    scrpy=tk.Variable()

    gscrmath=scrmath.get()#获取数学成绩
    gscrEgh=scrEgh.get()#获取英语读写译成绩
    gscrch=scrch.get()#获取大学化学成绩
    gscrcmp=scrcmp.get()#获取大学计算机基础基础
    gscrpy=scrpy.get()#获取python程序设计成绩


    l1=tk.Label(window,text="请认真录入以下成绩",bg="grey",font=("Ariaal",13),width=800,height=2).pack()

    l2=tk.Label(window,text="高等数学：",font=20).place(x=100,y=80)
    e2=tk.Entry(window,font=30,textvariable=scrmath).place(x=200,y=83)

    l3=tk.Label(window,text="英语读写译：",font=20).place(x=84,y=130)
    e3=tk.Entry(window,font=30,textvariable=scrEgh).place(x=200,y=133)

    l4=tk.Label(window,text="大学化学：",font=20).place(x=100,y=180)
    e4=tk.Entry(window,font=30,textvariable=scrch).place(x=200,y=183)

    l5=tk.Label(window,text="大学计算机基础：",font=20).place(x=40,y=230)
    e5=tk.Entry(window,font=30,textvariable=scrcmp).place(x=200,y=233)

    l6=tk.Label(window,text="python程序设计：",font=20).place(x=40,y=280)
    e6=tk.Entry(window,font=30,textvariable=scrpy).place(x=200,y=283)

    b1=tk.Button(window,text="重置",bg="grey",font=13,width=10,height=1,command=clean).place(x=400,y=80)#重置高等数学成绩

    b2=tk.Button(window,text="重置",bg="grey",font=13,width=10,height=1,command=clean).place(x=400,y=130)#重置英语读写译成绩

    b3=tk.Button(window,text="重置",bg="grey",font=13,width=10,height=1,command=clean).place(x=400,y=180)#重置大学化学成绩

    b4=tk.Button(window,text="重置",bg="grey",font=13,width=10,height=1,command=clean).place(x=400,y=230)#重置大学计算机基础成绩

    b5=tk.Button(window,text="重置",bg="grey",font=13,width=10,height=1,command=clean).place(x=400,y=280)#重置python程序设计成绩

    b6=tk.Button(window,text="提交",font=13,width=20,height=2,command=commit)#commit函数为提交成绩到csv表格中的函数，皮昊旋不会写，在本文件4`5行定义了一个pass函数
    b6.place(x=200,y=383)

    b7=tk.Button(window,text="退出",font=13,width=20,height=2,command=exit).place(x=400,y=383)
    window.mainloop()

def searchpergad():
    def search():
        pass#用于导出指定学号对应的成绩(只需要各科成绩即可)
    window=tk.Tk()
    window.geometry("800x450")
    window.title("查询个人成绩")

    stunum=tk.Variable()

    l1=tk.Label(window,text="请输入您的学号用以查询各科成绩",bg="grey",font=("Ariaal",13),width=800,height=2).pack()

    l2=tk.Label(window,text="请输入学号：",font=20,width=20,height=2).place(x=100,y=80)
    e2=tk.Entry(window,font=30,textvariable=stunum).place(x=230,y=90)

    b1=tk.Button(window,text="查询",font=13,width=10,height=1,command=search).place(x=500,y=85)

    b2=tk.Button(window,text="退出",font=13,width=10,height=1,command=exit).place(x=350,y=383)


    window.mainloop()

def stpergad():
    def searchsum():
        pass#用于导出指定学号的成绩总和及平均分
    window=tk.Tk()
    window.geometry("800x450")
    window.title("统计个人成绩")

    stunum=tk.Variable()
    l1=tk.Label(window,text="请输入您的学号用以查询总分成绩及平均成绩",bg="grey",font=("Ariaal",13),width=800,height=2).pack()

    l2=tk.Label(window,text="请输入学号：",font=20,width=20,height=2).place(x=100,y=80)
    e2=tk.Entry(window,font=30,textvariable=stunum).place(x=230,y=90)

    b1=tk.Button(window,text="查询",font=13,width=10,height=1,command=searchsum).place(x=500,y=85)

    b2=tk.Button(window,text="退出",font=13,width=10,height=1,command=exit).place(x=350,y=383)

    window.mainloop()

def stallgad():
    def searchall():
        pass#用以导出指定学号对应的总评成绩
    window=tk.Tk()
    window.geometry("800x450")
    window.title("统计总评成绩")

    stunum=tk.Variable()
    l1=tk.Label(window,text="请输入您的学号用以查询总评成绩",bg="grey",font=("Ariaal",13),width=800,height=2).pack()

    l2=tk.Label(window,text="请输入学号：",font=20,width=20,height=2).place(x=100,y=80)
    e2=tk.Entry(window,font=30,textvariable=stunum).place(x=230,y=90)

    b1=tk.Button(window,text="查询",font=13,width=10,height=1,command=searchall).place(x=500,y=85)

    b2=tk.Button(window,text="退出",font=13,width=10,height=1,command=exit).place(x=350,y=383)

    window.mainloop()

# def clean(s):
#     s.set("")

