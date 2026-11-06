import flet as ft
from api.tools import Tools
from ui.style import CastomButton
import logging
from api.backend import Generator

class MyCalendar(ft.Container):
    def __init__(self,cache, inform):
        super().__init__()
        self.inform = inform
        self.cache = cache
        self.top_bar = ft.Row([ft.IconButton(ft.Icons.ARROW_RIGHT_ALT,on_click=self._home)])
        self.tools = Tools()
        list_data_save_calendar = self.tools.ReturnCalendarsData()
        self.logger = logging.getLogger(f"{__name__}.MyCalendar")
        self.PanelList = ft.ExpansionPanelList()
        
        for calend in list_data_save_calendar:
            events_in_day = [ft.Text(x['event_name']) for x in calend[2]]
            if len(events_in_day)==0:
                events_in_day = [ft.Text("Нет событий")]
            self.rows_event = ft.Row(
                        controls=[ft.Container(ft.Column([ft.Text(x['event_name']) for x in calend[2]]),padding=ft.Padding.only(left=30))],
                        expand=True,
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.START
                            )
            self.button_open = CastomButton('Открыть',on_click=self._open,size=15,padding=5,expand=True,data=calend[3])
            self.button_edit = CastomButton("Редактировать",on_click=self._edit,size = 15,padding=5,data=calend[3])
            self.button_live = CastomButton("В люимое",on_click=self._love,size = 15,padding=5, data=calend[3])
            self.logger.info(f"{calend[3],self.tools.love_calendar()}")
            if calend[3]==self.tools.love_calendar():
                
                titlecontrol = f"{calend[0]}   love"
            else: titlecontrol = f"{calend[0]}"
            self.PanelList.controls.append(
                ft.ExpansionPanel(
                header=ft.ListTile(title=ft.Text(titlecontrol)),
                content=ft.Container(
                    ft.Row([
                        ft.Column([
                            ft.Text(f"Год: {calend[1]}",size=15,weight=ft.FontWeight.BOLD),
                            ft.Text("События:",size=15,bgcolor="#2c2c2c"),
                            self.rows_event,
                            ]),
                        ft.Column([
                            self.button_edit,
                            self.button_open,
                            self.button_live
                        ],width=200)
                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),padding=ft.Padding.only(left=30)
                    )
                
                )
            )
            self.content = ft.Column([self.top_bar,self.PanelList])
    async def _open(self, e):
        # закешировать №315
        self.cache._add_value()
        await self.inform('/open', e.control.data)
        self.logger.info(e.control.data)
    async def _edit(self, e):
        await self.editdef(e.control.data)
    def _love(self, e):
        if self.tools._update_setting("love_calendar_path",e.control.data):
            None

    async def _home(self, e):
        await self.inform('/home')