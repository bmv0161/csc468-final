import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
from sqlalchemy import types, create_engine

#gets event data from site and exports to mysql server
def scrape():
    #get data from website
    payload = {'range': '0', 'limit': '80'}
    url = 'https://ramconnect.wcupa.edu/mobile_ws/v17/mobile_events_list'
    response = requests.get(url, params=payload)
    #create dictionary of fields to make accessing data easier
    data = response.json()[1:]
    fields = {}
    keys = data[0]['fields'].split(',')[:-1]
    for i in range(0, len(keys)):
        fields[keys[i]] = 'p' + str(i)
    #create dictionary for table entries
    events_dict = {'name':[], 'organizer': [], 'date': [], 'location': [], 'description': [] }
    #step through data, add entries to events_dict
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
    init_db(df)
    export_data(df)

def export_data(data):
    #connect to mysql database
    engine = create_engine('mysql+mysqlconnector://root:notpassword@mydb:3306/campus')
    data.to_sql(name='events', con=engine, if_exists='append', index=False)

def init_db(data):
    mydb = mysql.connector.connect(host='mydb', port='3306', user='root', password='notpassword', database='campus')
    query = '''CREATE TABLE events (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            %s VARCHAR(255),
            %s VARCHAR(255),
            %s VARCHAR(255),
            %s VARCHAR(255),
            %s VARCHAR(255))''' % (tuple(data.columns))
    cursor = mydb.cursor()
    cursor.execute('DROP TABLE IF EXISTS events')
    cursor.execute(query)
    cursor.close()
    mydb.close()

print('init database')

if __name__ == '__main__':
    scrape()

