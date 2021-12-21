import pandas as pd
data = pd.read_excel('new_text.xlsx','mt',index_col=0)
data.to_csv('data.csv',encoding='utf-8')