import flet as ft
from ui.style import CastomButton
class Aplay(ft.Container):
    def __init__(self, cache, inform):
        super().__init__()
        self.alignment = ft.Alignment.TOP_CENTER
        self.cache = cache
        self.lebel = ft.Text(str(self.cache._export('aplay_labal')))
        self.info = ft.Text(str(self.cache._export('aplay_info')))
        self.icon = ft.Icon(icon=ft.Icons.CHECK,size=140)
        self.cache._remuve("aplay_labal")
        self.cache._remuve("aplay_info")
        self.inform = inform
        self.inhome = CastomButton("На главную",on_click=self._home, height=150)
        self.content = ft.Column([
            self.lebel,
            self.icon,
            self.info,
            self.inhome
        ],alignment=ft.MainAxisAlignment.CENTER)
    async def _home(self,e):
        await self.inform("/home")