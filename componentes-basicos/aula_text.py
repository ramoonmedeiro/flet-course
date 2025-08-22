import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLACK

    page.add(
        ft.Text("Eai")
    )

    page.add(
        ft.Icon(name=ft.Icons.ABC)
    )


ft.app(target=main)
