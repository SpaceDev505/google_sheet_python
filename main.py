import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/adrive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open('testspace')
sheet = workbook.sheet1
# print(sheet.)
for cell in sheet.range('A2:A5'):
    print(cell.value)

print(sheet.acell('A3').value)