import datetime
import json
import logging
import os

logger = logging.getLogger(f"{__name__}.FormatCore")
KEYWEEKDAY_IN_ICS = ['MO','TU','WE','TH','FR','SA','SU']
def date_format_in_ics(date_iso: str):
    return  date_iso.replace("-",'').replace(":",'').split('.')[0]

def date_ics_sgvig_in_work(start_sdvig:int = 0,old:int = 2026,sdvig:int = 0):
    start_day_plas_sdvig = str(int(start_sdvig)+1+sdvig)
    date_start = str(old)+'01'+(str(start_day_plas_sdvig) if len(start_day_plas_sdvig)>1 else str("0"+start_day_plas_sdvig))
    return date_start

def date_time_in_ics(event,date_start):
    _is_all_day = (event["start_time"]=='' and event["end_time"]=='')
    if event["start_time"]!="":
        date_time_start = "DTSTART:"+date_start+'T'+str(event["start_time"]).replace(":",'')
    elif _is_all_day == True: 
        date_time_start = f'DTSTART;VALUE=DATE:{date_start}'
    else:
        date_time_start = "DTSTART:"+date_start+'T'+"000001"
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
    return date_time

def film_adaptation_isc(text:str):
    return text.replace(',','\\,').replace(';','\\;').replace(':','\\:').replace('\\','\\\\')

def json_to_ics(
        calendar = {
                'old':int,
                "events":[
                        {
                        "uuid": str,
                        "event_name": str,
                        "event_color": str,
                        "start_time": str,
                        "end_time": str,
                        "date_create": str,
                        "date_edit": str,
                        "type_and_data": [int,str,str,str | list]
                        }
                    ]
        },
        save_path:str = ''
                ): 
    try:
        with open(f"{save_path}.ics","w",encoding='utf-8') as f:
            f.write('''BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//MyCalendar//RU\n''')
            for event in calendar["events"]:
                description = None
                if event.get("description")!=None:
                    description = f"\nDESCRIPTION:{film_adaptation_isc(event["description"])}"
                
                date_create = date_format_in_ics(event["date_create"])
                if event['type_and_data'][0]==0:
                    for work_day in range(0,int(event['type_and_data'][2])):
                        date_start = date_ics_sgvig_in_work(event["type_and_data"][3],calendar['old'],work_day)
                        date_time = date_time_in_ics(event,date_start)
                        f.write(
                            f'''BEGIN:VEVENT
    UID:{event["uuid"]}-{work_day}@yarik-calendar.local
    DTSTAMP:{date_create}Z
    {date_time}{description}
    RRULE:FREQ=DAILY;INTERVAL={int(event['type_and_data'][1])+int(event['type_and_data'][2])}
    SUMMARY:{event["event_name"]}
    STATUS:CONFIRMED
    END:VEVENT\n
    '''
                        )

                elif event['type_and_data'][0]==1:

                    for weekday in range(0,7):
                        if event['type_and_data'][1][weekday]==1:
                            date_start = date_ics_sgvig_in_work(0,calendar['old'])
                            date_time = date_time_in_ics(event,date_start)
                            f.write(
                            f'''BEGIN:VEVENT
    UID:{event["uuid"]}-{KEYWEEKDAY_IN_ICS[weekday]}@yarik-calendar.local
    DTSTAMP:{date_create}Z
    {date_time}{description}
    RRULE:FREQ=WEEKLY;BYDAY={KEYWEEKDAY_IN_ICS[weekday]}
    SUMMARY:{event["event_name"]}
    STATUS:CONFIRMED
    END:VEVENT\n
    '''
                        )
                
                else:
                    date_start = str(event['type_and_data'][0]).replace('-','')
                    date_time = date_time_in_ics(event,date_start)
                    f.write(
                        f'''BEGIN:VEVENT
UID:{event["uuid"]}@yarik-calendar.local
DTSTAMP:{date_create}Z
{date_time}{description}
SUMMARY:{event["event_name"]}
STATUS:CONFIRMED
END:VEVENT\n
'''
                    )
            
            f.write("END:VCALENDAR")
        return True
    except FileNotFoundError as e:
        logger.error(f'NOT FOLDER: {e}')
        return False
    except PermissionError as e:
        logger.error(f'NOT Permission: {e}')
        return False    
    except OSError as e:
        logger.error(f'FILE SISTEM ERROR: {e}')
        return False        




