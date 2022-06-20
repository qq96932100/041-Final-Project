import twstock
ts = twstock.realtime.get('0050')
tsinfo = ts['info']
print(tsinfo)