from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import twstock

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
    return render(request, "hellotemplates.html", locals())