import flet as ft
from api.backend import Generator

 

class CreateCalendarDayToDayList(ft.Container):
    def __init__(self,god):
        super().__init__()
        self.DATARENDER = 1

        self.listtextmes = [
            'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
        self.generator = Generator()
        self.calendar = self.generator._generetor(int(god))
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
        lens = len(self.calendar[f'{self.DATARENDER}'])
        for day in self.calendar[f'{self.DATARENDER}']:
            
            if dayMes%7==0 and dayMes>0:
                data.rows.append(ft.DataRow(cells=dataNed))
                dataNed = []
            x = ft.DataCell(ft.Container(ft.Text(day["day"]),on_click=self.TESTdata,data=dayMes+1,expand=True))
            dataNed.append(x)   
            dayMes+=1
            if dayMes==lens:
                while dayMes%7!=0:
                    dayMes+=1
                    x = ft.DataCell(ft.Container(ft.Text("-"),expand=True))
                    dataNed.append(x) 
                data.rows.append(ft.DataRow(cells=dataNed))
        
        self.content = ft.Column([
                    ft.Text(self.listtextmes[self.DATARENDER]),
                    ft.Row([
                        self.ReversButton,
                        data,
                        self.NextButton
                ])])
         

            
