import requests
import json
from bs4 import BeautifulSoup

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


for event in data:
    name = event[fields['eventName']]
    print(name)
    if name != 'False':
        print(event[fields['clubName']])
        dateTag = event[fields['eventDates']]
        soup = BeautifulSoup('<b>' + str(dateTag) + '</b>', 'html.parser')
        date = ''
        for line in soup.findAll('p'):
            date += line.getText() + ' '
        print(date)
        print(event[fields['eventLocation']])
        print(event[fields['ariaEventDetailsWithLocation']])
        print()

