import time
import datetime
import os 
import flet as ft
import json
VERSION = '1.1.1.1'

PAGE = None

def main(page: ft.Page):
    # PAGE SETTING
    page.title = "calend tool"
    global PAGE


    # BAR NAVIGEISION
    def reopen_page(e):
        print(navigation_bar.selected_index)
        if navigation_bar.selected_index==0:
            return
        elif navigation_bar.selected_index==1:
            
            page.remove(PAGE)

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
        ],on_change=reopen_page,selected_index=2
    )
    page.navigation_bar = navigation_bar

    # MY CALENDAR
    with open('data/data.json','r') as f:
        data = json.load(f)
    if data["calend"]==[]:
        none_calendar_my = ft.Text('У вас нет календарей')
        mu_calendar_page = ft.SafeArea(ft.Container(content=none_calendar_my,expand=True))
        PAGE = mu_calendar_page
        
        page.update()
    else:
        None

    # CREATE CALENDAR 
    def tupe_calendar(e):
        print(calendar_type_input.selected_index)

        input_day_work = ft.TextField(label="Дней работы")
        input_day_not_work = ft.TextField(label="Дней отдыха")
        sdvig = ft.TextField(label="Сдвиг")

        cont_input_day_work = ft.Container(input_day_work,width=150)
        cont_input_day_not_work = ft.Container(input_day_not_work,width=150)
        cont_sdvig = ft.Container(sdvig,width=150)

        day_1 = ft.TextButton("Пн")
        day_2 = ft.TextButton("Вт")
        day_3 = ft.TextButton("Ср")
        day_4 = ft.TextButton("Чт")
        day_5 = ft.TextButton("Пт")
        day_6 = ft.TextButton("Сб")
        day_7 = ft.TextButton("Вс")

        index = calendar_type_input.selected_index
        if len(column_create_calendar.controls)==7:
            column_create_calendar.controls.append(ft.Text(' '))

        if index ==0:
            data = ft.Row([cont_input_day_work,cont_input_day_not_work,cont_sdvig])
            column_create_calendar.controls.pop(-1)
            column_create_calendar.controls.append(data)
            column_create_calendar.update()
        elif index ==1:
            data = ft.Row([day_1,day_2,day_3,day_4,day_5,day_6,day_7])
            column_create_calendar.controls.pop(-1)
            column_create_calendar.controls.append(data)
            column_create_calendar.update()
        else:
            column_create_calendar.controls.pop(-1)
            column_create_calendar.update()
    
    calendar_type_input = ft.CupertinoSlidingSegmentedButton(
        selected_index=2,
        controls=[
            ft.Text('Дней через дней'),
            ft.Text("По дням недели"),
            ft.Text("Пользавательский")
        ],on_change=tupe_calendar
    )
    input_name = ft.TextField(label="Название")
    input_god = ft.TextField(value=2026)
    column_create_calendar = ft.Column([
                ft.Text('Создание календаря',size=20),

                ft.Text("   Введите название:"),
                ft.Container(content=input_name,padding=ft.Padding(15,0,0,0),width=400),

                ft.Text("   Введите год:"),
                ft.Container(content=input_god,padding=ft.Padding(15,0,0,0),width=400),

                ft.Text("   Выберите тип:"),
                ft.Container(content=calendar_type_input,padding=ft.Padding(15,0,0,0))


            ])
    create_calendar_page = ft.SafeArea(
        ft.Container(
            content=column_create_calendar,
            expand=True)
        )
    page.add(create_calendar_page)

    # ============ page create ==========
    calend_list_btn_row = ft.Row(controls=[],wrap=True,width=600,alignment=ft.alignment.center)
    calend_btn_cont = ft.Container(content=calend_list_btn_row,margin=ft.Margin(100,0,100,0))
    left_bt_create = ft.Button('<')
    right_bt_create = ft.Button('>')

    border_btn_ = ft.border.all(
        ft.BorderSide(color="#F54927", width=1)
)
    for x in range(1,32):
        calend_list_btn_row.controls.append(ft.Container(ft.Button(f'{x}',expand=True),border=border_btn_,width=60,height=60))
        

    page_new_calend = ft.Column([
        ft.Text("Новый календарь"),
        ft.Row([
                ft.Text("Введите год:"),
                ft.TextField(label='Год')
            ]),
            ft.Row([ft.Container(left_bt_create),ft.Container(calend_btn_cont),right_bt_create],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,)
        ])
    


ft.app(main)
