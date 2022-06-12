from django.test import TestCase
import sqlite3
import pandas as pd

# Create your tests here.

stock_number = ["0050","2330","2884","1101","1102","2002","2412","2823","5880","2892"]
for k in stock_number:
    conn = sqlite3.connect('stock_'+k+'.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE stock_%s(Date, Capacity, Turnover, Open, High, Low, Close, Change, Transcation)'%k)  #建立資料表
    conn.commit()
    # sqlite3.connect() 連結資料庫 
    # /.cursor()        建立資料庫指標 
    # /.execute()       建立資料庫的colume_label
    # /.commit()        確認完成
    for i in range(7,13):
        df = pd.read_csv('D:/041final_project/041-Final-Project/django/sample/back_end/0050/0050 2021 '+str(i)+'月'+'.csv', index_col=[0])
        # 寫入資料表 /.to_sql 關鍵參數為:資料表名字,連線參數,
        # 是否已存在,是否寫入pandas dataframe索引值
        df.to_sql('stock_'+k, conn, if_exists='append', index=False)
    for j in range(1,7):
        df = pd.read_csv('D:/041final_project/041-Final-Project/django/sample/back_end/0050/0050 2022 '+str(j)+'月'+'.csv', index_col=[0])
        df.to_sql('stock_'+k, conn, if_exists='append', index=False)



