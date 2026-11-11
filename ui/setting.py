import flet as ft
import logging as lg
from api.tools import Tools
from ui.style import CastomButton,CastomTopBar

class SettingPage(ft.Column):
    def __init__(self,cache, inform):
        super().__init__()
        self.cache = cache
        self.inform = inform
        self.tools = Tools()
        self.label = ft.Text('Настойки',size=20,weight=ft.FontWeight.BOLD)
        self.Exit_button = CastomButton('Назад',on_click=self._exit,width=70)
        self.SETTING = self.tools.returnSETTING()
        self.input_save_calendar = ft.TextField(value=self.SETTING["save_pach"],label="Путь сохранения")
        self.aplay_button = CastomButton("Сохранить", size = 15,padding=5,on_click=self._aplay)
        self.path_setting_label = ft.Text("Настройки путей",size=15)
        self.path_setting = ft.Container(
            ft.Row([
                self.input_save_calendar
            ]),padding=ft.Padding(left=10)
        )
        self.controls = [
            self.Exit_button,
            self.label,
            self.path_setting_label,
            self.path_setting,
            self.aplay_button
        ]
    def _aplay(self,e):
        if self.tools._valid_save_path(self.input_save_calendar.value):
            self.tools._update_setting("save_pach",self.input_save_calendar.value)
            self.tools._seve_setting()
    async def _exit(self, e):
        await self.inform('/home')