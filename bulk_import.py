import openpyxl
import pandas as pd

data=pd.read_csv('new text.csv',header=None)
df=data.values.tolist()

def write_excel_data(value):
    workbook = openpyxl.Workbook()    # 新建一个工作簿
    sheet = workbook.active           # 获取当前活跃的表单
    sheet.title = "测试数据写入excel"   # 设置表单的名称
    '''方法1'''
    # for i in range(0, len(value)):
    #     for j in range(0, len(value[i])):
    #         sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]))
    #         # openpyxl 读写单元格时，单元格的坐标位置起始值是（1, 1），即下标最小值为1，否则报错！
    ''''方法2'''
    for i in value:
        sheet.append(i)
    workbook.save("text.xlsx")  # 保存工作簿

    print("写入数据成功！")
write_excel_data(df)