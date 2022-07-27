#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pygsheets
from datetime import datetime, timedelta
import json
import time
now = datetime.now().strftime("%H")
while(now!="44"):
    print(now)
    time.sleep(60)
    now = datetime.now().strftime("%H")
print('end')


# In[ ]:




