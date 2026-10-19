import flet as ft
from ui.render_list_calendar import CreateCalendarList, CreateEventList
from api.backend import Generator
from flet_color_pickers import BlockPicker
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
        self.enter = ft.TextButton(content='Далее',on_click=self._valid)
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
    async def _valid(self,e):
        LISTPOLL = ['Название','Год','Тип']
        if (self.input_name.value!='' and self.input_god.value!='' and self.calendar_type_input.selected_index!=None):
            global STARTDATA
            STARTDATA=[self.input_name.value,self.input_god.value,self.calendar_type_input.selected_index]
            await self.inform([self.input_name.value,self.input_god.value,self.calendar_type_input.selected_index]) 
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
        self.generator = Generator()
        global STARTDATA
        self.inform_start = STARTDATA

        self.dialog_picker =BlockPicker(
        color="#9c27b0",
        height=90,
        available_colors=[
            "#f44336",
            "#e91e63",
            "#9c27b0",
            "#3f51b5",
            "#2196f3",
            "#009688",
            "#4caf50",
            "#795548",
        ],)

        self.sheet = ft.BottomSheet(
        show_drag_handle=True,
        content=ft.Container(
            padding=10,
            alignment=ft.Alignment.CENTER,
            content=ft.Column(
            spacing=15,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Новое событие", size=15, weight=ft.FontWeight.BOLD),
                    ft.TextField(label="Название мероприятия", width=400),
                    ft.Row(
                        [
                            ft.TextField(label="Рабочие дни", width=150),
                            ft.TextField(label="Выходные дни", width=150),
                            ft.TextField(label="Сдвиг", width=100, value="0"),
                        ],
                        spacing=10,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    self.dialog_picker,
                    ft.Row(
                        [
                            ft.TextButton(content="Отменить", on_click=lambda e: self.page.pop_dialog()),
                            ft.TextButton(content="Сохранить", on_click=self._valid),
                        ],
                        
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),],),),)

        self.AddEventButton = ft.TextButton(content="Добавить событие", on_click=lambda e: self.page.show_dialog(self.sheet))

        self.CreateCalendarList = CreateCalendarList(self.inform_start,self.generator)
        self.panel_list = CreateEventList(self.generator,self.CreateCalendarList)    

        self.column = ft.Column([
            self.AddEventButton,
            self.panel_list 
            ])

        self.content = (ft.Row([ft.Container(self.column,bgcolor="#242424",expand=True),self.CreateCalendarList]))
    def _valid(self, e):
        event_data = self.sheet.content.content.controls
        if (event_data[1].value != '' and event_data[2].controls[0].value!='' and 
            event_data[2].controls[1].value!='' and event_data[2].controls[2].value!=''):
            self._addEvent([event_data[1].value, int(event_data[2].controls[0].value), 
                            int(event_data[2].controls[1].value), int(event_data[2].controls[2].value), event_data[3].color])

    def _addEvent(self, event_data):
        event = {"event_name":event_data,"event_color":event_data[-1]}
        data = self.generator._addEvents(event_data[1],event_data[2],event_data[3],event)
        self.panel_list.RenderPaner(data)
        self.panel_list.update()
        self.update()
        self.CreateCalendarList._update(data)
        self.CreateCalendarList.update()
        
        self.page.pop_dialog()
        


class CreateCalendarUser(ft.Container):
    def __init__(self,inform_start):
        super().__init__()
        self.content = ft.Text('Uaer')

class CreateCalendarWeekday(ft.Container):
    def __init__(self,inform_start):
        super().__init__()
        self.content = ft.Text('Weekday')

