import pygsheets
from datetime import datetime, timedelta
import json
import time

gc = pygsheets.authorize(service_file='./creds.json')
survey_url = 'https://docs.google.com/spreadsheets/d/1QwnPezCF8T_TJgY9C0vTa_lykLgXF2Y-WEYPISwRZkA/edit?fbclid=IwAR2oDcXlmmfvC90cSgog-rU7nYjDrpBY6chkcmjxoyan-lS0zdpPSWJBw1k#gid=1852814271'
sh = gc.open_by_url(survey_url)
testData=sh.worksheet('title','test')


while(True):
    List=testData.get_col(1,include_tailing_empty=False)
    Place= len(List)
    testData.add_rows(1)
    testData.update_row(userPlace+1, values=["0"], col_offset=0)
    time.sleep(60)