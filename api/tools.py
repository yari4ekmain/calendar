import json
import datetime
import logging.config as lg
import logging
import os
CLASS_NAME = 'Tools'
VERSION = '1.1.1.1'
NAMEAPP = "CALENDAR"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "detailed": {
            # Ключевые поля для понимания "откуда упало":
            "format": "[%(asctime)s] %(levelname)s "
                      "| %(name)s "          # полное имя логгера (модуль.Класс)
                      "| %(module)s:%(funcName)s:%(lineno)d "  # файл, функция, строка
                      "| %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "detailed",
            "level": "INFO",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/app.log",
            "maxBytes": 10_000_000,
            "backupCount": 1,
            "formatter": "detailed",
            "level": "DEBUG",  # в файл можно писать всё, в консоль — только важное
        },
    },
    "root": {
        "level": "DEBUG",        
        "handlers": ["console", "file"],
    },}

START_SETTING = {
    "version":VERSION,
    "language":'ru',
    "save_pach":f'{os.getcwd()}',
    "calendars": [],
    "tam":"black"
}

SETTING = {}

class Tools():
    def __init__(self):
        super().__init__()



    def StartApp(self):
        global SETTING
        lg.dictConfig(LOGGING_CONFIG)
        try:
            with open('setting.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        if data.get('version', '') == '':
            with open('setting.json', 'w', encoding='utf-8') as f:
                json.dump(START_SETTING, f, indent=2, ensure_ascii=False)
            data = START_SETTING  
        SETTING = data
        if not os.path.isdir(SETTING["save_pach"]+"/data"):
            os.mkdir(SETTING["save_pach"]+"/data")
        return SETTING
    def ReturnCalendarsData(self):
        data_pash = SETTING["save_pach"]+"/data"
        lis = os.listdir(data_pash)
        if len(lis)==0:
            logging.info("ReturnCalendarsData: NOT CALENDAR")
            return []
        reqvest = []
        for calendar in lis:
            try:
                with open(f"{data_pash}/{calendar}","r") as f:
                    data = json.load(f)
                name = data["name"]
                old = data["old"]
                events = data["events"]
                path = f"{data_pash}/{calendar}"
                reqvest.append([name,old,events,path])
            except KeyError as e:
                logging.error(f"ReturnCalendarsData: {e}")
        return reqvest
    
    def SortEvent(self,events):
        '''-> end_minutes-start_minutes,event,start_minutes,end_minutes '''
        sort_len_list = []
        for event in events:
            start_not_valid = event["start_time"]
            if start_not_valid != '':
                time_start = start_not_valid
            else: time_start = '00:00:00'
            h, m, _ = map(int, time_start.split(":"))
            start_minutes = h * 60 + m

            end_not_volid = event["end_time"]
            if end_not_volid!='':
                time_end = end_not_volid
            else: time_end = "24:00:00"
            h, m, _ = map(int, time_end.split(":"))
            end_minutes = h * 60 + m   
            sort_len_list.append([end_minutes-start_minutes,event,start_minutes,end_minutes])
            sort_len_list = sorted(sort_len_list, key=lambda x: x[0], reverse=True)
        return sort_len_list
