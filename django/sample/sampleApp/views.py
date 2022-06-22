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
import json
import os
import plotly.io as io



stock_number = ['0050','2330','2884','1101','1102','2002','2412','2303','5880','2892']

# Create your views here.
def index(request):
    return render(request,"index.html",locals())

#即時查詢股票資訊
def stock_realtime_search(request):
    data = request.GET.get('input')
    print(data)
    ts = twstock.realtime.get(data)
    print(ts)
    #以下整理成json
    tsinfo = ts['info']
    stock_number = tsinfo['code']
    stock_name = tsinfo['name']
    # print(stock_name)
    stock_fullname = tsinfo['fullname']
    stock_time = str(tsinfo['time'])
    stock_time = stock_time.split(" ")
    stock_time_day = stock_time[0]
    stock_time_clock = stock_time[1]
    tsrt = ts['realtime']
    stock_best_bid_price = tsrt['best_bid_price']
    stock_best_bid_volume = tsrt['best_bid_volume']
    stock_best_ask_price = tsrt['best_ask_price']
    stock_best_ask_volume = tsrt['best_ask_volume']
    stock_open = tsrt['open']
    stock_high = tsrt['high']
    stock_low = tsrt['low']
    # data = request.POST.get()

    return render(request,"index.html",locals())#自填html檔名

#繪製開盤收盤圖
def open_close_pic(input_num, begin_time, end_time):
    #從資料庫抓資料
    print("suscces")
    for i in range (0, len(stock_number)):
        if(input_num == stock_number[i]):
            print("found!",stock_number[i])
            # conn = sqlite3.connect('C:\041-Final-Project\django\sample\back_end\all_stockDB\stock_'+input_num+'.db')
            conn = sqlite3.connect('../sample/back_end/all_stockDB/stock_'+input_num+'.db')
            df = pd.read_sql('SELECT * FROM stock_'+input_num+' WHERE (Date >= \'{}-01\' AND Date < \'{}-01\')'
                .format(begin_time,end_time), conn)
            month = df['Date']#X軸
            open = df['Open']#第一條線的資料
            close = df['Close']#第二條線的資料
            print(month,open,close)
            plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
            plt.plot(month,open,'s-',color = 'r', label="open")
            plt.plot(month,close,'o-',color = 'g', label="close")
            fileTrend = '../sample/static/trend.jpg'
           
            if(os.path.isfile(fileTrend)):
                os.remove(fileTrend)
                print('exist')
            else:
                print('not exist')
            
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
            plt.savefig('../sample/static/trend.jpg')



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
            fileKline = '../sample/static/kline.jpg'
            print(os.path.isfile(fileKline))
            if(os.path.isfile(fileKline)):
                os.remove(fileKline)
                print('exist')
            else:
                print('not exist')
            figure.write_image("../sample/static/kline.jpg", width=1500, height=1000)
            # plt.savefig('../sample/static/kline.jpg')
            # figure.show()
    return 

def info(request):
    return render(request,"info.html",locals())

def about(request):
    return render(request,"about_us.html",locals())

def chart(request):
    input_num = request.GET.get('input_num')
    begin_date = request.GET.get('begin_date')
    end_date = request.GET.get('end_date')    
    if(type(input_num) != 'NoneType' and type(begin_date) != 'NoneType' and type(end_date) != 'NoneType'):
        print('input_num:', input_num, ', begin_date:', begin_date, ', end_date:', end_date)
        open_close_pic(input_num, begin_date, end_date)
    return render(request, "chart.html", locals())
