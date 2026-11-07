import flet as ft
from ui.render_list_calendar import CreateCalendarList
from api.backend import Generator, today
from ui.style import CastomLanDay,CastomColorExplanation, CastomTopBar
import logging


class OpenCalendar(ft.Container):
    def __init__(self,
                 cache, 
                 inf,
                 generator = Generator()):
        self.lg=logging.getLogger(f"{__name__}.OpenCalendar")
        self.lg.info("START INIT OpenCalendar")
        self.inf = inf
        self.cache = cache
        super().__init__()
        self.generator = generator
        self.calendar = self.generator._open(self.cache._export("open"))
        self.today = today()
        self.castomdayevent = CastomLanDay()
        self.castomcolors = CastomColorExplanation()    
        self.topbar = CastomTopBar(self.inf)   
        if self.calendar["old"]==self.today[0]:
            day = self.today[2]
            mes =self.today[1]
        else:
            day, mes= 1, 1
        events = self.generator._getEvent(mes,day)
        self.castomcolors.Render(events)
        self.castomdayevent.Render(events)
        self.topbar.Render(self.today,name=self.calendar["name"])
        self.home_calendar = ft.Container(content=ft.Row([ft.Container(self.castomdayevent),self.castomcolors,CreateCalendarList(self.calendar,self.reqvest)]),expand=True)
        
        self.content = ft.Column([self.topbar,self.home_calendar],expand=True)
        self.lg.info('INIT OpenCalendar')

    def reqvest(self,control):
        self.lg.info(f"reqvest {control}")
        self.castomdayevent._update(control["events"])
        self.castomcolors._update(control["events"])
        self.update()