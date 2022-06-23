import twstock
import pandas as pd

def csv_make2021(target_price,i,j):
    df = pd.DataFrame(columns=name_attribute, data=target_price)
    filename = f'D:/Github/041-Final-Project/django/sample/back_end/2303/'+all[j]+' 2021 '+str(i)+'月.csv'
    df.to_csv(filename)
    
def csv_make2022(target_price,i,j):
    df = pd.DataFrame(columns=name_attribute, data=target_price)
    filename = f'D:/Github/041-Final-Project/django/sample/back_end/2303/'+all[j]+' 2022 '+str(i)+'月.csv'
    df.to_csv(filename)

def all_stock(target,j):
    for i in range(6,13):
        target_price = target.fetch(2021, i)
        csv_make2021(target_price,i,j)
        print(i)
    for i in range(1,7):
        target_price = target.fetch(2022, i)
        csv_make2022(target_price,i,j)
        print(i)

all=["0050","2330","2884","1101","1102","2002","2412","2303","5880","2892"]

name_attribute = [
        'Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change',
        'Transcation'
        ]

for i in range(0,10):
    target = twstock.Stock(all[i])
    all_stock(target,i)



