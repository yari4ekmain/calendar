import flet as ft
from ui.render_list_calendar import CreateCalendarList, CreateEventList,CreateEvent
from ui.style import CastomButton
from api.backend import Generator
import logging
class CreateCalendarStart(ft.Row):
    def __init__(
            self,
            cache, 
            inform):
        super().__init__()
        self.cache = cache
        self.logger = logging.getLogger(f"{__name__}.CreateCalendarStart")
        self.inform = inform
        self.error = ft.Text("",color="#ff5e5e")
        self.input_name = ft.TextField(label="Название")
        self.input_god = ft.TextField(value=2026)
        self.aplay = CastomButton(text='Далее',on_click=self._aplay,size=15,padding=5,border_radius=5)
        self.undo = CastomButton(text="Назад",on_click=self._undo,size=15,padding=5,border_radius=5)
        self.controls = [ft.Column([
                    ft.Text('Создание календаря',size=20,weight=ft.FontWeight.BOLD),
                    self.error,
                    ft.Text("   Введите название:"),
                    ft.Container(content=self.input_name,padding=ft.Padding(15,0,0,0),width=400),

                    ft.Text("   Введите год:"),
                    ft.Container(content=self.input_god,padding=ft.Padding(15,0,0,0),width=400),
                    ft.Container(ft.Row([
                        self.aplay,
                        self.undo
                    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),width=300)
            ],expand=True,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER)]
       
        self.alignment=ft.MainAxisAlignment.CENTER
        self.expand = True
        self.logger.info("CreateCalendarStart: init")

    def _valid(self,e):
        flag = True
        if (str(self.input_name.value).replace(' ','') in ["", None]):
            self.logger.warning("NOT VOLID")
            self.input_name.color = "#7a0505"
            flag = False
        else:  self.input_name.color = "#007535"
        if (str(self.input_god.value).replace(' ','') in ["", None]):
            try:
                int(self.input_god.value)
            except TypeError as e:
                self.logger.warning(f"{e}")
            self.logger.warning("NOT VOLID")
            self.input_god.color = "#7a0505"
            flag = False
        else:  self.input_god.color = "#007535"
        self.update()
        return flag

    async def _aplay(self, e):
        if self._valid:
            self.cache._add_value('start_data',[self.input_name.value,self.input_god.value])
            await self.inform('/create_colendar_day_to_day')         

    async def _undo(self, e):
        await self.inform("/home")
    
class CreateCalendarDayToDay(ft.Container):
    def __init__(
            self,
            cache, 
            inform):
        
        super().__init__()
        self.logger = logging.getLogger(f"{__name__}.CreateCalendarDayToDay")
        self.generator = Generator()
        self.cache = cache
        self.inform = inform
        self.inform_start = self.cache._export('start_data')
        self.alignment = ft.Alignment.TOP_CENTER
        if self.cache._export('edit')==None:
            data = self.generator._generetor(self.inform_start)
        else: 
            self.logger.info(f"open: {self.cache._export('edit')}")
            data = self.generator._open(self.cache._export('edit'))
            self.cache._remuve('open')
        self.CreateCalendarList = CreateCalendarList(data)
        self.panel_list = CreateEventList(self.generator,self.CreateCalendarList)    

        self.column = ft.Column([
            self.panel_list 
            ],horizontal_alignment=ft.CrossAxisAlignment.START,alignment=ft.MainAxisAlignment.START,scroll=ft.ScrollMode.AUTO)
        self.aplay = ft.TextButton(content="Сохранить",on_click=self._aplay)
        self.undo = ft.TextButton(content="Отменить",on_click=self._undo)
        self.row_button = ft.Row([self.undo,self.aplay])
        self.content = (ft.Column([
                ft.Row([ft.Container(self.column,bgcolor="#242424",width=400,height=300),ft.Column([self.row_button,self.CreateCalendarList],expand=True)]),
                ft.Row([CreateEvent(self._addevent,self._addeventweekdayx)],expand=True)],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN))
        self.logger.info("CreateCalendarDayToDay: init")
        

    def _addevent(self, work: int = None,chill: int=None,sdvig: int=None ,event = {}):
        try:
            self._update(self.generator._addEvents(work,chill,sdvig,event))
            self.logger.info(f"CreateCalendarDayToDay: CREATE (work: {work}, chill: {chill}, sdvig: {sdvig})")
        except Exception as e:
            self.logger.error(f"_addEvent: {e}")
    def _addeventweekdayx(self, workdays:list = [], event={}):
        data = self.generator._addEventWeekdays(workdays,event)     
        self.logger.info(f"CreateCalendarDayToDay: CREATE (weekday: {workdays})")
        self._update(data)
             
    def _update(self, data):
        self.logger.info("CreateCalendarDayToDay: UPDATE")
        self.panel_list.RenderPaner(data)
        self.panel_list.update()
        self.update()
        self.CreateCalendarList._update(data)
        self.CreateCalendarList.update()

    async def _aplay(self, e):
        from api.tools import SETTING
        from time import time as tm
        self.generator._seve(SETTING["save_pach"]+"/data/"+f"{tm()}.json")
        await self.inform("/home")
    async def _undo(self, e):
        await self.inform("/home")


