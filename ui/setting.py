import json 

EVENT1 = {"event_name":"work", "event_color":"#004E97"}
EVENT2 = {"event_name":"fffffff", "event_color":"#C7D1DA"}
PATH = 'data/data.json'
import json 

class Generator():
    def __init__(self):
        super().__init__()
        
    def _vesocos(self):
        return (self.old%100!=0 and self.old%4==0)

    def _open(self,path):
        with open(path,"r") as f:
            self.data = json.load(f)
            self.old = self.data["old"]
    def _generetor(self,inform_start):
        self.inform_start = inform_start
        self.old = int(self.inform_start[1])
        self.data = {
            "name":self.inform_start[0],
            "old":self.old,
            "events":[]
        }
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



gen = Generator()
gen._generetor(["fff", 2026,1])
gen._addEvents(2,3,3,EVENT1)
gen._addEvents(3,4,5,EVENT2)
gen._seve("data/data1.json")
print(gen._remuveEvent(EVENT1))
gen._seve("data/data2.json")

