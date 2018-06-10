#!usr/bin/env python3
import datetime
import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
		'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('SPCMachines-47b188100dd5.json' , scope)
client = gspread.authorize(creds)
print(client)

workbook = client.open_by_key('1o66bESi_ln3BL4RIHkROiljuELhL6HRdLfqIhCxXOsU')

sheet = workbook.get_worksheet(9)





con = pyodbc.connect('DRIVER=FreeTDS;SERVER=192.168.110.26;PORT=1433;DATABASE=GMSDB;UID=gas;PWD=gas;TDS_Version=7.0;')
cursor = con.cursor()
today_str = '%s'%(str(datetime.datetime.now().year)+str("%02d"%(datetime.datetime.now().month,))+str("%02d"%(datetime.datetime.now().day),))

cursor.execute("SELECT SeqNum , GaugeID , GaugeName , BasicValue , Value , RangeUp , RangeDown , RegDate , RegTime , result FROM T1GaugeData WHERE GaugeID = 'P07' AND RegDate = %s"%(today_str))

row = cursor.fetchall()

cursor.execute("SELECT TOP 1 SeqNum , RegDate  FROM T1GaugeData WHERE regDate = %s ORDER BY SeqNum Desc"%(today_str))

max_today = cursor.fetchone()
max_today = int(max_today[0])


cursor.execute("SELECT TOP 1 SeqNum , RegDate  FROM T1GaugeData WHERE GaugeID = 'P07' ORDER BY SeqNum Desc")

max_total =  cursor.fetchone()
max_total = int(max_total[0])
print(today_str)
print(max_today,max_total)

i = 1
j = 0
for data in row:
	for cell in data:
		sheet.update_cell(i,j,str(cell))
		j+=1
	i+=1	

records = sheet.get_all_records()

print(records)