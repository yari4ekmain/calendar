import time
import datetime
import os 
import flet as ft
import json
Version = '0.1'
qq = None
ni = None
day = False
bbv = False
disabled_v = False
sat = 0
smn = False
sat_liv = None
sd = 0
ra = 0
st2 = None
banner = False
import requests
st5 = []
st1 = None
event = []



 


if os.listdir(os.getcwd()).count('data')==0:
    os.mkdir('data')
# if os.listdir(os.getcwd()).count('info.json')==0:
#     f = open('info.json')
#     json.dump({"Version": Version},f)
def a1(tupee =1):
    global qq
    global ni
    global day
    global bbv
    global sat
    global sd
    global sat_liv
    global smn
    tim = f'{int(time.time())}_{sat}_{sd}_{sat_liv}_{qq}_{smn}'
    file = open(f'data/text{ni}_{tim}.html','w', encoding='utf-8')
    if int(ni) % 4 == 0:
        z = ['''<!DOCTYPE html>,
    
    <html lang="ru">,
    <head>,
        <meta charset="UTF-8">,
        <meta name="viewport" content="width=device-width, initial-scale=1.0">,
        <title>КАЛЕНДАРЬ</title>,
        <style>,
            td {background-color: #cbffdc;},
            h1 {margin: 0 10px ;},
            h2 {text-align: left;margin-left: 3px;},
            .v4_31 {background-color: rgb(255 255 255);},
            .v6_31 {background-color: rgb(255 255 255);},
            .v9_31 {background-color: rgb(255 255 255);},
            .v11_31 {background-color: rgb(255 255 255);},
            .v2_31 {background-color: rgb(255 255 255);},
            .v2_30 {background-color: rgb(255 255 255);},
        
        
        </style>,
    </head>,
    <body>,
        <table border="0.5px"; align="left";>,
            <thear>,
                <th><h1>Январь</h1></th>,
                <th><h1>Февраль</h1></th>,
                <th><h1>Март</h1></th>,
                <th><h1>Апрель</h1></th>,
                <th><h1>Май</h1></th>,
                <th><h1>Июнь</h1></th>,
                <th><h1>Июль</h1></th>,
                <th><h1>Август</h1></th>,
                <th><h1>Сентябрь</h1></th>,
                <th><h1>Октябрь</h1></th>,
                <th><h1>Ноябрь</h1></th>,
                <th><h1>Декабрь</h1></th>,
            </thear>,''']
    else:
        z = ['''<!DOCTYPE html>,
    
    <html lang="ru">,
    <head>,
        <meta charset="UTF-8">,
        <meta name="viewport" content="width=device-width, initial-scale=1.0">,
        <title>КАЛЕНДАРЬ</title>,
        <style>,
            td {background-color: #cbffdc;},
            h1 {margin: 0 10px ;},
            h2 {text-align: left;margin-left: 3px;},
            .v4_31 {background-color: rgb(255 255 255);},
            .v6_31 {background-color: rgb(255 255 255);},
            .v9_31 {background-color: rgb(255 255 255);},
            .v11_31 {background-color: rgb(255 255 255);},
            .v2_31 {background-color: rgb(255 255 255);},
            .v2_30 {background-color: rgb(255 255 255);},
        .v2_29 {background-color: rgb(255 255 255);},
        </style>,
    </head>,
    <body>,
            
        <table border="0.5px"; align="center";>,
            <thear>,
                <th><h1>Январь</h1></th>,
                <th><h1>Февраль</h1></th>,
                <th><h1>Март</h1></th>,
                <th><h1>Апрель</h1></th>,
                <th><h1>Май</h1></th>,
                <th><h1>Июнь</h1></th>,
                <th><h1>Июль</h1></th>,
                <th><h1>Август</h1></th>,
                <th><h1>Сентябрь</h1></th>,
                <th><h1>Октябрь</h1></th>,
                <th><h1>Ноябрь</h1></th>,
                <th><h1>Декабрь</h1></th>,
            </thear>,''']
    for i in range(0,31):
        z.append('<tr>')
        y = i+1
        for x in range(0, 12):
            l = x+1
            if i ==29:
                if x == 1:
                        z.append (f"""
                        <td class="v{l}_{y}"><h2> </h2></td>,""" )
                else:
                    z.append (f"""
                        <td class="v{l}_{y}"><h2>{y}</h2></td>,""" )
            elif i ==28:
                if x == 1 and ni % 4 !=0:
                        z.append (f"""
                        <td class="v{l}_{y}"><h2> </h2></td>,""" )
                else:
                    z.append (f"""
                        <td class="v{l}_{y}"><h2>{y}</h2></td>,""" )
            elif i == 30:
                if x == 1:
                    z.append (f"""
                        <td class="v{l}_{y}"><h2> </h2></td>,""" )
                elif x == 3:
                    z.append (f"""
                            <td class="v{l}_{y}"><h2> </h2></td>,""" )
                elif x == 5:
                    z.append (f"""
                            <td class="v{l}_{y}"><h2> </h2></td>,""" )
                elif x == 8:
                    z.append (f"""
                            <td class="v{l}_{y}"><h2> </h2></td>,""" )
                elif x == 10:
                    z.append (f"""
                            <td class="v{l}_{y}"><h2> </h2></td>,""" )
                elif x == 12:
                    z.append (f"""
                            <td class="v{l}_{y}"><h2> </h2></td>,""" )
                else:
                    z.append (f"""
                        <td class="v{l}_{y}"><h2>{y}</h2></td>,""" )
                    
            else:
                z.append (f"""
                        <td class="v{l}_{y}"><h2>{y}</h2></td>,""" )


        z.append('</tr>')
    z.append('''    </table>,''')
    
    
    q = str(f'1 January, {ni}')
    q = time.strptime( q, "%d %B, %Y")
    z.append('<style>,')
    pp = str(q.tm_wday)
    print(pp)
    q = q.tm_wday
    qwe = str(q)
    lq = 1
    xx = 1
    listt = ['Пн','Вт','Ср','Чт','Пт','Сб','Вс']
    lak = sat
    lak = lak-sd
    xl = []
    if event != []:
        for ev in event:
            q1 = str(ev[1]).replace(f'{ni}_','').replace('08','8').replace('01','1').replace('02','').replace('2','').replace('03','3').replace('04','4').replace('05','5').replace('06','6').replace('07','7').replace('09','9')
            xl.append(f'.v{q1}'+'{background-color: #5db2f8;},')
            xl.append(f'.v{q1}::after '+'{'+f' content: "-{ev[0]}"; '+'},')
    for a in range(0,399):
        
        if smn == True:
            if lak <1:
                lak = sat
            if lak >sat_liv :
                z.append(f'.v{lq}_{xx}'+'{background-color: #fc800d;},')
            
    
            if day == True:
                z.append(f'.v{lq}_{xx}::after '+'{'+f' content: "{listt[q]}"; '+'},')
            if (q == 5 or q==6) and bbv == True:
                z.append(f'.v{lq}_{xx}'+'{background-color: #4af744;},')
            if (sat_liv < lak) and (bbv == True) and (q == 5 or q==6):
                z.append(f'.v{lq}_{xx}'+'{background-color: #f5f23b;},')
            lak-=1
            
        else:
            if qq != None:
                if qq.count(qwe) == 1:
                    z.append(f'.v{lq}_{xx}'+'{background-color: #fc800d;},')
            
            if day == True:
                z.append(f'.v{lq}_{xx}::after '+'{'+f' content: "{listt[q]}"; '+'},')

            if (q == 5 or q==6) and bbv == True:
                z.append(f'.v{lq}_{xx}'+'{background-color: #4af744;},')
            if qq != None:
                if (qq.count(qwe) == 1) and (bbv == True) and (q == 5 or q==6):
                    z.append(f'.v{lq}_{xx}'+'{background-color: #f5f23b;},')

        tupee = 1
        q += 1
        qwe = str(q)
        if tupee == 1:
            if q > 6:
                q = 0
                qwe = '0'
            else:
                None
        xx +=1 
        if xx == 32 and lq == 1:#
            xx = 1
            lq = 2 
        if xx == 29 and lq == 2 and ni% 4!=0 :
            xx = 1
            lq = 3
        elif xx == 30 and lq == 2 :
            xx = 1
            lq = 3
        if xx == 32 and lq == 3:#
            xx = 1
            lq = 4 
        if xx == 31 and lq == 4:#
            xx = 1
            lq = 5
        if xx == 32 and lq == 5:#
            xx = 1
            lq = 6 
        if xx == 31 and lq == 6:#
            xx = 1
            lq = 7
        if xx == 32 and lq == 7:#
            xx = 1
            lq = 8 
        if xx == 32 and lq == 8:#
            xx = 1
            lq = 9
        if xx == 31 and lq == 9:#
            xx = 1
            lq = 10
        if xx == 32 and lq == 10:#
            xx = 1
            lq = 11
        if xx == 31 and lq == 11:#
            xx = 1
            lq = 12
        if xx == 32 and lq == 12:#
            break
    z.append(xl)
    z.append('</style>, </body>,</html>')

    
    
    file.write(str(z).replace('\\n','').replace(',','\n').replace("'",'').replace('[','').replace(']',''))
    file.close()
    os.startfile(f'data\\text{ni}_{tim}.html')
    ni = None
    qq = None


def main(page: ft.Page):
    global banner, event
    global st1
    def close_banner(e):
        page.close(banner1)
        page.update()
    def button_clicked(e):
        global ni, day, qq, bbv, smn, sat_liv, sat, sd

         
        xc=0
        if c2.value == True:
            smn = False
            if 1000 < int(asd.value) < 5000:
                ni = int(asd.value) 
                asd.border_color="#48f31d"
                page.update()
            else:
                asd.border_color='#f31d1d'
                page.update()
                return
            if q0q.value == True:
                qq = f'{qq}0'
            if q1.value == True:
                qq = f'{qq}1'
            if q2.value == True:
                qq = f'{qq}2'
            if q3.value == True:
                qq = f'{qq}3'
            if q4.value == True:
                qq = f'{qq}4'
            if q5.value == True:
                qq = f'{qq}5'
            if q6.value == True:
                qq = f'{qq}6'
        else:
             
             
            sat = int(l1.value) + int(l2.value)
            sat_liv = int(l2.value)
            smn = True
            if 1000 < int(asd.value) < 5000:
                ni = int(asd.value) 
                asd.border_color="#48f31d"
                page.update()
            else:
                asd.border_color='#f31d1d'
                page.update()
                return
        page.update()
        if q7.value == True:
            day = True
        else:
            day = False
        if q8.value == True:
            bbv = True
        else:
            bbv = False

        ni = int(asd.value) 
        if c1.value == True:
            sd = int(l3.value)
            if int(l3.value) > int(l1.value) + int(l2.value):
                l1.border_color='#f31d1d'
                l2.border_color='#f31d1d'
                l3.border_color='#f31d1d'
                page.update()
                
            else:
                l1.border_color="#1df32f"
                l2.border_color="#1df32f"
                l3.border_color="#24f31d"
                page.update()
                xc += 1
        if event != []:
            for ev in event:
                d = str(ev[1]).split('_')
                if d[0] != str(ni):
                    asd.label = 'Год не совпадает с Мероприятиями'
                    asd.border_color='#f31d1d'
                    page.update()
                    return
                else:
                    asd.border_color="#24f31d"
                    asd.label = 'Год'
                    page.update()

        a1(ni)
    def add_event(e):
        global st5, event, st1
        
         

        if l4.value == None or l4.value == '':
            l4.border_color = "#f3361d"
            l4.label = 'это поле не может быть пустым'
            page.update()
            return
        else:
            l4.border_color = "#1df364"
            l4.label = 'Краткое название'
            page.update()
        if DateP.text == "Выбрать дату":
            DateP.color = "#f3361d"
            page.update()
            return
        else:
            DateP.color = "#24f31d"
            page.update()
  
        # exp1 = ft.ExpansionPanel(
        #     bgcolor="#8972ee",
        #     header=ft.ListTile(title=ft.Text(f"Название:{l4.value}\nДата:{DateP.text}"), bgcolor="#8972ee"))
        # exp1.content = ft.ListTile(
        #     title=ft.Text(f"Название:{l4.value}\nДата:{DateP.text}" ),
        #     subtitle=ft.IconButton(ft.Icons.OPEN_IN_NEW, data=exp1),
        #     trailing=ft.IconButton(ft.Icons.DELETE, data=exp1),
        #     bgcolor="#8972ee"
        # )
        
        # page.update()
        # st5.append(exp1)
        # panel = ft.ExpansionPanelList(
        # controls=st5,
        # expand=True  # или False, в зависимости от нужного поведения
        
        # )        


         
                
        def delete_container(container_to_delete):
            """Удаляет конкретный контейнер из st5 и обновляет интерфейс"""
            global st5, st1, event
            
            if container_to_delete in st5:
                print(st5.index(container_to_delete))
                del event[int(st5.index(container_to_delete))]
                st5.remove(container_to_delete)
                
                update_interface()  # Функция для полного обновления интерфейса
        

        def update_interface():
            """Полностью пересобирает и обновляет интерфейс"""
            global st1

            
            # Создаем колонку с актуальным списком st5 или пустой контейнер
            if st5:
                ss = ft.Column(controls=st5)  # Используем controls для явного указания
            else:
                ss = ft.Container()
            
            # Создаем новый st1 с актуальными данными
            new_st1 = ft.Row([rail,banner1,ft.VerticalDivider(width=1),ft.Column([
                ft.Text(value="Создать календарь",size=20, weight="bold"),
                asd,
                c1,
                cn3,
                c2,
                cn2,   
                t4,cn5,
                t2,cn4,
                ss,
                ft.ElevatedButton(text="Создать календарь", on_click=button_clicked)
                ],alignment=ft.MainAxisAlignment.START,scroll=ft.ScrollMode.AUTO)],expand=True)
            
            # Заменяем старый st1 на новый
            try:
                page.remove(st1)
            except ValueError:  # Если st1 уже удален или не существует
                pass
            page.add(new_st1)
            st1 = new_st1  # Обновляем глобальную ссылку
            page.update()

        # Внутри функции add_event
        container = ft.Container(
            content=ft.Row([]),
            bgcolor="#453d6b",
            padding=8,
            border_radius=10,
            margin=5
        )
        te = ft.Text(value=f'Название:{l4.value}\nДата:{DateP.text}')
        event.append([l4.value,DateP.text])
        bt2 = ft.IconButton(
            ft.Icons.DELETE,
            on_click=lambda e: delete_container(container),  # Теперь delete_container определена выше
            data=container  # Передаем ссылку на контейнер
        )
        container.content.controls.extend([te, bt2])  # Добавляем элементы в контейнер
        st5.append(container)

        update_interface()  # Обновляем интерфейс после добавления
        print(event)
    
    def b12(e):
        global disabled_v
        if c1.value == True:
            c2.value=False
            q0q.disabled=True
            q1.disabled=True
            q2.disabled=True
            q3.disabled=True
            q4.disabled=True
            q5.disabled=True
            q6.disabled=True
            l1.disabled=False
            l2.disabled=False
            l3.disabled=False


            page.update()
    def b21(e):
        global disabled_v
        if c2.value == True:
            c1.value = False
            
            q0q.disabled=False
            q1.disabled=False
            q2.disabled=False
            q3.disabled=False
            q4.disabled=False
            q5.disabled=False
            q6.disabled=False
            l1.disabled=True
            l2.disabled=True
            l3.disabled=True
            page.update()
    def a3(e):
        try:
            l3.label = 'сдвиг max: '+str(int(l1.value) + int(l2.value))
            page.update()
        except:
            None
    asd = ft.TextField(label="Год",value='2025',bgcolor='#21293073')
    q0q = ft.Checkbox(adaptive=True, label="Понидельник")
    q1=ft.Checkbox(adaptive=True, label="Вторник", value=False)
    q2=ft.Checkbox(adaptive=True, label="Среда", value=False)
    q3=ft.Checkbox(adaptive=True, label="Четверг", value=False)
    q4=ft.Checkbox(adaptive=True, label="Пятница", value=False)
    q5=ft.Checkbox(adaptive=True, label="Субота", value=False)
    q6=ft.Checkbox(adaptive=True, label="Васкресение", value=False)
    q7=ft.Checkbox(adaptive=True, label="Подписать дни недели", value=False)
    q8=ft.Checkbox(adaptive=True, label="Подписать выходные дни", value=False)
    l1 = ft.TextField(label="Количество рабочих дней",disabled=True)
    l2 = ft.TextField(label="Количество выходных",on_click=a3,disabled=True)
    l3 = ft.TextField(label="сдвиг",on_change=a3,disabled=True,value=0)
    l4 = ft.TextField(label="Краткое название",max_length=6)
    t1 = ft.Text(value='-')
    t2 = ft.Text(value='Добавить Мероприятиe',size=20,weight="bold")
    t4 = ft.Text(value='Дополнительные функции',size=20,weight="bold")
    t3 = ft.Text(value='Укажите дату и название мероприятия (максимум 6 букв) для внесения в календарь', theme_style=ft.TextThemeStyle.LABEL_MEDIUM)
    bt1 = ft.ElevatedButton(text="Добавить", on_click=add_event,on_long_press=print(event))
    
    banner1 = ft.Banner(
        bgcolor=ft.Colors.AMBER_100,
        leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.AMBER, size=40),
        content=ft.Text(
            value="Oops, there were some errors while trying to delete the file. What would you like to do?",
            color=ft.Colors.BLACK,
        ),
        actions=[
            ft.TextButton(
                text="Обновить", on_click=close_banner
            ),
            ft.TextButton(
                text="Не обновлять", on_click=close_banner
            ),

        ],
    )
  
    c1 = ft.CupertinoSwitch(
            label="Режим смен",
            value=False, on_change=b12
        )
    c2 = ft.CupertinoSwitch(
            label="Недельный режим",
            value=True, on_change=b21
        )
    def handle_change(e):
        DateP.text = str(e.control.value).replace("00:00:00",'').replace('-','_')
        page.update()


        

    DateP = ft.ElevatedButton(
            text = "Выбрать дату",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=1000, month=10, day=1),
                    last_date=datetime.datetime(year=5000, month=10, day=1),
                    on_change=handle_change,
                    
                )
            ),
        )
    
     
    
    row01 = ft.Row([l1,t1,l2,l3], alignment=ft.MainAxisAlignment.CENTER)
    row0 = ft.Row([q0q,q1,q2,q3], alignment=ft.MainAxisAlignment.CENTER)
    row1 = ft.Row([q4,q5,q6], alignment=ft.MainAxisAlignment.CENTER)
    row3 = ft.Row([q7,q8], alignment=ft.MainAxisAlignment.CENTER)
    row4 = ft.Row([DateP,l4,bt1], alignment=ft.MainAxisAlignment.CENTER)
    cn2 = ft.Container(ft.Column([row0,row1]),margin=3,bgcolor='#21293073',padding=7,border_radius=10)
    cn3 = ft.Container(row01,margin=3,bgcolor='#21293073',padding=7,border_radius=10)
    cn4 = ft.Container(ft.Column([t3,row4]),margin=3,bgcolor='#21293073',padding=7,border_radius=10)
    cn5 = ft.Container(row3,margin=3,bgcolor='#21293073',padding=7,border_radius=10)
    def st(e,q):
        print(2222)
        os.startfile(f'data\\{q}')
        page.update()
    def dl(e,q):
        os.remove(f'data\\{q}')
        page.remove(st2)
        page.update()
        page.add(st2)
        page.update()
    def rails(e):
        global ra, st2

        if rail.selected_index == 1 and ra!=1:
            if ra == 0:
                ax=1
                page.remove(st1)
                ss = os.listdir('data')
                st4 = []
                for s in ss:
                    q=s
                    ax +=1
                    if ax%2==1:
                        bgcolor = "#8972ee"
                    else:
                        bgcolor ="#512afa"
                    s = s.replace('text','').replace('.html','')
                    s = s.split('_')
                    if s[6] == "True":
                        d = f'Посменный {int(s[2])-int(s[4])} через {s[4]}'
                    else:
                        g = []
                        listt = ['Пн','Вт','Ср','Чт','Пт','Сб','Вс']
                        for b in range(0,7):
                            if s[5].count(f'{b}'):
                                g.append(listt[b])
                        d = f'Недельный {g}'


                    exp = ft.ExpansionPanel(
                        bgcolor=bgcolor,
                        header=ft.ListTile(title=ft.Text(f"Panel {s[0]}"), bgcolor=bgcolor),
                    )
# 2022_1757865315_0_0_None_None4      f'{int(time.time())}_{sat}_{sd}_{sat_liv}_{qq}'
                    exp.content = ft.ListTile(
                        title=ft.Text(f"календарь на {s[0]} г.\nДата создания:{time.ctime(float(s[1]))}\nТип: {d}" ),
                        subtitle=ft.IconButton(ft.Icons.OPEN_IN_NEW, on_click=lambda e, q=q: st(e, q), data=exp,),
                        trailing=ft.IconButton(ft.Icons.DELETE, data=exp, on_click=lambda e, q=q: dl(e, q)),
                        bgcolor=bgcolor,
                    )
                    st4.append(exp)
                expansion_panel_list = ft.ExpansionPanelList(
                controls=st4,
                expand=True  # или False, в зависимости от нужного поведения
            )
        
        # Создаем контейнер для всего содержимого
                
                content_column = ft.Column(
                controls=[expansion_panel_list],
                scroll=ft.ScrollMode.AUTO,  # Добавляем прокрутку если много элементов
                expand=True
        )       
                print(8888)
                
                st2 = ft.Row(
                    controls=[
                        rail,
                        ft.VerticalDivider(width=1),
                        ft.Column(
                            controls=[
                                ft.Text(value="Мои календари", size=20, weight="bold"),
                                content_column,
                            ],
                            expand=True
                        )
                    ],
                    expand=True
                )
                page.add(st2)
                page.update()
                

                    
                ra =1
        if rail.selected_index == 0 and ra!=0:
            if ra == 1:
                page.remove(st2)
                page.add(st1)
            ra =0
        page.update()
            

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=10,
        min_extended_width=40,

        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.ADD_BOX_OUTLINED,
                selected_icon=ft.Icons.ADD_BOX,
                label="Новый", 
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.BOOKMARK_BORDER),
                selected_icon=ft.Icon(ft.Icons.BOOKMARK),
                label="Созданые",
            ),

        ],
        on_change=rails,
    )
    
    st1 = ft.Row([rail,banner1,ft.VerticalDivider(width=1),ft.Column([
        ft.Text(value="Создать календарь",size=20, weight="bold"),
        asd,
        c1,
        cn3,
        c2,
        cn2,   
        t4,cn5,
        t2,cn4,
        ft.ElevatedButton(text="Создать календарь", on_click=button_clicked)
        ])],expand=True,alignment=ft.MainAxisAlignment.START,scroll=ft.ScrollMode.AUTO)

    
    



    page.update()
    rail,
    ft.VerticalDivider(width=1),
    page.add(st1)
    if banner == True:
        page.open(banner1)
        page.update()    
    
    
   

ft.app(main)
