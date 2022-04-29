# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import mysql.connector

class ActionEventSearch(Action):

    def name(self) -> Text:
        return "action_event_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is a list of upcoming events:")

        mydb = mysql.connector.connect(host="mydb", user="root", password="notpassword", database="campus")

        cursor = mydb.cursor()
        cursor.execute("SELECT name FROM events LIMIT 5")

        for x in cursor:
            dispatcher.utter_message(text=str(x)[2:-3])
        
        cursor.close()
        mydb.close()

        return []
    
class ActionEventQuery(Action):

    def name(self) -> Text:
        return "action_event_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(host="mydb", user="root", password="notpassword", database="campus")

        event = tracker.get_slot("event")
        cursor = mydb.cursor()
        query = "SELECT date, description FROM events WHERE name=%s"
        cursor.execute(query, (event))
        for x in cursor:
            dispatcher.utter_message(text=str(x))

        cursor.close()
        mydb.close()

        return []
