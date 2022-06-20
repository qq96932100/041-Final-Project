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
import os 

stock_number = ['0050','2330','2884','1101','1102','2002','2412','2823','5880','2892']
def open_close_pic(input_num, begin_time, end_time):
    #從資料庫抓資料
    for i in range (0, len(stock_number)):
            if(input_num == stock_number[i]):
                # conn = sqlite3.connect('C:\041-Final-Project\django\sample\back_end\all_stockDB\stock_'+input_num+'.db')
                conn = sqlite3.connect('C:/041-Final-Project/django/sample/back_end/all_stockDB/stock_0050.db')
                df = pd.read_sql('SELECT * FROM stock_'+input_num+' WHERE (Date >= \'{}-01\' AND Date < \'{}-01\')'
                    .format(begin_time,end_time), conn)
    month = df['Date']#X軸
    open = df['Open']#第一條線的資料
    close = df['Close']#第二條線的資料
    plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
    plt.plot(month,open,'s-',color = 'r', label="open")
    plt.plot(month,close,'o-',color = 'g', label="close")
    # 設定圖片標題，以及指定字型設定，x代表與圖案最左側的距離，y代表與圖片的距離
    plt.title("open-close line pic", x=0.5, y=1.03)
    plt.xticks(fontsize=7)
    plt.xticks(rotation = 90)
    ax = plt.gca()
    ax.set_xticks(ax.get_xticks()[::3])
    plt.yticks(fontsize=10)
    plt.xlabel("month", fontsize=20, labelpad = 15)
    plt.ylabel("price", fontsize=20, labelpad = 20)
    plt.legend(loc = "best", fontsize=5)
    plt.show()
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
#自製資料
input_num = str(input("Enter a stock number:"))
begin_time = str(input("Enter begin time (e.g. 2021-06):"))
end_time = str(input("Enter end time (e.g. 2022-06):"))
open_close_pic(input_num, begin_time, end_time)
