

class Cache():
    def __init__(self):
        super().__init__()
        self.data = {}
    def _add_value(self,key,value):
        self.data[key]=value
        return True
    def _export(self,kay):
        return self.data.get(kay,None)
    def _remuve(self, kay):
        try:
            self.data.pop(kay)
            return True
        except: 
            return False
        