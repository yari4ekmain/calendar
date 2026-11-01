import flet as ft
from api.tools import Tools

class MyCalendar(ft.Container):
    def __init__(self,inform):
        super().__init__()
        list_data_save_calendar = Tools().ReturnCalendarsData()
        self.PanelList = ft.ExpansionPanelList()
        for calend in list_data_save_calendar:
            self.PanelList.controls.append(
                ft.ExpansionPanel(
                header=ft.ListTile(title=ft.Text(f"{calend[0]}")),
                content=ft.Column([
                    ft.Text(f"Год: {calend[1]}",size=15),
                    ft.Text("События:"),
                    ft.Column([
                        ft.Text(x['event_name']) for x in calend[2]]),],alignment=ft.Alignment.CENTER_LEFT,expand=True),)
            )
            self.content = self.PanelList