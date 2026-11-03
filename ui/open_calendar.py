import flet as ft
from ui.render_list_calendar import CreateCalendarList
from api.backend import Generator
from ui.style import CastomLanDay,CastomColorExplanation
import logging


class OpenCalendar(ft.Container):
    def __init__(self,reqvest,path_calendar):
        self.lg=logging.getLogger(f"{__name__}.OpenCalendar")
        self.lg.info("START INIT OpenCalendar")
        self.inf = reqvest
        super().__init__()
        calendar = Generator()._open(path_calendar)
        self.castomdayevent = CastomLanDay()
        self.castomcolors = CastomColorExplanation()
        def reqvest(control):
            self.lg.info(f"reqvest {control}")
            self.castomdayevent._update(control["events"])
            self.castomcolors._update(control["events"])
            self.update()
        self.home_calendar = ft.Container(content=ft.Row([ft.Container(self.castomdayevent),self.castomcolors,CreateCalendarList(calendar,reqvest)]),expand=True)
        
        self.content = ft.Column([self.home_calendar],expand=True)
        self.lg.info('INIT OpenCalendar')