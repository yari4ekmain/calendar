import time
import datetime
import os 
import flet as ft
import json

from ui.create_calendar import CreateCalendarStart, CreateCalendarDayToDay, CreateCalendarUser, CreateCalendarWeekday
VERSION = '1.1.1.1'

PAGE = None





def main(page: ft.Page):
    # PAGE SETTING
    page.title = "calend tool"

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
    page.go("/create_colendar_start")

 
    page.update()
    def inform(x):
        global dataStart
        dataStart = x
        print(dataStart)
        if x[2]==0:
            page.go('/create_colendar_day_to_day')
        elif x[2]==1:
            page.go('/create_colendar_weekday')  
        else:
            page.go('/create_colendar_user')  


    # with open('data/data.json','r') as f:
    #     data = json.load(f)
    # if data["calend"]==[]:
    #     none_calendar_my = ft.Text('У вас нет календарей')
    #     mu_calendar_page = ft.SafeArea(ft.Container(content=none_calendar_my,expand=True))
    #     PAGE = mu_calendar_page
        
    #     page.update()
    # else:
    #     None
    

ft.app(main)
