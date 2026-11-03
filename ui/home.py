import flet as ft
from ui.render_list_calendar import CreateCalendarList
from api.backend import Generator
from ui.style import CastomButton, CastomLanDay,CastomColorExplanation
import logging
class Home(ft.Container):
    def __init__(self,inform):
        self.lg=logging.getLogger(f"{__name__}.Home")
        self.lg.info("START INIT HOME")
        self.inf = inform
        super().__init__()
        calendar = Generator()._open('data/1793718955.289867.json')
        self.castomdayevent = CastomLanDay()
        self.castomcolors = CastomColorExplanation()
        def reqvest(control):
            self.lg.info(f"reqvest {control}")
            self.castomdayevent._update(control["events"])
            self.castomcolors._update(control["events"])
            self.update()
        self.home_calendar = ft.Container(content=ft.Row([ft.Container(self.castomdayevent),self.castomcolors,CreateCalendarList(calendar,reqvest)]),expand=True)
        self.addcalendar = CastomButton(text = 'Создать календарь',size=15,padding=5,border_radius=3,on_click=self._create)
        self.my_calendar = CastomButton(text = 'Мои календари',size=15,padding=5,border_radius=3,on_click=self._my_calendr)
        self.setting = CastomButton(text = 'Настройки',size=15,padding=5,border_radius=3,on_click=None)
        self.row_button = ft.Row([self.addcalendar,self.my_calendar,self.setting],alignment=ft.MainAxisAlignment.CENTER,expand=True)
        self.content = ft.Column([self.home_calendar,self.row_button],expand=True)
        self.lg.info('INIT HOME')
    async def _create(self,e):
        await self.inf('/create_colendar_start')
    async def _my_calendr(self, e):
        await self.inf('/my_calendar')