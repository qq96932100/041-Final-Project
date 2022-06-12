from re import X
import sqlite3
import pandas as pd

stock_number = ['0050','2330','2884','1101','1102','2002','2412','2823','5880','2892']

def search_stock(x):
    for i in range (0,len(stock_number)):
        if(x == stock_number[i]):
            conn = sqlite3.connect('D:/041final_project/041-Final-Project/django/sample/back_end/all_stock_db/stock_'+x+'.db')
            # 透過SQL語法讀取資料庫中的資料 pd.read_sql("SELECT*FROM table_name /WHERE label='someone_label_name'(非必要)/", 連結資料庫參數(conn))
            df = pd.read_sql('SELECT * FROM stock_'+x, conn)
            print(df)
            break
            
input_number = str(input("Inter a stock number:"))
search_stock(input_number)
            
