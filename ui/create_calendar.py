import flet as ft
from ui.render_list_calendar import CreateCalendarList, CreateEventList,CreateEvent
from api.backend import Generator
import logging
STARTDATA = []
class CreateCalendarStart(ft.Row):
    def __init__(self,inform):
        super().__init__()
        self.logger = logging.getLogger(f"{__name__}.CreateCalendarStart")
        self.inform = inform
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
                    self.info,
                    self.enter
            ])]
       
        self.alignment=ft.MainAxisAlignment.CENTER
        self.expand = True
        self.logger.info("CreateCalendarStart: init")
    async def _valid(self,e):
        LISTPOLL = ['Название','Год','Тип']
        if (self.input_name.value!='' and self.input_god.value!=''):
            global STARTDATA
            STARTDATA=[self.input_name.value,self.input_god.value]
            await self.inform('/create_colendar_day_to_day') 
        else:
            if self.input_name.value=='':
                x=0
            elif self.input_god.value=='':
                x=1
            else:
                x=2
            self.error(f"_valid: NOT VALUE: {x}")
            self.error.value = f'   не заполнено поле: {LISTPOLL[x]}'
            self.update()

class CreateCalendarDayToDay(ft.Container):
    def __init__(self,inform_start):
        super().__init__()
        self.logger = logging.getLogger(f"{__name__}.CreateCalendarDayToDay")
        self.generator = Generator()
        global STARTDATA
        self.inform_start = STARTDATA
        self.alignment = ft.Alignment.TOP_CENTER

        self.CreateCalendarList = CreateCalendarList(self.generator._generetor(self.inform_start))
        self.panel_list = CreateEventList(self.generator,self.CreateCalendarList)    

        self.column = ft.Column([
            self.panel_list 
            ],horizontal_alignment=ft.CrossAxisAlignment.START,alignment=ft.MainAxisAlignment.START,scroll=ft.ScrollMode.AUTO)

        self.content = (ft.Column([
                ft.Row([ft.Container(self.column,bgcolor="#242424",width=400,height=300),self.CreateCalendarList]),
                ft.Row([CreateEvent(self._addevent,self._addeventweekdayx)],expand=True)],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN))
        self.logger.info("CreateCalendarDayToDay: init")
        

    def _addevent(self, work: int = None,chill: int=None,sdvig: int=None ,event = {}):
        try:
            self._update(self.generator._addEvents(work,chill,sdvig,event))
            self.logger.info(f"CreateCalendarDayToDay: CREATE (work: {work}, chill: {chill}, sdvig: {sdvig})")
        except Exception as e:
            self.logger.error(f"_addEvent: {e}")
    def _addeventweekdayx(self, workday:list = [], event={}):
        x=0
        data = None
        for day in workday:
            if day.data == 'on':
                data = self.generator._addEventWeekday(x,event)
                
                self.logger.info(f"CreateCalendarDayToDay: CREATE (weekday: {x} day.data: {day.data})")
            x+=1
        self._update(data)
             
    def _update(self, data):
        self.logger.info("CreateCalendarDayToDay: UPDATE")
        self.panel_list.RenderPaner(data)
        self.panel_list.update()
        self.update()
        self.CreateCalendarList._update(data)
        self.CreateCalendarList.update()

class CreateCalendarUser(ft.Container):
    def __init__(self,inform_start):
        super().__init__()
        self.content = ft.Text('Uaer')

class CreateCalendarWeekday(ft.Container):
    def __init__(self,inform_start):
        super().__init__()
        self.content = ft.Text('Weekday')

