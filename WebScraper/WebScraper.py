import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector

#gets event data from site and exports to mysql server
def scrape():
    #get data from website
    payload = {'range': '0', 'limit': '40'}
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

    export_data(events_dict)

def export_data(data):
    #connect to mysql database
    mydb = mysql.connector.connect(host='mydb', user='root', password='notpassword', database='campus')
    cursor = mydb.cursor()
    
    placeholders = ', '.join(['%s'] * len(data))
    colums = ', '.join(data.keys())
    query = 'INSERT INTO events ( %s ) VALUES ( %s )'

    

def init_db():
    mydb = mysql.connector.connect(host='mydb', port='3306', user='root', password='notpassword')

    cursor = mydb.cursor()
    cursor.execute('DROP DATABASE IF EXISTS campus')
    cursor.execute('CREATE DATABASE campus')
    cursor.close()

    mydb = mysql.connector.connect(host='mydb', port='3306', user='root', password='notpassword', database='campus')

    cursor = mydb.cursor()
    cursor.execute('DROP TABLE IF EXISTS events')
    cursor.execute('CREATE TABLE events (id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            organizer VARCHAR(255),
            date VARCHAR(255),
            location VARCHAR(255),
            description VARCHAR(255))')
    cursor.close()

print('init database')

if __name__ == __main__:
    scrape()
    init_db()

