from pyworkexpand import *
def level2():
    import tkinter as tk
    window=tk.Tk()

    window.title("学生信息管理系统")

    window.geometry("800x450")


    l1=tk.Label(window,text="欢迎登录学生信息管理系统",bg="grey",font=("Ariaal",13),width=800,height=2)
    l1.pack()

    b1=tk.Button(window,text="成绩录入",bg="grey",font=13,width=20,height=2,command=impgad)
    b1.place(x=305,y=60)

    b2=tk.Button(window,text="查询个人成绩",bg="grey",font=13,width=20,height=2,command=searchpergad)
    b2.place(x=305,y=140)

    b3=tk.Button(window,text="统计个人成绩",bg="grey",font=13,width=20,height=2,command=stpergad)
    b3.place(x=305,y=220)

    b4=tk.Button(window,text="统计总评成绩",bg="grey",font=13,width=20,height=2,command=stallgad)
    b4.place(x=305,y=300)

    b5=tk.Button(window,text="退出",bg="grey",font=13,width=20,height=2,command=exit)
    b5.place(x=305,y=380)

    window.mainloop()