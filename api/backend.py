import json 
import datetime
import logging
class Generator():
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(f"{__name__}.Generator")
    def _get_shift(self, mes, day) -> int:
        """Смещение: 0 = понедельник, 1 = вторник, ... 6 = воскресенье"""
        return datetime.date(int(self.old), mes, day).weekday()
        
    def _vesocos(self):
        return (self.old%100!=0 and self.old%4==0)

    def _open(self,path):
        with open(path,"r") as f:
            self.data = json.load(f)
            self.old = self.data["old"]
        return self.data
    def _generetor(self,inform_start):
        self.inform_start = inform_start
        self.old = int(self.inform_start[1])
        self.data = {
            "name":self.inform_start[0],
            "old":self.old,
            "weeks":{},
            "events":[]
        }
        for mes in range(1,12 +1):
            self.data["weeks"][f"{mes}"]=self._get_shift(mes,1)
        for mes in range(1,12 +1):
            _mes_data = []
            for day in range(1,31 +1):
                event = []
                
                _day_data={
                    "day":day,
                    "mes":mes,
                    "events":event
                     
                    }
                if self._vesocos() and mes ==2 and day==29:
                    None
                elif (mes in [4,6,9,11] and day>30) or (mes==2 and day>28):
                    continue
                _day_data["weekday"] = self._get_shift(mes,day)
                _mes_data.append(_day_data)
            self.logger.info("GENERATOR RENEREIN aplay")
            self.data[f"{mes}"]=_mes_data
        return self.data
    def _addEvents(self, work: int,chill: int,sdvig: int,event):
        self.data["events"].append(event)
        caunt = sdvig 
        flag = False
        for mes in range(1,12 +1):
            _mes_data = self.data[f"{mes}"]
            for day in _mes_data:
                if caunt>0 and flag == False:
                    caunt-=1
                    continue
                elif caunt == 0 and flag == False:
                    caunt -= work
                    flag = True
                elif caunt == 0 and flag == True:
                    caunt -= chill
                    flag = False
                if caunt <0 and flag ==True:
                    caunt+=1
                    day["events"].append(event)
                elif caunt<0 and flag ==False:
                    caunt+=1
        return self.data
        
    def _addEvent(self, dataevent, event):
        """dataevent = [mes, day] mes -- int, day -- int"""
        self.data[f'{dataevent[0]}'][dataevent[1]-1]["events"].append(event)
        self._seve("")
        return self.data

    def _addEventWeekday(self,dayx, event):
        self.data["events"].append(event)
        for mes in range(1,12 +1):
            _mes_data = self.data[f"{mes}"]
            for day in _mes_data:
                self.logger.info(f"Generanor ADDEVENT WEEKDAY dayx: {dayx}, daydata: {day["weekday"]}")
                if int(day["weekday"])==int(dayx):
                     
                    day["events"].append(event)
        return self.data
    
    def _remuveEvent(self,event):
        self.data["events"].remove(event)
        for mes in range(1,13):
            for day in self.data[f"{mes}"]:
                if day['events'].count(event):
                    (day["events"]).remove(event)
        return self.data

    def _seve(self,pathname):
        with open(pathname ,'w') as f:
            json.dump(self.data,f,indent=2)
        return self.data

VALUECONTRAST = 50
def average_hex_color(hex1: str, hex2: str) -> str:
    """
    Возвращает средний HEX-цвет по двум входным HEX-кодам.
    Поддерживает форматы: '#RRGGBB' или 'RRGGBB'.
    """
    def hex_to_rgb(hex_code: str):
        hex_code = hex_code.lstrip('#')
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return r, g, b

    def rgb_to_hex(r: int, g: int, b: int) -> str:
        r = max(0, min(255, round(r)+VALUECONTRAST))
        g = max(0, min(255, round(g)+VALUECONTRAST))
        b = max(0, min(255, round(b)+VALUECONTRAST))
        return f"#{r:02X}{g:02X}{b:02X}"

    r1, g1, b1 = hex_to_rgb(hex1)
    r2, g2, b2 = hex_to_rgb(hex2)

    avg_r = (r1 + r2 + VALUECONTRAST) / 2
    avg_g = (g1 + g2) / 2
    avg_b = (b1 + b2) / 2

    return rgb_to_hex(avg_r, avg_g, avg_b)

g = Generator()
event_1 = {
      "event_name": "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435",
      "event_color": "#00ff0d",
      "start_time": "  ",
      "end_time": "  "
    }
event_2 = {
      "event_name": "cull",
      "event_color": "#8c00ff",
      "start_time": "  ",
      "end_time": "  "
    }
g._generetor(['test',2026])
g._addEvents(3,3,0,event_1)
g._addEventWeekday(6,event_2)
g._addEventWeekday(0,event_2)
g._seve('data/dataTEST.json')