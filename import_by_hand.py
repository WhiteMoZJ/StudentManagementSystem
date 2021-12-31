import pandas as pd
import math as m
def ibh(a,b,c,d,e,f,g):
    gscrmath = a # 获取数学成绩
    gscrEgh = b# 获取英语读写译成绩
    gscrch = c  # 获取大学化学成绩
    gscrcmp = d  # 获取大学计算机基础基础
    gscrpy = e  # 获取python程序设计成绩
    gsn = f  # 获取学生姓名   snn=student name
    gspn = g  # 获取学生电话号码  spn=student phone number
    total_score = int(gscrmath)+int(gscrEgh)+int(gscrch)+int(gscrcmp)+int(gscrpy)

    list1 = [gsn, gspn, gscrmath, gscrEgh, gscrch, gscrcmp, gscrpy, str(total_score)]

    df=pd.DataFrame([list1])
    df.to_csv("main_list.csv",mode='a',header=False,index=False)