import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pandas as pd


def insert(ID):
    #插入数据
    def Search(data, ID):#根据学号查找和搜索信息
        """
        搜索信息
        """
        count = 0
        for item in data:
            if item[1] == int(ID):#找到与所输入的学号相同的学生信息并导出
                # if str(item[1]) == ID:

                # print("姓名      ID   高等数学     英语视听说  大学化学 大学计算机基础  Python程序设计")
                # print(item[0],'\t', item[1],'\t',item[2],'\t\t',
                #      item[3],'\t', item[4], '\t',item[5],'\t\t',item[6])
                count = 1
                lst=[]#接下来遍历这个二维列表查找信息
                for i in item[0:1]:
                    lst.append(str(i))
                for i in item[1:]:
                    lst.append(int(i))
                return lst
        if count == 0:
            messagebox.showinfo(message="您已输错密码3次，请于5分钟后再试！")
        

    # ID = input("请输入学号：")
    data = pd.read_csv('main_list.csv')#使用pandas读取csv文件
    df = data.values.tolist()#使用pandas读取csv文件
    item = [Search(df, ID)]
    return item

        # '''以下则为如何将信息用表格形式展现出来'''


def ppi(ID):
    win = tkinter.Toplevel()  # 窗口
    win.title('个人成绩')  # 标题
    win.geometry('1000x200')  # 大小以及位置

    tabel_frame = tkinter.Frame(win)
    tabel_frame.pack()

    xscroll = Scrollbar(tabel_frame, orient=HORIZONTAL)
    yscroll = Scrollbar(tabel_frame, orient=VERTICAL)

    columns = ['姓名', 'ID','电话号码','高等数学', '英语读写译', '大学化学', '大学计算机', 'Python程序设计','总分']
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

    item1 = insert(ID)
    for index, data in enumerate(item1):#利用enumerate函数同时获得索引和值
        table.insert('', END, values=data)  # 添加数据到末尾