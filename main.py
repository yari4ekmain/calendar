
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
    async def inform(route: str):
        logging.info("inform")
        await page.push_route(f'{route}')


    routes = {
        '/home': lambda: Home(cache,inform),
        '/create_colendar_start': lambda: CreateCalendarStart(cache,inform),
        '/create_colendar_day_to_day': lambda: CreateCalendarDayToDay(cache,inform),
        '/setting': lambda: SettingPage(cache,inform),
        '/open': lambda: OpenCalendar(cache,inform),
        '/my_calendar': lambda: MyCalendar(cache,inform),
        '/import': lambda: Import(cache,inform),
        '/export': lambda: Export(cache,inform),
        '/choice_calendar': lambda: ChoiceCalendar(cache,inform)
    }
    

    
    def route_change(e):
        page.views.clear()
        builder = routes.get(page.route)
        if builder:
            page.views.append(ft.View(
                route=page.route,
                controls=[builder()]
            ))
            
        page.update()
    page.on_route_change = route_change
    logging.info('MAIN START')
    await page.push_route("/home")
    page.window.height = 700
    page.window.width = 1500
    page.update()





ft.run(main)
