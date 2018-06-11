#!/usr/bin/env python3

from xls import Xlsx
from sql import ODBCQuery

#xls = Xlsx('SPC_test')
odbc = ODBCQuery('192.168.110.26')

today_data  = odbc.today_registers('P07')
print(today_data)

#xls.write_data()
#xls.close()