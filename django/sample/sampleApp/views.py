from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import twstock
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import mplfinance as mpf
import plotly.graph_objects as go
import pandas as pd

# Create your views here.
def sayhello(request):
    return HttpResponse("Hello")
def templates(request):
    now = datetime.now()
    return render(request,"Hello.html",locals())
#即時查詢股票資訊
def stock_search(request):
    data = request.POST.get('stock_number')
    ts = twstock.realtime.get(data)
    #以下整理成json
    tsinfo = ts['info']
    stock_number = tsinfo['code']
    stock_name = tsinfo['name']
    stock_fullname = tsinfo['fullname']
    stock_time = tsinfo['time']
    tsrt = ts['realtime']
    stock_best_bid_price = tsrt['best_bid_price']
    stock_best_bid_volume = tsrt['best_bid_volume']
    stock_best_ask_price = tsrt['best_ask_price']
    stock_best_ask_volume = tsrt['best_ask_volume']
    stock_open = tsrt['open']
    stock_high = tsrt['high']
    stock_low = tsrt['low']

    return render(request, "chart.html", locals())#自填html檔名
#繪製開盤 收盤價曲線圖
def stock_pic(request):
    #改成自己的絕對路徑
    myfont = FontProperties(fname='D:/Github/041-Final-Project/django/sample/back_end/Futura.ttc', size=40)##改成Futura.ttc的絕對路徑
    month = []#X軸
    open = []#第一條線的資料
    close = []#第二條線的資料
    plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
    plt.plot(month,open,'s-',color = 'r', label="open")
    plt.plot(month,close,'o-',color = 'g', label="close")
    # 設定圖片標題，以及指定字型設定，x代表與圖案最左側的距離，y代表與圖片的距離
    plt.title("開盤 收盤價曲線圖", fontproperties=myfont, x=0.5, y=1.03)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel("month", fontsize=30, labelpad = 15)
    plt.ylabel("price", fontsize=30, labelpad = 20)
    plt.legend(loc = "best", fontsize=20)
    plt.show()
    return render(request, "???.html", locals())#自填html檔名


def Kline_pic(request):
    stock_no=''
    start_date=''
    end_date=''
    figure= go.Figure(
    data=[
        go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            increasing_line_color='red',
            decreasing_line_color='green'
            )
        ]
    )
    #figure.update_layout(xaxis_rangeslider_visible=False)
    figure.update_layout(
        title=stock_no,
        xaxis_title='Date',
        yaxis_title='Price',
    )

    #秀圖
    figure.show()
    return render(request, "???.html", locals())#自填html檔名