#!usr/bin/env python3

"""
import pyodbc

conn = pyodbc.connect("Driver ={SQL Server};Server=192.168.110.23;database=GMSDB;uid=gas;pw=gas")

cur = conn.cursor("SELECT * FROM T1GaugeData")

for row in cur:
	for column in row:
	    print(column)

cur.close()
conn.close()
"""


import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
con = pyodbc.connect('DRIVER=FreeTDS;SERVER=192.168.110.26;PORT=1433;DATABASE=GMSDB;UID=gas;PWD=gas;TDS_Version=7.0;')
cursor = con.cursor()

cursor.execute('SELECT GaugeID , GaugeName , BasicValue , Value , RegDate , RegTime FROM T1Gaugedata')

row = cursor.fetchall()

for data in row:
	print(data)

