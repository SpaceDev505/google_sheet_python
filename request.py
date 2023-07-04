import requests
import gspread
from oauth2client.service_account  import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']


credentials = ServiceAccountCredentials.from_json_keyfile_name('key.json', scopes=scope)
gc = gspread.authorize(credentials)
sheet = gc.open_by_key('1bTl1gcKI0iJYcHoBtZLpeXrJm7WETx8zlMZx0YdfTL4')
ws = sheet.worksheet('SpaceVision')


# ws.update('B3', '1234')
# ws.update_cell(3, 2, '233333')

# eia_url = 
spaceurl = 'https://www.api.thespacevision.net/home2/ocizguwu/server/crude/'
space_response  = requests.get(spaceurl)

# index = 3
# if space_response.status_code == 200:
#     spacejson = space_response.json()
#     spacecrude = spacejson['data'][-4:]
#     for space in reversed(spacecrude):
#         print(space)
#         date = space['date']
#         SAE = space['SAE']
#         SAX = space['SAX']
#         SAS = space['SAS']
        
#         ws.update_cell(index, 1, date)
#         ws.update_cell(index, 2, SAE)
#         ws.update_cell(index, 3, SAX)
#         ws.update_cell(index, 4, SAS)
        
#         index += 1
#         print(date)

#     # update date
#     date = spacecrude[-1]
#     print('date123',date['date'])
#     ws.update_cell(14, 7, date['date'])
# else:
#     print("request failed")

index_eia = 3
eiaurl = "http://api.thespacevision.net/home2/ocizguwu/server/eia/"
eia_response = requests.get(eiaurl)

if eia_response.status_code == 200:
    eiajson = eia_response.json()
    eiacrude = eiajson['data'][-4:]
    for eia in reversed(eiacrude):
        print(eia)
        date = eia['date']
        SAE = eia['SAE']
        SAX = eia['SAX']
        SAS = eia['SAS']
        
        ws.update_cell(index_eia, 5, SAE)
        ws.update_cell(index_eia, 6, SAX)
        ws.update_cell(index_eia, 7, SAS)
        
        index_eia += 1
        print(date)
else:
    print('failed eia crude oil request')





