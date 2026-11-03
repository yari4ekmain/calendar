import flet as ft
import typing
from api.tools import Tools

class CastomButton(ft.Container):
    def __init__(
        self,
        text: str | None = None,
        size: int = 10,
        padding: int | None = None,
        bgcolor: str | None = None,
        color: str | None = None,
        border_radius: int | None = None,
        on_click: typing.Callable | None = None,
        on_hover: typing.Callable | None = None,
        data: str | int | None = None,
        expand: bool | int | None = None,
        width: int | None = None,
        height: int | None = None,
        margin: int | None = None,
        sticking: bool | None = None,
    ):
        if sticking is True:
            self.datax = "off"
            self._on_click_handler = self._click_on
        else:
            self.datax = data
            self._on_click_handler = on_click

        self._text_control = ft.Text(
            expand=expand,
            value=text,
            size=size,
            color=color,
            text_align=ft.TextAlign.CENTER,
        )

        super().__init__(
            content=self._text_control,
            alignment=ft.Alignment.CENTER,          
            border=ft.Border.all(1, "#ffffff"),    
            padding=padding,
            bgcolor=bgcolor,
            border_radius=border_radius,
            expand=expand,
            width=width,
            height=height,
            margin=margin,
            data=self.datax,
            on_click=self._on_click_handler,
            on_hover=on_hover,
            ink=True,  
        )

    def _click_on(self, e):
        e.control.bgcolor = "#082F77"
        e.control.on_click = self._click_off
        e.control.data = 'on'

    def _click_off(self, e):
        e.control.bgcolor = None
        e.control.on_click = self._click_on
        e.control.data = 'off'



class CastomLanDay(ft.Stack):
    def __init__(self):
        super().__init__()
        self.width = 150
        self.slep_grid = 1
        self.height = 350 
    def Render(self,events_day):       
        if len(events_day)!=0:
            sort_events = Tools().SortEvent(events_day)
            for event in sort_events:
                color = event[1]["event_color"]
                self.controls.append(
                    ft.Container(
                        width=self.width,
                        bgcolor=color,
                        margin=ft.Margin(top=int((self.height / (24 * 60)) * (event[2]))+10,left = 50),
                        height=int((self.height / (24 * 60)) * (event[0])),
                        
                    )
                )

        time_next_grid = 0
        grid_alig = ft.Alignment.TOP_CENTER
        for grid in range(0,25,self.slep_grid):
            cont_grid = ft.Container(content=ft.Row([ft.Text(f"{grid}:00" if len(str(grid))==2 else f"0{grid}:00"),ft.Container(bgcolor="#910000",height=2,alignment=grid_alig,width=self.width-35,)]),padding=ft.Padding.only(top=time_next_grid))
            self.controls.append(cont_grid)
            time_next_grid+=self.height / (24 / self.slep_grid)
    def _update(self, events_day=[]):
        self.controls.clear()
        self.Render(events_day)
        self.update()

class CastomColorExplanation(ft.Column):
    def __init__(self):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.START
    def Render(self,events = []):
        if len(events)!=0: 
          for event in events:
            color = event["event_color"]
            name = event["event_name"]
            obg = ft.Row([ft.Container(bgcolor=color,width=10,height=10),ft.Text(value=name)])
            self.controls.append(obg)
    def _update(self, events = []):
        self.controls.clear()
        self.Render(events)
        self.update()