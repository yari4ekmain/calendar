import flet as ft
from ui.render_list_calendar import CreateCalendarList
from api.backend import Generator
from ui.style import CastomButton
class Home(ft.Container):
    def __init__(self,inform):
        self.inf = inform
        super().__init__()
        calendar = Generator()._open('data/dataTEST.json')
        self.home_calendar = ft.Container(content=CreateCalendarList(calendar=calendar),expand=True)
        self.addcalendar = CastomButton(text = 'Создать календарь',size=15,padding=5,border_radius=3,on_click=self._create)
        self.my_calendar = CastomButton(text = 'Мои календари',size=15,padding=5,border_radius=3,on_click=None)
        self.setting = CastomButton(text = 'Настройки',size=15,padding=5,border_radius=3,on_click=None)
        self.row_button = ft.Row([self.addcalendar,self.my_calendar,self.setting],alignment=ft.MainAxisAlignment.CENTER,expand=True)
        self.content = ft.Column([self.home_calendar,self.row_button],expand=True)
    async def _create(self,e):
        await self.inf('/create_colendar_start')