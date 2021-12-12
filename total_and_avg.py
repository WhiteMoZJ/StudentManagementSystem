stunum = input('学生学号:')
math = float(input('高等数学:'))
Egh = float(input('英语读写译:'))
ch = float(input('大学化学:'))
com = float(input('大学计算机基础:'))
py = float(input('python程序设计:'))
#总成绩
SumScore = math + Egh + ch + com + py
#平均成绩
AvgScore = SumScore / 5
print(SumScore)
print(AvgScore)