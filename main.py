" { A Clock by <Mychel/> } "


# Used libraries
from time import strftime
import os
import locale
import flet as ft


# Setting the locale to "Portuguese-Brazil"
locale.setlocale(locale.LC_ALL, 'pt_br.UTF-8')


# Creating the Application
def clock(app: ft.Page):
    "Function that allow us to create the App."

    app.title = f"Relógio do(a) {os.getlogin()}"
    app.window_width = 450
    app.window_height = 350
    app.window_resizable = False
    app.horizontal_alignment = 'center'
    app.theme_mode = 'dark'
    app.padding = 0
    app.window_title_bar_hidden = True
    app.window_always_on_top = True

    # Function to close the window by clicking on the close button
    def close_window(_):
        app.window_close()

    # Function to minimize the window by clicking on the minimize button
    def minimize_window(_):
        app.window_minimized = True
        app.update()

    # Function to change the app theme mode between dark and light
    def change_theme(_):
        if app.theme_mode == 'dark':
            app.theme_mode = 'light'
            _.control.icon = ft.icons.LIGHT_MODE
            _.control.tooltip = 'Toque para mudar o tema. Atual: light'

        elif app.theme_mode == 'light':
            app.theme_mode = 'dark'
            _.control.icon = ft.icons.DARK_MODE
            _.control.tooltip = 'Toque para mudar o tema. Atual: dark'

        app.update()

    # Function that get the current time
    def get_current_time(_):
        current_hour.value = strftime('%H:%M:%S')
        app.update()

    # Creating some variables containing "Flet Controls"
    # Current date text control
    current_date = ft.Text(
        font_family='Georgia',
        style='headlineSmall',
        color='#9932CC',
        value=strftime('%A, %d de %B de %Y')
    )

    # Current hour text control
    current_hour = ft.Text(
        font_family='Georgia',
        style='displayMedium',
        weight='bold',
        color='#9400D3'
    )

    # Window drag area control
    draggable_area = ft.Row(
        controls=[
            ft.WindowDragArea(
                content=ft.Container(
                    height=35,
                    width=435,
                    content=ft.Row(
                        alignment='spaceBetween',
                        controls=[
                            ft.Row(
                                width=90,
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.DARK_MODE,
                                        height=35,
                                        icon_size=16,
                                        on_click=change_theme,
                                        tooltip='Toque para alterar o tema. Atual: dark'
                                    ),
                                ]
                            ),
                            ft.Text(
                                value='arraste aqui para mover',
                                text_align='center',
                                font_family='Georgia',
                                opacity=0.3,
                                size=10
                            ),
                            ft.Row(
                                spacing=0,
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.MINIMIZE,
                                        on_click=minimize_window,
                                        tooltip='Minimizar janela',
                                        icon_size=16,
                                        height=35
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.CLOSE,
                                        on_click=close_window,
                                        tooltip='Fechar janela',
                                        icon_size=16,
                                        height=35
                                    )
                                ]
                            )
                        ]
                    )
                )
            )
        ]
    )

    # Adding the controls to the app window
    app.add(
        draggable_area,

        ft.Divider(),

        ft.Text(
            value='Clockaz',
            font_family='Georgia',
            style='displayLarge',
            color='#4B0082',
            weight='bold',
            italic=True,
            height=130
        ),

        current_date,

        current_hour
    )

    # Loop to get the current time without stopping
    while True:
        get_current_time(app)


ft.app(target=clock)
