import flet as ft
from api.tools import Tools
import logging as lg
from api.formatcore import json_to_ics
from api.calendarcore import Generator
from ui.style import CastomButton

LEN_FORMAT = [".ICS",".JSON",".IMG",".CSV",".HTML",".XLSX"]
class Import(ft.Container):
    def __init__(self,cache,inform):
        super().__init__()
        None
    def _valid(self,e):
        None

class Export(ft.Container):
    def __init__(self,cache,inform):
        super().__init__()
        self.cache =cache
        self.inform = inform
        labal = ft.Text("Выберите формат")
        self.format_exp_row = ft.Row([CastomButton(x,on_click=self._valid,data =x) for x in LEN_FORMAT],alignment=ft.MainAxisAlignment.CENTER)
        self.exit = CastomButton("Назад",expand=True)
        self.info_text = ft.Text('')
        self.column = ft.Column([labal,self.format_exp_row,self.info_text,self.exit])
        self.content= self.column
    async def _valid(self,e):
        if e.control.data != '.ICS':
            self.info_text.value =  "Извените только формат .ics"
        else:
            self.file_name = str(self.cache._export("export")).split('/')[-1].replace('json','ics')
            self.save_path = await ft.FilePicker().save_file(file_name=self.file_name)
            self.calendar = Generator()._open(self.cache._export("export"))
            if json_to_ics(self.calendar,self.save_path.replace('.ics','')):
                self.cache._add_value('aplay_info',f'Фаил {self.file_name} успешно сохранён')
                await self.inform('/aplay')
            


class ChoiceCalendar(ft.Container):
    def __init__(self, cache,inform):
        super().__init__()
        self.cache = cache
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
        self.cache._add_value('export',self.keygrup)
        await self.inform('/export')
    def _change(self, e):
        self.lg.info(f"CHANGE {e.control.value}")
        self.keygrup = e.control.value