from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import twstock
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import mplfinance as mpf
import plotly.graph_objects as go
import pandas as pd
from re import X
import sqlite3
import pandas as pd

stock_number = ['0050','2330','2884','1101','1102','2002','2412','2823','5880','2892']

def Kline_pic(input_num, begin_time, end_time):
    #從資料庫抓資料
    for i in range (0, len(stock_number)):
        if(input_num == stock_number[i]):
            conn = sqlite3.connect('D:/Github/041-Final-Project/django/sample/back_end/all_stockDB/stock_'+input_num+'.db')
            df = pd.read_sql('SELECT * FROM stock_'+input_num+' WHERE (Date >= \'{}-01\' AND Date < \'{}-01\')'
                .format(begin_time,end_time), conn)
    #畫圖
    figure= go.Figure(
    data=[
        go.Candlestick(
            x=df['Date'],
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            increasing_line_color='red',
            decreasing_line_color='green'
            )
        ]
    )
    figure.update_layout(
        title=input_num,
        xaxis_title='Date',
        yaxis_title='Price',
    )
    figure.show()
#自製輸入
input_num = str(input("Enter a stock number:"))
begin_time = str(input("Enter begin time (e.g. 2021-06):"))
end_time = str(input("Enter end time (e.g. 2022-06):"))
Kline_pic(input_num, begin_time, end_time)