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
            "backupCount": 5,
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
                reqvest.append([name,old,events])
            except KeyError as e:
                logging.error(f"ReturnCalendarsData: {e}")
        return reqvest