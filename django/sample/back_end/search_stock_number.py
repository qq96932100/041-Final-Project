from re import X
import sqlite3
import pandas as pd
import twstock
import os

stock_number = ['0050','2330','2884','1101','1102','2002','2412','2823','5880','2892']

def search_stock(input_num, begin_time, end_time): 
    for i in range (0, len(stock_number)):
        if(input_num == stock_number[i]):
            conn = sqlite3.connect('C:\041-Final-Project\django\sample\back_end\all_stockDB\stock_'+input_num+'.db')
            df = pd.read_sql('SELECT * FROM stock_'+input_num+' WHERE (Date >= \'{}-01\' AND Date < \'{}-01\')'
                .format(begin_time,end_time), conn),
            print(df)
            return df
        
input_number = str(input("Enter a stock number:"))
begin_time = str(input("Enter begin time (e.g. 2021-06):"))
end_time = str(input("Enter end time (e.g. 2022-06):"))
search_stock(input_number, begin_time, end_time)         
        
def realtime_stock(input_num): 
    realtime_info = twstock.realtime.get(input_num)
    print(realtime_info)
    return realtime_info




            
