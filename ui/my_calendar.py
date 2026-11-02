import flet as ft
from api.tools import Tools
import logging
class MyCalendar(ft.Container):
    def __init__(self,inform):
        super().__init__()
        list_data_save_calendar = Tools().ReturnCalendarsData()
        self.logger = logging.getLogger(f"{__name__}.MyCalendar")
        self.PanelList = ft.ExpansionPanelList()
        for calend in list_data_save_calendar:
            events_in_day = [ft.Text(x['event_name']) for x in calend[2]]
            if len(events_in_day)==0:
                events_in_day = [ft.Text("Нет событий")]
            self.PanelList.controls.append(
                ft.ExpansionPanel(
                header=ft.ListTile(title=ft.Text(f"{calend[0]}")),
                content=ft.Container(
                    ft.Column([
                        ft.Text(f"Год: {calend[1]}",size=15,weight=ft.FontWeight.BOLD),
                        ft.Text("События:",size=15,bgcolor="#2c2c2c"),
                        ft.Row(
                            controls=[ft.Container(ft.Column([ft.Text(x['event_name']) for x in calend[2]]),padding=ft.Padding.only(left=30))],
                            expand=True,
                            alignment=ft.MainAxisAlignment.START,
                            vertical_alignment=ft.CrossAxisAlignment.START)
                        ]),padding=ft.Padding.only(left=30)
                    )
                )
            )
            self.content = self.PanelList