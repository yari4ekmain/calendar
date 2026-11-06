import flet as ft
from api.backend import ImportGenerator, ExportGenerator
from api.tools import Tools
import logging as lg
from ui.style import CastomButton

LEN_FORMAT = [".JSON",".IMG",".CSV",".HTML",".XLSX"]
class Import(ft.Container):
    def __init__(self,cache,inform):
        super().__init__()
        self.format_imp_row = ft.Row([CastomButton(f"{LEN_FORMAT[x]}",on_click=self._valid,data =x) for x in LEN_FORMAT])

    def _valid(self,e):
        None

class Export(ft.Container):
    def __init__(self,cache,inform):
        super().__init__()
        self.format_exp_row = ft.Row([CastomButton(f"{LEN_FORMAT[x]}",on_click=self._valid,data =x) for x in LEN_FORMAT])

    def _valid(self,e):
        None

class ChoiceCalendar(ft.Container):
    def __init__(self, cache,inform):
        super().__init__()
        # ======ВРЕМЕННО
        calendars = Tools().ReturnCalendarsData()

        self.lg=lg.getLogger(f"{__name__}.ChoiceCalendar")
        self.inform = inform
        self.calendars = calendars
        self.keygrup = None
        self.radiogrup = ft.Column([])
        self.aplay_button = CastomButton("Продолжить",on_click=self._aplay)
        self.column = ft.Column(controls=[ft.Text("Выберите календарь"),ft.RadioGroup(content=self.radiogrup,on_change=self._change),self.aplay_button])
        for calendar in self.calendars:
            self.radiogrup.controls.append(
                ft.Radio(label=f"{calendar[0]}. Год {calendar[1]}",value=f"{calendar[3]}")
            )
        self.lg.info("INIT")
        self.radiogrup.controls[0].autofocus = True
        self.content = self.column
    async def _aplay(self,e):
        self.lg.info(f"APLAY {self.keygrup}")
        await self.inform()
    def _change(self, e):
        self.lg.info(f"CHANGE {e.control.value}")
        self.keygrup = e.control.value