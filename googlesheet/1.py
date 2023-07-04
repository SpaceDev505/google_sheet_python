import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('spacevission-2-f635f5246f30.json'
            , scope)

gc = gspread.authorize(credentials)
sheet = gc.open_by_key('1bTl1gcKI0iJYcHoBtZLpeXrJm7WETx8zlMZx0YdfTL4')
ws = sheet.worksheet('SpaceVision')
# print(ws.acell('A2'))

ws.update('B4', '123')
