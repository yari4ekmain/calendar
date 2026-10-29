
import flet as ft

from ui.create_calendar import CreateCalendarStart, CreateCalendarDayToDay, CreateCalendarUser, CreateCalendarWeekday
from ui.home import Home
from api.tools import Tools



async def main(page: ft.Page):
    page.title = "calend tool"
    Tools().StartApp()
    import logging
        
    async def inform(route):
        await page.push_route(f'{route}')

    routes = {
        '/home': lambda: Home(inform),
        '/create_colendar_start': lambda: CreateCalendarStart(inform),
        '/create_colendar_day_to_day': lambda: CreateCalendarDayToDay(inform),
        '/create_colendar_user': lambda: CreateCalendarUser(inform),
        '/create_colendar_weekday': lambda: CreateCalendarWeekday(inform),
        '/setting': lambda: None,
        '/my_calendar': lambda: None,
    }
    drawer = ft.NavigationDrawer(
        # on_dismiss=handle_dismissal,
        # on_change=handle_change,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.Icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.Icons.PHONE,
            ),
        ],
    )

    
    def route_change(e):
        page.views.clear()
        builder = routes.get(page.route)
        if builder:
            page.views.append(ft.View(
                route=page.route,
                controls=[builder()],
                drawer=drawer
            ))
            
        page.update()
    page.on_route_change = route_change
    logging.info('MAIN START')
    await page.push_route("/home")
    page.window.height = 700
    page.window.width = 1500
 
    page.update()





ft.run(main)
