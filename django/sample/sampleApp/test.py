from django.shortcuts import render
import twstock


def stock_realtime_search():
    # data = request.POST.get('stock_number')
    # print(data)
    ts = twstock.realtime.get('0050')
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
    # data = request.POST.get()

    return stock_number,stock_name,stock_fullname,stock_time,stock_best_bid_price,stock_best_bid_volume,stock_best_ask_price,stock_best_ask_volume
    # render(request, "test.html", locals())#自填html檔名

print(stock_realtime_search())
