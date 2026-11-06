
import flet as ft

from ui.create_calendar import CreateCalendarStart, CreateCalendarDayToDay
from ui.my_calendar import MyCalendar
from ui.open_calendar import OpenCalendar
from ui.home import Home
from api.tools import Tools
from api.cache import Cache
from ui.import_export import Import, Export, ChoiceCalendar
from ui.setting import SettingPage

async def main(page: ft.Page):
    page.title = "calend tool"
    Tools().StartApp()
    cache = Cache()
    import logging
    path_calendar = None
    async def inform(route: str, data = None):
        nonlocal path_calendar
        path_calendar = data
        logging.info("inform")
        await page.push_route(f'{route}')

    edit_path = '/generait'
    async def open_edit(data):
        nonlocal edit_path
        edit_path = data
        logging.info(f"open_edit: {data}")
        await page.push_route("/create_colendar_day_to_day")
    routes = {
        '/home': lambda: Home(cache,inform),
        '/create_colendar_start': lambda: CreateCalendarStart(cache,inform),
        '/create_colendar_day_to_day': lambda: CreateCalendarDayToDay(cache,inform,edit_path),
        '/setting': lambda: SettingPage(cache,inform),
        '/open': lambda: OpenCalendar(cache,inform,path_calendar),
        '/my_calendar': lambda: MyCalendar(cache,inform,open_edit),#Закешировать №315
        '/import': lambda: Import(cache,inform),
        '/export': lambda: Export(cache,inform),
        '/choice_calendar': lambda: ChoiceCalendar(cache,inform)
    }
    drawer = ft.NavigationDrawer(
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
    # await page.push_route("/home")
    await page.push_route("/choice_calendar")
    page.window.height = 700
    page.window.width = 1500
    page.update()





ft.run(main)
