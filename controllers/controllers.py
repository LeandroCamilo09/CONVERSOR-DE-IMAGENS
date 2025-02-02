import flet as ft
from model.model import Conversor, pick_files_result, salvar_imagens, abrir_pasta

cor_red="#f81d5b"


title=ft.Row([ft.Text("Conversor de imagens!", text_align="center", style=ft.TextStyle(size=24,weight=ft.FontWeight.BOLD))],alignment="center")

selected_files = ft.Text()
container_selected_files = ft.Column([selected_files],height=100, scroll= ft.ScrollMode.ALWAYS)
selected_format = ft.Dropdown(label="Formato",
                                  options=[
                                       ft.dropdown.Option("PNG"),
                                       ft.dropdown.Option("JPEG"),
                                       ft.dropdown.Option("JPG"),
                                       ft.dropdown.Option("BMP"),
                                       ft.dropdown.Option("TIFF"),
                                       ft.dropdown.Option("TIF"),
                                       ft.dropdown.Option("RAW"),
                                       ft.dropdown.Option("WEBP"),
                                       ],width=120, border_color=cor_red, label_style=ft.TextStyle(weight=ft.FontWeight.BOLD))


lounding=ft.Text("...")
# if lambda e: salvar_imagens:
#      lounding.value = "Concluido !!"

arquivos=ft.FilePicker(on_result=lambda e: pick_files_result(event=e,files=selected_files))

arquivos_salvos= ft.FilePicker(on_result=lambda e: salvar_imagens(event=e,selected_format=selected_format.value, load=lounding))

btn_arquivos=ft.ElevatedButton("Procurar imagem", icon="IMAGE", on_click=lambda _:arquivos.pick_files(allow_multiple=True, file_type=ft.FilePickerFileType.CUSTOM, allowed_extensions=["png","jpeg","jpg","bmp","tiff", "tif", "raw", "webp"]))

btn_abrir_pasta = ft.ElevatedButton("Abrir Pasta", icon="FOLDER", on_click= lambda e: abrir_pasta(e))

btn_save=ft.ElevatedButton("Salvar imagens", icon="SAVE", on_click=lambda _:arquivos_salvos.get_directory_path())

container_btn_format=ft.Row([btn_arquivos,selected_format], alignment="center")
programa = ft.Column([title,container_btn_format,container_selected_files,lounding,btn_save,btn_abrir_pasta], horizontal_alignment= "CENTER")