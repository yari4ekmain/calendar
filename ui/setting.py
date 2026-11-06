import flet as ft
import logging as lg
from api.tools import Tools
from ui.style import CastomButton

class SettingPage(ft.Column):
    def __init__(self,inform):
        super().__init__()
        self.inform = inform
        self.tools = Tools()
        self.SETTING = self.tools.returnSETTING()
        self.input_save_calendar = ft.TextField(value=self.SETTING["save_pach"],label="Путь сохранения")
        self.aplay_button = CastomButton("Сохранить", size = 15,padding=5,on_click=self._aplay)
        self.controls = [
            self.input_save_calendar,
            self.aplay_button
        ]
    def _aplay(self,e):
        if self.tools._valid_save_path(self.input_save_calendar.value):
            self.tools._update_setting("save_pach",self.input_save_calendar.value)
            self.tools._seve_setting()
