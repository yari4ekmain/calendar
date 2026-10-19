import time
import datetime
import os 
import flet as ft
import json
from ui.create_calendar import CreateCalendarStart, CreateCalendarDayToDay, CreateCalendarUser, CreateCalendarWeekday
VERSION = '1.1.1.1'

PAGE = None





async def main(page: ft.Page):
    # PAGE SETTING
    page.title = "calend tool"
    async def inform(x):
        global dataStart
        dataStart = x
        print(dataStart)
        if x[2]==0:
            await page.push_route('/create_colendar_day_to_day')
        elif x[2]==1:
            await page.push_route('/create_colendar_weekday')  
        else:
            await page.push_route('/create_colendar_user')  
    routes = {
        '/create_colendar_start': lambda: CreateCalendarStart(inform),
        '/create_colendar_day_to_day': lambda: CreateCalendarDayToDay(inform),
        '/create_colendar_user': lambda: CreateCalendarUser(inform),
        '/create_colendar_weekday': lambda: CreateCalendarWeekday(inform),
        '/setting': lambda: None,
        '/my_calendar': lambda: None,
    }
    navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icon(
                    ft.Icons.SEVEN_K_PLUS,
                    badge=ft.Badge(small_size=10),
                ),
                label="Сохранённые колендари",
                
                
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.NEW_RELEASES,
                label="Новый календарь",
            ),
            ft.NavigationBarDestination(
                label='Настройки',
                icon=ft.Icon(
                    ft.Icons.SETTINGS
                )
            ),
        ],selected_index=2
    )
    def route_change(e):
        page.views.clear()
        builder = routes.get(page.route)
        if builder:
            page.views.append(ft.View(
                route=page.route,
                controls=[builder()],
                navigation_bar=navigation_bar
            ))
            
        page.update()
    page.on_route_change = route_change
    await page.push_route("/create_colendar_start")

 
    page.update()





ft.run(main)
