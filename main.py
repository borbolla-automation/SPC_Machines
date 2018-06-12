#!/usr/bin/env python3

from xls import Xlsx
from sql import ODBCQuery
from mail import SendMail

xls = Xlsx('SPC_test')
odbc = ODBCQuery('192.168.110.26')
smail = SendMail(['administracion@borbolla-automation.com' , 'ingenieria@borbolla-automation.com' , 'bhleenk@kodaco.co.kr'] , 'SPC_test.xlsx' , subject = 'Today SPC 4G101 DP1 REGISTERS' )
today_data  = odbc.today_registers('P07')
print(today_data)

today_data = xls.query_modificator(today_data)

xls.write_data(today_data)
xls.close()

smail.fast_send()