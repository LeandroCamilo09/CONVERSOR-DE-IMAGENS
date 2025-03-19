# from controllers.controllers import programa,arquivos,arquivos_salvos
from controllers.controllers import programa, arquivos, Arquivos_salvos
import flet as ft


def main(page: ft.Page):   
     page.window.width=500
     page.window.height=500
     page.theme_mode = "DARK"
     page.overlay.append(arquivos)
     # page.window.center()
     arquivo_salvo=Arquivos_salvos(aplicativo=page)
     page.overlay.append(arquivo_salvo)
     

     page.title = "Conversor de imagens_1.0"
     p=programa(arq=arquivo_salvo)
     
     page.add(p)

ft.app(target=main)