import pandas as pd

def Search(data, ID):
    count = 0
    for item in data:
        if item[1] == int(ID):
        #或者 if str(item[1]) == ID:
            print("姓名      ID   高等数学     英语视听说  大学化学 大学计算机基础  Python程序设计")
            print(item[0],'\t', item[1],'\t',item[2],'\t\t',
                  item[3],'\t', item[4], '\t',item[5],'\t\t',item[6])
            count = 1
            break
    if count == 0:
        print("没有该学号")

ID = input()
data=pd.read_csv('new_text.csv')
df=data.values.tolist()
Search(df,ID)