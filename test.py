import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pandas as pd

def insert():
    # 插入数据
    info_data=pd.read_csv('new_text.csv')
    info = info_data.values.tolist()

    print(info)
    for index, data in enumerate(info):
        table.insert('', END, values=data)  # 添加数据到末尾


if __name__ == '__main__':
    pass
    win = tkinter.Tk()  # 窗口
    win.title('郑一凡')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 1000
    height = 500
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

    tabel_frame = tkinter.Frame(win)
    tabel_frame.pack()

    xscroll = Scrollbar(tabel_frame, orient=HORIZONTAL)
    yscroll = Scrollbar(tabel_frame, orient=VERTICAL)

    columns = ['姓名', 'ID', '高等数学', '英语读写译', '大学化学', '大学计算机', 'Python程序设计','总分']
    table = ttk.Treeview(
            master=tabel_frame,  # 父容器
            height=10,  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列
            xscrollcommand=xscroll.set,  # x轴滚动条
            yscrollcommand=yscroll.set,  # y轴滚动条
            )
    for column in columns:
        table.heading(column=column, text=column, anchor=CENTER,
                      command=lambda name=column:
                      messagebox.showinfo('', '{}描述信息~~~'.format(name)))  # 定义表头
        table.column(column=column, width=100, minwidth=100, anchor=CENTER, )  # 定义列
    xscroll.config(command=table.xview)
    xscroll.pack(side=BOTTOM, fill=X)
    yscroll.config(command=table.yview)
    yscroll.pack(side=RIGHT, fill=Y)
    table.pack(fill=BOTH, expand=True)

    insert()
    btn_frame = Frame()
    btn_frame.pack()
    #Button(btn_frame, text='添加', bg='yellow', width=20, command=insert).pack()
    win.mainloop()