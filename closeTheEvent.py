import pygsheets
from datetime import datetime, timedelta
import json
import time
now = datetime.now().strftime("%H")
while(now!="8"):
    print(now)
    time.sleep(60)
    now = datetime.now().strftime("%H")
print('end')
gc = pygsheets.authorize(service_file='./creds.json')
survey_url = 'https://docs.google.com/spreadsheets/d/1QwnPezCF8T_TJgY9C0vTa_lykLgXF2Y-WEYPISwRZkA/'
sh = gc.open_by_url(survey_url)
testData=sh.worksheet('title','testData')
testData.update_col(0, values=[now], row_offset=0)