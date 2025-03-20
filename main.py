from controllers.controllers import programa, arquivos, Arquivos_salvos
import flet as ft


def main(page: ft.Page):   
     page.window.width=500
     page.window.height=500
     page.theme_mode = "DARK"
     page.overlay.append(arquivos)
     page.window.center()
     arquivo_salvo=Arquivos_salvos(aplicativo=page)
     page.overlay.append(arquivo_salvo)
     

     page.title = "Conversor de imagens_1.0"
     app=programa(arq=arquivo_salvo)
     
     page.add(app)

ft.app(target=main)