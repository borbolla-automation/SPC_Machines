#######################################################################
#
# An example of creating an Excel chart in a chartsheet with Python
# and XlsxWriter.
#
# Copyright 2013-2018, John McNamara, jmcnamara@cpan.org
#
import xlsxwriter
import random
import datetime

class Xlsx(object):
	"""docstring for Xlsx"""
	def __init__(self, filename ):
		self.filename = filename
		#self.data = data
		self.workbook = xlsxwriter.Workbook(filename+'.xlsx')
		self.workbook.set_properties({
		    'title':    'SPC Machine data aquisition',
		    'subject':  '4G101',
		    'author':   'Luis Borbolla',
		    'manager':  'Luis Borbolla',
		    'company':  'Borbolla Automation',
		    'category': 'reporting and graph worksheets',
		    'keywords': 'kodaco SPC data aquisition',
		    'created':  datetime.date(2018, 6, 11),
		    'comments': 'created specifically for MKDC company '})
		self.worksheet = self.workbook.add_worksheet('Data_DP1')

		self.chartsheet = self.workbook.add_chartsheet()
		self.bold = self.workbook.add_format({'bold': 1})
		self.headings = ['SEQ_NUM','GAUGE_ID','GAUGE_NAME','BASICVALUE','VALUE','RANGE_UP','RANGE_DOWN','REG_DATE_TIME','RESULT']
		self.worksheet.write_row('A1', self.headings, self.bold)
		for column in range(len(self.headings)):
			self.worksheet.set_column(1, column, 17)


	def get_data(self , data):
		self.data = data

	def write_data(self , query):
		self.row_line = 1
		for row in query:
			self.worksheet.write_row(self.row_line , 0 , row)
			self.row_line +=1
		
	def chart(self):
		self.chart1 = workbook.add_chart({'type': 'line'})	
		self.chart1.add_series({
		    'name':       '=Data_DP1!$B$1',
		    #'categories': '=Data_DP1!$A$2:$A$7',
		    'values':     '=Data_DP1!B2:B1048576',
		})

		self.chart1.add_series({
		    'name':       '=Data_DP1!$D$1',
		    #'categories': '=Data_DP1!$A$2:$A$7',
		    'values':     '=Data_DP1!$D$2:$D$1048576',
		    'line': {
		            'color': 'red',
		            'width': 2,
		            'dash_type': 'long_dash',
		        },
		})


		# Configure a second series. Note use of alternative syntax to define ranges.
		self.chart1.add_series({
		    'name':       ['Data_DP1', 0, 2],
		    'categories': ['Data_DP1', 1, 0, 6, 0],
		    'values':     ['Data_DP1', 1, 2, 6, 1048576],
		})

		# Add a chart title and some axis labels.
		self.chart1.set_title ({'name': 'Results of sample analysis for DP1'})
		self.chart1.set_x_axis({'name': 'Test number'})
		self.chart1.set_y_axis({'name': 'Sample length (mm)'})

		# Set an Excel chart style.
		self.chart1.set_style(11)

		# Add the chart to the chartsheet.
		self.chartsheet.set_chart(chart1)

	def date_separator(self , date , time):
		year  = date[0:4]
		month = date[4:6]
		day   = date[6:]

		hour   = time[0:2]
		minute = time[2:4]
		second = time[4:]

		date_time = datetime.datetime(year = int(year) , month = int(month) , day = int(day) , hour = int(hour) , minute = int(minute) , second = int(second))

		return date_time

	def query_modificator(self , query ):
		matrix = []
		for line in query:
			list_line = list(line)
			date_time = self.date_separator(list_line[7],list_line[8])
			list_line.pop(7)
			list_line.pop(7)
			list_line.insert(7,date_time)
			matrix.append(list_line)

		return matrix	

	def close(self):
	    self.workbook.close()
		

if __name__ == '__main__':
	xls = Xlsx('test')
	data = [
	[1,2,3,4,5,6,7,8,9,0],
	[11,12,13,14,15,16,17,18,19,20],
	[1,2,3,4,5,6,7,8,9,0,],
	[11,12,13,14,15,16,17,18,19,20],

	]

	xls.write_data(data)
	xls.close()



# Create a new bar chart.


# Configure the first series.
		

