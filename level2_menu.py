import pyworkexpand as pe
def level2():
    import tkinter as tk
    window=tk.Tk()
    window.title("学生信息管理系统")
    window.geometry("800x450")

    tk.Label(window,text="欢迎登录学生信息管理系统",bg="grey",font=("Ariaal",13),width=800,height=2).pack()
    tk.Button(window,text="成绩和信息录入",bg="grey",font=13,width=20,height=2,command=pe.impgad).place(x=305,y=60)
    tk.Button(window,text="查询个人成绩",bg="grey",font=13,width=20,height=2,command=pe.searchpergad).place(x=305,y=140)
    tk.Button(window,text="统计个人成绩",bg="grey",font=13,width=20,height=2,command=pe.stpergad).place(x=305,y=220)
    tk.Button(window,text="统计总评成绩",bg="grey",font=13,width=20,height=2,command=pe.stallgad).place(x=305,y=300)
    tk.Button(window,text="退出",bg="grey",font=13,width=20,height=2,command=exit).place(x=305,y=380)

    #window.mainloop()