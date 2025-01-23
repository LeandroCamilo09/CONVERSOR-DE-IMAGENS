from controllers.controllers import programa,arquivos,arquivos_salvos
import flet as ft


def main(page: ft.Page):   
     page.window.width=500
     page.window.height=500
     page.theme_mode = "DARK"
     page.overlay.append(arquivos)
     page.overlay.append(arquivos_salvos)
     page.window.center()
     page.title = "Conversor de imagens_1.0"

     page.add(programa)

ft.app(target=main)