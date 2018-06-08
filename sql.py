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
server = '192.168.110.26' 
database = 'GMSDB' 
username = 'gas' 
password = 'gas' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

