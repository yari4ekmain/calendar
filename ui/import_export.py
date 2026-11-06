import flet as ft
from api.backend import ImportGenerator, ExportGenerator
import logging as lg
from ui.style import CastomButton

LEN_FORMAT = [".JSON",".IMG",".CSV",".HTML",".XLSX"]
class Import(ft.Container):
    def __init__(self):
        super().__init__()
        self.format_imp_row = ft.Row([CastomButton(f"{LEN_FORMAT[x]}",on_click=self._valid,data =x) for x in LEN_FORMAT])

    def _valid(self,e):
        None

class Export(ft.Container):
    def __init__(self):
        super().__init__()
        self.format_exp_row = ft.Row([CastomButton(f"{LEN_FORMAT[x]}",on_click=self._valid,data =x) for x in LEN_FORMAT])

    def _valid(self,e):
        None