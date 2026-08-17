import time
import datetime
import os 
import flet as ft
import json
VERSION = '1.1.1.1'

PAGE = None

def main(page: ft.Page):
    global PAGE
    
    def page_create_calend():
        text = ft.Text("123")
    page.title = "calend tool"
    with open('data/data.json','r') as f:
        data = json.load(f)
    text = ft.Text('e ')
    if data["calend"]==[]:
        text = ft.Text('У вас нет календарей')
    def reopen_page(e):
        print(navigation_bar.selected_index)
        if navigation_bar.selected_index==0:
            return
        elif navigation_bar.selected_index==1:
            page_create_calend()
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
        ],on_change=reopen_page,
    )
    page.navigation_bar = navigation_bar
    page_my_calendar = ft.SafeArea(content=ft.Column(controls=[text]))
    PAGE = page_my_calendar
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
    
    page.add(page_new_calend)

ft.app(main)
