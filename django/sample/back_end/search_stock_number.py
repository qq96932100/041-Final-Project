from re import X
import sqlite3
import pandas as pd
import twstock

stock_number = ['0050','2330','2884','1101','1102','2002','2412','2823','5880','2892']

def search_stock(input_num): 
    for i in range (0, len(stock_number)):
        if(input_num == stock_number[i]):
            conn = sqlite3.connect('D:/041final_project/041-Final-Project/django/sample/back_end/all_stockDB/stock_'+input_num+'.db')
            # 讀取資料庫中的資料 pd.read_sql("SELECT*FROM table_name /WHERE label='someone_label_name'(非必要)/", 連結資料庫參數(conn))
            df = pd.read_sql('SELECT Date FROM stock_'+input_num+' WHERE Date = \'2021-06\'', conn)
            print(df)
            break
        
def realtime_stock(input_num): 
    realtime_info = twstock.realtime.get(input_num)
    print(realtime_info)
    return realtime_info

input_number = str(input("Enter a stock number:"))
search_stock(input_number)


            
