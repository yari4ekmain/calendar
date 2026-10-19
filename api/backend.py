import json 
import datetime

class Generator():
    def __init__(self):
        super().__init__()

    def _get_shift(self, mes) -> int:
        """Смещение: 0 = понедельник, 1 = вторник, ... 6 = воскресенье"""
        return datetime.date(int(self.old), mes, 1).weekday()
        
    def _vesocos(self):
        return (self.old%100!=0 and self.old%4==0)

    def _open(self,path):
        with open(path,"r") as f:
            self.data = json.load(f)
            self.old = self.data["old"]
    def _generetor(self,inform_start):
        self.inform_start = inform_start
        self.old = int(self.inform_start[1])
        self._get_shift
        self.data = {
            "name":self.inform_start[0],
            "old":self.old,
            "weeks":{},
            "events":[]
        }
        for mes in range(1,12 +1):
            self.data["weeks"][f"{mes}"]=self._get_shift(mes)
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
                    continue
                if (mes in [4,6,9,11] and day>30) or (mes==2 and day>29):
                    continue
                _mes_data.append(_day_data)
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

