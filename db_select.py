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
    sql= """SELECT machineno, time, doorstat, hopperstat FROM data WHERE machineno = 'AEL-001'"""
    cursor.execute(sql)
    conn.commit()
    pymysql.store_result()
    pymysql.bind_result(ma, ti, do, ho)
    pymysql.fetch()
    t = pymysql.bind_result(ma, ti, do, ho)
    print(t)
finally:
    cursor.close()
    conn.close()

