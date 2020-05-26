import pymysql
import time


conn = pymysql.connect(
    host = '3.133.100.99',
    user ='kang851216',
    passwd = 'rkdrudals1',
    db='RAWDATA',
    charset='utf8mb4',
)

try:
    cursor=conn.cursor()
    print(conn)
    #sql= """INSERT INTO groupinfo(group_name, owner_name, rep_name, contact) VALUES(%s,%s,%s,%s)"""
    #isql = """SELECT id FROM data ORDER BY id DESC LIMIT 1"""
    idsql = """UPDATE machineinfo SET  group_name = 'HK001' WHERE machineno = 'AEL-002'""" 
    #cursor.execute(isql)
    cursor.execute(idsql)
    #cursor.execute(sql, ("ZH001","ZAEL","ZAEL","8615663"))
    
    conn.commit()
finally:
    cursor.close()
    conn.close()
