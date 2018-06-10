import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
		'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('SPCMachines-47b188100dd5.json' , scope)
client = gspread.authorize(creds)
print(client)

sheet = client.open('STATISTICAL PROCESS CONTROL').sheet10

records = sheet.get_all_records()
print(records)
