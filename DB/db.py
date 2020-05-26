import sqlite3
import time
import datetime
rawdata = ['AEL001', '1234567', 100.08]
date = datetime.datetime.now().strftime("%Y") + datetime.datetime.now().strftime("%m") + datetime.datetime.now().strftime("%d")
time = datetime.datetime.now().strftime("%H") + datetime.datetime.now().strftime("%M") + datetime.datetime.now().strftime("%S")

con = sqlite3.connect(".../DB/rawdata.db")
cursor = con.cursor()
#cursor.execute("Create Table RAWDATA(Date text, Time text, Machineno text, QRcode text, weight int)")
cursor.execute("INSERT INTO RAWDATA(Date, Time, Machineno, QRcode, weight) VALUES(?, ?, ?, ?, ?)", (date, time, rawdata[0], rawdata[1], rawdata[2]))
con.commit()
con.close()
