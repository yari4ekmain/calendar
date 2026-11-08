import datetime
import json
import logging

def json_to_ics(calendar,save_path):
    with open(save_path,"w") as f:
        f.write('''BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//MyCalendar//RU''')
    



# TEST
from api.backend import Generator
calendar = Generator()._open('1794160620.983157.json')
json_to_ics(calendar,'test.ics')