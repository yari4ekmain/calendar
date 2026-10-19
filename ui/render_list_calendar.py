import flet as ft
from api.backend import average_hex_color

class CreateCalendarList(ft.Container):
    def __init__(self,inform_start,generator):
        global PATH
        super().__init__()
        self.DATARENDER = 1
        self.listtextmes = [
            "", 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
        self.generator = generator
        self.calendar = self.generator._generetor(inform_start)
        self.NextButton = ft.TextButton('Next',on_click=self.render_next)
        self.ReversButton = ft.TextButton('Revers',on_click=self.render_revers)
        self.RenderListCalendar()

    def TESTdata(self, e):
        print(e.control.data)
    def render_next(self,e):
        if self.DATARENDER>=12:
            self.DATARENDER = 1
        else: self.DATARENDER+=1
        self.RenderListCalendar()
        self.update()

    def render_revers(self,e):
        if self.DATARENDER<=1:
            self.DATARENDER = 12
        else: self.DATARENDER-=1
        self.RenderListCalendar()
        self.update()

    def RenderListCalendar(self):
        data = ft.DataTable(    
                columns=[ft.DataColumn(ft.Text("Пн")),
                ft.DataColumn(ft.Text("Вт")),
                ft.DataColumn(ft.Text("Ср")),
                ft.DataColumn(ft.Text("Чт")),
                ft.DataColumn(ft.Text("Пт")),
                ft.DataColumn(ft.Text("Сб")),
                ft.DataColumn(ft.Text("Вс",color="#8f0101"))]
        )
        dayMes = 0
        dataNed = []
        week = self.calendar["weeks"][f'{self.DATARENDER}']
        lens = len(self.calendar[f'{self.DATARENDER}'])
        dayMes+=week
        for day in self.calendar[f'{self.DATARENDER}']:
            if week>0:
                while week>0:
                    x = ft.DataCell(ft.Container(ft.Text("-"),expand=True))
                    dataNed.append(x) 
                    print('-')
                    week-=1
                dayMes = week
            if len(dataNed)==7:
                data.rows.append(ft.DataRow(cells=dataNed))
                dataNed = []
            color= None
            if len(day["events"])>1:
                color = day["events"][0]["event_color"]
                for event in day["events"][1:]:
                    color = average_hex_color(event["event_color"],color)
            elif len(day["events"])==1:
                color = day["events"][0]["event_color"]
            x = ft.DataCell(ft.Container(ft.Text(day["day"],color=color),on_click=self.TESTdata,data=day,expand=True))
            dataNed.append(x)   
            dayMes+=1
            print('day:',dayMes,'neddata:', len(dataNed))
            if int(day["day"])==lens:
                
                while len(dataNed)!=7:
                    dayMes+=1
                    print('--',dayMes%7)
                    x = ft.DataCell(ft.Container(ft.Text("-"),expand=True))
                    dataNed.append(x) 
                print('----','neddata:', len(dataNed))
                data.rows.append(ft.DataRow(cells=dataNed))
        self.generator._seve('data/dataTEST.json')
        self.content = ft.Column([
                    ft.Text(self.listtextmes[self.DATARENDER]),
                    ft.Row([
                        self.ReversButton,
                        data,
                        self.NextButton
                ])])
    def _update(self, data):
        self.calendar = data
        self.RenderListCalendar()
        self.update()

class CreateEventList(ft.ExpansionPanelList):
    def __init__(self, generator, render):
        super().__init__()
        self.render = render
        self.generator = generator
        self.expand_icon_color=ft.Colors.AMBER
        self.divider_color=ft.Colors.AMBER
        self.controls=[]

    def _remuveEvent(self, e):
        print(e.control.data)
        event = e.control.data
        data = self.generator._remuveEvent(event)
        self.RenderPaner(data)
        self.render._update(data)
        self.update()
    def RenderPaner(self, data):
        self.data = data
        self.controls.clear()
        i=0
        
        if data==None:
            self.controls.append(ft.ExpansionPanel(
                header=ft.ListTile(title=ft.Text(f"Panel {i}")),
                content=ft.ListTile(
                    title=ft.Text(f"Событие 00"),
                    subtitle=ft.Text(f"Press the icon to delete panel "),
                    trailing=ft.IconButton(
                        icon=ft.Icons.DELETE
                    ),),))
            
            return 0 
        for event in data["events"]:
            i+=1
            color=event["event_color"]
            self.controls.append(
                    ft.ExpansionPanel(
                bgcolor=color,
                header=ft.ListTile(title=ft.Text(f"Panel {i}"), bgcolor=color),
                content=ft.ListTile(
                    bgcolor=color,
                    title=ft.Text(f"Событие {event['event_name']}"),
                    subtitle=ft.Text(f"Press the icon to delete panel {i}"),
                    trailing=ft.IconButton(
                        icon=ft.Icons.DELETE,
                        on_click=self._remuveEvent,
                        data=event
                    ),),))
        
            