import flet as ft
import typing

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
