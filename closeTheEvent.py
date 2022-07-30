import pygsheets
from datetime import datetime, timedelta
import json
import time
now = datetime.utcnow().strftime("%H")
''''''
while(now!="00" and now!="24"):
    #print(now)
    time.sleep(600)
    now = datetime.utcnow().strftime("%H")
print('end')

gc = pygsheets.authorize(service_file='./creds.json')
survey_url = 'https://docs.google.com/spreadsheets/d/1QwnPezCF8T_TJgY9C0vTa_lykLgXF2Y-WEYPISwRZkA/edit?fbclid=IwAR2oDcXlmmfvC90cSgog-rU7nYjDrpBY6chkcmjxoyan-lS0zdpPSWJBw1k#gid=1852814271'
sh = gc.open_by_url(survey_url)
newData=sh.worksheet('title','WeightTest')
oldData=sh.worksheet('title','CakemonDataTest')
newWeight=newData.get_col(2,include_tailing_empty=False)
oldData.update_col(2, values=newWeight, row_offset=0)
while(True):
    time.sleep(3600)