from curses.ascii import SP
import os
from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent

conn =sqlite3.connect(os.path.join(BASE_DIR,'db.sqlite3'))
cur = conn.cursor()

sName = input("Name: ")
sSex = input("Sex: ")
sPhone = input("Phone: ")

sql_str = "INSERT INTO sampleApp_sample(sName,sSex,sPhone) values('{}','{}','{}')".format(sName,sSex,sPhone)
cur.execute(sql_str)

conn.commit()