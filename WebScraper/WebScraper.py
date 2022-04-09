import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector as db

payload = {'range': '0', 'limit': '40'}
url = 'https://ramconnect.wcupa.edu/mobile_ws/v17/mobile_events_list'
#header = {'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
response = requests.get(url, params=payload)
#print(response.status_code)
data = response.json()[1:]
fields = {}
keys = data[0]['fields'].split(',')[:-1]

for i in range(0, len(keys)):
    fields[keys[i]] = 'p'+str(i)

events_dict = {'name':[], 'organizer': [], 'date': [], 'location': [], 'description': [] }

for event in data:
    name = event[fields['eventName']]
    if name != 'False':
        events_dict['name'].append(name)
        events_dict['organizer'].append(event[fields['clubName']])
        soup = BeautifulSoup('<b>' + str(event[fields['eventDates']]) + '</b>', 'html.parser')
        date = ''
        for line in soup.findAll('p'):
            date += line.getText() + ' '
        events_dict['date'].append(date)
        events_dict['location'].append(event[fields['eventLocation']])
        events_dict['description'].append(event[fields['ariaEventDetailsWithLocation']])
        
df = pd.DataFrame.from_dict(events_dict)
print(df.head(5))    

cnx = db.connect(user='root', password='notpassword', host='',
        database='events')
