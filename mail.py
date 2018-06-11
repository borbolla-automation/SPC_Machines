
"""# smtplib module send mail

import smtplib

TO = 'administracion@borbolla-automation.com'
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'

# Gmail Sign In
gmail_sender = 'administracion@borbolla-automation.com'
gmail_passwd = 'borbollaSP123'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()
"""

#!/usr/bin/env python
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
import credentials

class SendMail(object):
	"""docstring for send"""
	def __init__(self, recipients , filename , subject = 'Message from KODACO server'):
		
		self.recipients = recipients
		self.filename = filename
		self.emaillist = [elem.strip().split(',') for elem in self.recipients]		
		self.subject = subject

		#recipients = ['administracion@borbolla-automation.com','ingenieria@borbolla-automation.com','ventas@borbolla-automation.com']

	def build_msg(self):
		
		self.msg = MIMEMultipart()
		self.msg['Subject'] = str(self.subject)
		self.msg['From'] = 'administracion@borbolla-automation.com'
		self.msg['Reply-to'] = 'ingenieria@borbolla-automation.com'
		 
		self.msg.preamble = 'Multipart massage.\n'
		 
		part = MIMEText("Hi, please find the attached file")
		self.msg.attach(part)
		try:
			part = MIMEApplication(open(str(self.filename),"rb").read()) 	
		except FileNotFoundError as e:
		 	print('File not valid') 
		
		part.add_header('Content-Disposition', 'attachment', filename=str(self.filename))
		self.msg.attach(part)

	def server_connect(self):
		self.server = smtplib.SMTP("smtp.gmail.com:587")
		self.server.ehlo()
		self.server.starttls()
		self.server.login(credentials.credentials['email'], credentials.credentials['password'])

	def send_mail(self): 	 
		self.server.sendmail(self.msg['From'], self.emaillist , self.msg.as_string())

	def fast_send(self):
		self.build_msg()
		self.server_connect()
		self.send_mail()

if __name__ == '__main__':
	mail = SendMail(['administracion@borbolla-automation.com' , 'ingenieria@borbolla-automation.com'] , 'sql_bk.py' , subject = 'qwertyuio')
	mail.fast_send()