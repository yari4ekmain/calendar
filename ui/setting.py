import json 

EVENT = {"event_name":"work", "event_color":"#004E97"}
PATH = 'data/data.json'
class Generator():
    def __init__(self):
        super().__init__()
        
    def _vesocos(self):
        return (self.old%100!=0 and self.old%4==0)

    def _open(self,path):
        with open(path,"r") as f:
            self.data = json.load(f)
            self.old = self.data["old"]
            
    def _generetor(self,old):
        self.old = int(old)
        self.data = {
            "old":self.old
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
        
    def _addEvents(self, work,chill,sdvig,event):
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
                
        
    def _addEvent(self, dataevent, event):
        """dataevent = [mes, day] mes -- int, day -- int"""
        self.data[f'{dataevent[0]}'][dataevent[1]-1]["events"].append(event)
        
    def _seve(self,pathname):
        with open(pathname ,'w') as f:
            json.dump(self.data,f,indent=2)
        return self.data

gen = Generator()
gen._generetor(2026)
gen._addEvents(3,3,5,EVENT)
gen._addEvent([1,3],EVENT)
print(gen._seve(PATH))
print(gen._open(PATH))

