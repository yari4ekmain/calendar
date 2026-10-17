import flet as ft
from ui.render_list_calendar import CreateCalendarDayToDayList
STARTDATA = []
class CreateCalendarStart(ft.Row):
    def __init__(self,inform):
        super().__init__()
        self.inform = inform
        self.calendar_type_input = ft.CupertinoSlidingSegmentedButton(
            selected_index=2,
            controls=[
                ft.Text('Дней через дней'),
                ft.Text("По дням недели"),
                ft.Text("Пользавательский")
            ],on_change=self._calendarTupe
        )
        
        self.error = ft.Text("",color="#ff5e5e")
        self.info = ft.Text('   Свободное расписание —  конкретные даты.',text_align=ft.MainAxisAlignment.CENTER)
        self.input_name = ft.TextField(label="Название")
        self.input_god = ft.TextField(value=2026)
        self.enter = ft.TextButton(text='Далее',on_click=self._valid)
        self.controls = [ft.Column([
                    ft.Text('Создание календаря',size=20),
                    self.error,
                    ft.Text("   Введите название:"),
                    ft.Container(content=self.input_name,padding=ft.Padding(15,0,0,0),width=400),

                    ft.Text("   Введите год:"),
                    ft.Container(content=self.input_god,padding=ft.Padding(15,0,0,0),width=400),

                    ft.Text("   Выберите тип:"),
                    ft.Container(content=self.calendar_type_input,padding=ft.Padding(15,0,0,0)),
                    self.info,
                    self.enter
            ])]
       
        self.alignment=ft.MainAxisAlignment.CENTER
        self.expand = True
    def _calendarTupe(self, e):
        if self.calendar_type_input.selected_index == 0:
            self.text = """   Задача повторяется через равные промежутки."""
        
        elif self.calendar_type_input.selected_index==1:
            self.text = '''   Задача повторяется в конкретные дни недели.'''
        
        else:
            self.text = '''   Свободное расписание —  конкретные даты.'''
        
        self.info.value = self.text
        self.update()
    def _valid(self,e):
        LISTPOLL = ['Название','Год','Тип']
        if (self.input_name.value!='' and self.input_god.value!='' and self.calendar_type_input.selected_index!=None):
            global STARTDATA
            STARTDATA=[self.input_name.value,self.input_god.value,self.calendar_type_input.selected_index]
            self.inform([self.input_name.value,self.input_god.value,self.calendar_type_input.selected_index]) 
        else:
            if self.input_name.value=='':
                x=0
            elif self.input_god.value=='':
                x=1
            else:
                x=2
            self.error.value = f'   не заполнено поле: {LISTPOLL[x]}'
            self.update()

class CreateCalendarDayToDay(ft.Container):
    def __init__(self,inform_start):
        super().__init__()
        global STARTDATA
        self.inform_start = STARTDATA
        
        self.workday = ft.TextField(label='Количество рабочих дней')
        self.chillday = ft.TextField(label='Количество выходных дней')
        self.sdvig = ft.TextField(label='сдвиг')

        self.column = ft.Column([
            ft.Text(''),
            self.workday,
            self.chillday,
            self.sdvig,
            
            ])
        self.content = ft.Row([self.column,CreateCalendarDayToDayList(self.inform_start[1])])



class CreateCalendarUser(ft.Container):
    def __init__(self,inform_start):
        super().__init__()
        self.content = ft.Text('Uaer')

class CreateCalendarWeekday(ft.Container):
    def __init__(self,inform_start):
        super().__init__()
        self.content = ft.Text('Weekday')