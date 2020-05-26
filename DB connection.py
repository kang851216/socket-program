import sqlite3

conn = sqlite3.connect("http://3.133.100.99:8000/rawdata.db") 
cur = conn.cursor() 
cur.execute('SELECT * FROM RAWDATA') 
r = cur.fetchall() 

print(r[1][1]) 

cur.close() 
conn.close()


