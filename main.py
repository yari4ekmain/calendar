import time
import datetime
import os 
import flet as ft
import json
from ui.create_calendar import CreateCalendarStart, CreateCalendarDayToDay, CreateCalendarUser, CreateCalendarWeekday
VERSION = '1.1.1.1'

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "detailed": {
            # Ключевые поля для понимания "откуда упало":
            "format": "[%(asctime)s] %(levelname)s "
                      "| %(name)s "          # полное имя логгера (модуль.Класс)
                      "| %(module)s:%(funcName)s:%(lineno)d "  # файл, функция, строка
                      "| %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "detailed",
            "level": "INFO",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "app.log",
            "maxBytes": 10_000_000,
            "backupCount": 5,
            "formatter": "detailed",
            "level": "DEBUG",  # в файл можно писать всё, в консоль — только важное
        },
    },
    "root": {
        "level": "DEBUG",        
        "handlers": ["console", "file"],
    },}

import logging.config


async def main(page: ft.Page):
    # PAGE SETTING
    async def close_app(e):
        await page.window.close()
    page.title = "calend tool"
    logging.config.dictConfig(LOGGING_CONFIG)
    
    async def inform(x):
        global dataStart
        dataStart = x
        await page.push_route('/create_colendar_day_to_day')

    routes = {
        '/create_colendar_start': lambda: CreateCalendarStart(inform),
        '/create_colendar_day_to_day': lambda: CreateCalendarDayToDay(inform),
        '/create_colendar_user': lambda: CreateCalendarUser(inform),
        '/create_colendar_weekday': lambda: CreateCalendarWeekday(inform),
        '/setting': lambda: None,
        '/my_calendar': lambda: None,
    }
    appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.PALETTE),
        leading_width=60,
        actions_padding=5,
        toolbar_height=30,
        secondary=True,
        bgcolor="#181152",
        actions=[
            ft.PopupMenuButton(
                padding=10,
                content='lflf',
                key="popup",
                items=[
                    ft.PopupMenuItem(content="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        content="Checked item",
                        checked=False,
                       
                    ),
                ],
            ),
        ft.IconButton(ft.Icons.TEXT_SNIPPET,icon_size=15,),
        ft.IconButton(ft.Icons.TEXT_SNIPPET,icon_size=15),
        ft.IconButton(ft.Icons.CLOSE,icon_size=15,on_click=close_app),
        ],
        
    )
    
    def route_change(e):
        page.views.clear()
        builder = routes.get(page.route)
        if builder:
            page.views.append(ft.View(
                route=page.route,
                controls=[builder()],
                appbar=appbar
            ))
            
        page.update()
    page.on_route_change = route_change
    await page.push_route("/create_colendar_start")
    page.window.height = 700
    page.window.width = 1500
 
    page.update()





ft.run(main)
