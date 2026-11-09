import datetime
import json
import logging

def date_format_in_ics(date_iso: str):
    return  date_iso.replace("-",'').replace(":",'').split('.')[0]

def json_to_ics(calendar,save_path):
    with open(save_path,"w",encoding='utf-8') as f:
        f.write('''BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//MyCalendar//RU''')
        for event in calendar["events"]:
            date_create = date_format_in_ics(event["date_create"])
            if event['type_and_data'][0]==0:
                start_day_plas_sdvig = str(int(event["type_and_data"][3])+1)
                date_start = str(calendar["old"])+'01'+(str(start_day_plas_sdvig) if len(start_day_plas_sdvig)>1 else str("0"+start_day_plas_sdvig))
                _is_all_day = (event["start_time"]=='' and event["end_time"]=='')
                if event["start_time"]!="":
                    date_time_start = "DTSTART;TZID=Europe/Moscow:"+date_start+'T'+str(event["start_time"]).replace(":",'')
                elif _is_all_day == True: 
                    date_time_start = f'DTSTART;TZID=Europe/Moscow;VALUE=DATE:{date_start}'
                else:
                    date_time_start = "DTSTART;TZID=Europe/Moscow:"+date_start+'T'+"000001"
                if event["end_time"]!="":
                    date_time_end = "DTEND:"+date_start+'T'+str(event["end_time"]).replace(":",'')
                elif _is_all_day==True:
                    date_time_end = None
                else: 
                    date_time_end = "DTEND:"+date_start+'T'+"235959"

                if date_time_end != None:
                    date_time = date_time_start+'\n'+date_time_end
                else:
                    date_time = date_time_start
                f.write(
                        f'''BEGIN:VEVENT
UID:{event["uuid"]}@yarik-calendar.local
DTSTAMP:{date_create}Z
{date_time}
RRULE:FREQ=DAILY;INTERVAL={event['type_and_data'][1]};COUNT={event['type_and_data'][2]}
SUMMARY:{event["event_name"]}
STATUS:CONFIRMED
END:VEVENT
'''
                    )
        f.write("END:VCALENDAR")
                

# BEGIN:VEVENT
# UID:work-3x3@yarik-calendar.local
# DTSTAMP:20261108T180000Z
# DTSTART:20261109T090000
# DTEND:20261109T170000
# RRULE:FREQ=DAILY;INTERVAL=6;COUNT=3
# SUMMARY:Рабочий день (3 через 3)
# DESCRIPTION:Цикл: 3 рабочих дня, затем 3 выходных. Серия начинается 9 ноября 2026.
# STATUS:CONFIRMED
# END:VEVENT

# END:VCALENDAR

# TEST
from backend import Generator
calendar = Generator()._open(r'E:\calendar\data\1794245591.9345262.json')
json_to_ics(calendar,'test.ics')
# print(datetime.datetime.isoformat(datetime.datetime.now()))



# BEGIN:VCALENDAR
# PRODID:-//Google Inc//Google Calendar 70.9054//EN
# VERSION:2.0
# CALSCALE:GREGORIAN
# METHOD:PUBLISH
# X-WR-CALNAME:test
# X-WR-TIMEZONE:Europe/Moscow
# BEGIN:VTIMEZONE
# TZID:Europe/Moscow
# X-LIC-LOCATION:Europe/Moscow
# BEGIN:STANDARD
# TZOFFSETFROM:+0300
# TZOFFSETTO:+0300
# TZNAME:GMT+3
# DTSTART:19700101T000000
# END:STANDARD
# END:VTIMEZONE
# BEGIN:VEVENT
# DTSTART;TZID=Europe/Moscow:20260102T073000
# DTEND;TZID=Europe/Moscow:20260102T193000
# RRULE:FREQ=DAILY;COUNT=3;INTERVAL=3
# DTSTAMP:20261109T182626Z
# UID:a0549898-f337-45ac-9d86-af369909cf84@yarik-calendar.local
# CREATED:20261109T181351Z
# LAST-MODIFIED:20261109T181602Z
# SEQUENCE:0
# STATUS:CONFIRMED
# SUMMARY:Название1
# TRANSP:OPAQUE
# END:VEVENT
# BEGIN:VEVENT
# DTSTART;TZID=Europe/Moscow:20260102T073000
# DTEND;TZID=Europe/Moscow:20260102T235959
# RRULE:FREQ=DAILY;COUNT=1;INTERVAL=3
# DTSTAMP:20261109T182626Z
# UID:ae265342-4963-4310-bfe3-708a0fc09829@yarik-calendar.local
# CREATED:20261109T181351Z
# LAST-MODIFIED:20261109T181602Z
# SEQUENCE:0
# STATUS:CONFIRMED
# SUMMARY:Название2
# TRANSP:OPAQUE
# END:VEVENT
# BEGIN:VEVENT
# DTSTART;VALUE=DATE:20260105
# DTEND;VALUE=DATE:20260106
# RRULE:FREQ=DAILY;COUNT=1;INTERVAL=1
# DTSTAMP:20261109T182626Z
# UID:70a3199e-4158-4396-a2bf-5ec4cb44abaf@yarik-calendar.local
# CREATED:20261109T181351Z
# LAST-MODIFIED:20261109T181602Z
# SEQUENCE:0
# STATUS:CONFIRMED
# SUMMARY:Название3
# TRANSP:OPAQUE
# END:VEVENT
# BEGIN:VEVENT
# DTSTART;TZID=Europe/Moscow:20260102T000001
# DTEND;TZID=Europe/Moscow:20260102T065500
# RRULE:FREQ=DAILY;COUNT=1;INTERVAL=6
# DTSTAMP:20261109T182626Z
# UID:06ceba01-ce7f-4f66-b269-bba0672e5afe@yarik-calendar.local
# CREATED:20261109T181351Z
# LAST-MODIFIED:20261109T181602Z
# SEQUENCE:0
# STATUS:CONFIRMED
# SUMMARY:Название2
# TRANSP:OPAQUE
# END:VEVENT
# END:VCALENDAR
