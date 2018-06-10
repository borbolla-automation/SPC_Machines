#!usr/bin/env python3
import datetime
import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

con = pyodbc.connect('DRIVER=FreeTDS;SERVER=192.168.110.26;PORT=1433;DATABASE=GMSDB;UID=gas;PWD=gas;TDS_Version=7.0;')
cursor = con.cursor()
today_str = '%s'%(str(datetime.datetime.now().year)+str("%02d"%(datetime.datetime.now().month,))+str("%02d"%(datetime.datetime.now().day),))

cursor.execute("SELECT SeqNum , GaugeID , GaugeName , BasicValue , Value , RangeUp , RangeDown , RegDate , RegTime FROM T1GaugeData WHERE GaugeID = 'P07' AND RegDate = %s"%(today_str))

row = cursor.fetchall()

cursor.execute("SELECT TOP 1 SeqNum , RegDate  FROM T1GaugeData WHERE GaugeID = 'P07' AND regDate = %s ORDER BY SeqNum Desc"%(today_str))

max_today = cursor.fetchone()

cursor.execute("SELECT TOP 1 SeqNum , RegDate  FROM T1GaugeData WHERE GaugeID = 'P07' ORDER BY SeqNum Desc")

max_total =  cursor.fetchone()
print(today_str)
print(max_total,max_total)

"""for data in row:
	print(data)"""

