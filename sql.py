#!usr/bin/env python3
import datetime
import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

con = pyodbc.connect('DRIVER=FreeTDS;SERVER=192.168.110.26;PORT=1433;DATABASE=GMSDB;UID=gas;PWD=gas;TDS_Version=7.0;')
cursor = con.cursor()

cursor.execute("SELECT SeqNum , GaugeID , GaugeName , BasicValue , Value , RangeUp , RangeDown , RegDate , RegTime FROM T1GaugeData WHERE GaugeID = 'P07' AND RegDate = %s"%(str(datetime.datetime.now().year)+str("%02d"%(datetime.datetime.now().month,))+str("%02d"%(datetime.datetime.now().day),)))

row = cursor.fetchall()

for data in row:
	print(data)

