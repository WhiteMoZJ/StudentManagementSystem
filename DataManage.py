import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import tkinter.filedialog

def File_Read_Save():
    """
    主要是文件的读取与保存
    """
    def Read_Main_List():
        """
        导入一个主列表文件
        每次导入其他数据列表就写入进去
        每次关闭之后重新打开就是上次关闭之前的内容
        导出excel也可以直接将此文件转为excel即可
        """
        default = pd.read_csv('main_list.csv')
        info = default.values.tolist()
        for index, data in enumerate(info):
            table.insert('', END, values=data)

    def Insert():
        '''
        从文件夹导入csv或excel文件
        '''
        try:
            filename = tkinter.filedialog.askopenfilename(title='导入数据',
                                                          filetypes=[('CSV文件','*.csv'),('表格文件','*.xls *.xlsx')])
            #读取文件
            try:
                info_data = pd.read_csv(filename)#判断编码形式
            except[FileExistsError]:
                info_data = pd.read_excel(filename)
        except:
            tkinter.messagebox.showerror(message="用户未导入文件", parent=win)
        df = info_data.values.tolist()
        Manual_Import = pd.DataFrame(df)
        Manual_Import.to_csv('main_list.csv', mode='a', header=False, index=False)
        '''
        将二维列表中的信息提取出来后按照一定的顺序加入一个新的列表中
        '''
        personinfo=[] #个人信息
        info=[]#总体信息
        for i in df:
            for j in i:
                '''
                如果元素是数字类型，转为整数
                如果不是，保持原型
                '''
                try:
                    j=int(j)
                except:
                    j=j
                #将这一组的数据添加进新的列表
                personinfo.append(j)
            info.append(personinfo)
            personinfo=[]
        for index, data in enumerate(info):
            table.insert('', END, values=data)  # 添加数据到末尾

    def Save_To_File():
        '''
        将当前显示列表写入Excel文件
        直接写入
        '''
        data = pd.read_csv('main_list.csv')
        df = pd.DataFrame(data)
        file_path = tkinter.filedialog.asksaveasfilename(title='保存当前数据',initialfile='总成绩',
                                                        filetypes=[('表格文件', '*.xls *.xlsx')])
        file = tkinter.filedialog.asksaveasfile(filetypes = file_path, defaultextension = file_path) 
        
 
    '''
    def Calculation():
        """
        计算总分和平均分
        """
        data = pd.read_csv('main_list.csv')
        info = data.values.tolist()
        for i in info:
            if len(i) == 8:
                sum = 0
                #列表元素为8则此组数据没有总和
                for j in i[3:]:
                    sum += int(j)
                i.append[sum]
        avg_list = ['平均分','','']
        print(info.T)
        '''

    win = tkinter.Tk()  # 窗口
    win.title('学生成绩')  # 标题
    win.geometry("1000x600")

    tabel_frame = tkinter.Frame(win)
    tabel_frame.pack()

    xscroll = Scrollbar(tabel_frame, orient=HORIZONTAL)
    yscroll = Scrollbar(tabel_frame, orient=VERTICAL)

    columns = ['姓名', 'ID', '电话号码','高等数学', '英语读写译', '大学化学', '大学计算机', 'Python程序设计','总分']
    table = ttk.Treeview(
            master=tabel_frame,  # 父容器
            height=25,  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列
            xscrollcommand=xscroll.set,  # x轴滚动条
            yscrollcommand=yscroll.set,  # y轴滚动条
            )
    for column in columns:
        table.heading(column=column, text=column, anchor=CENTER,
                    command=lambda name=column:
                    messagebox.showinfo('', '这里是{}'.format(name)))  # 定义表头
        table.column(column=column, width=100, minwidth=100, anchor=CENTER, )  # 定义列
    xscroll.config(command=table.xview)
    xscroll.pack(side=BOTTOM, fill=X)
    yscroll.config(command=table.yview)
    yscroll.pack(side=RIGHT, fill=Y)
    table.pack(fill=BOTH, expand=True)

    Read_Main_List()
    btn_frame = Frame(win)
    btn_frame.pack()
    Button(btn_frame, text='导入数据', bg='grey', width=10, command=Insert).pack()
    Button(btn_frame, text='导出数据', bg='grey', width=10, command=Save_To_File).pack()
    #Button(btn_frame, text='计算数据', bg='grey', width=10, command=Calculation).pack()
    #Button(btn_frame, text='清除数据', bg='grey', width=10, command=).pack()
    Button(btn_frame,text="退出",bg='grey', width=10,command=exit).pack()