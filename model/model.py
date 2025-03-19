from PIL import Image
import flet as ft
import os
from time import sleep
     
def pick_files_result(event,files):
          global selected_path
          selected_path = {}
          selected_path ={
                "nome":"",
                "caminho":""
                }

          files.value = (", ".join(map(lambda f: f.name, event.files)) if event.files else "Cancelled!").split(",")
          files.update()
          selected_path["nome"] = (",".join(map(lambda f: f.name, event.files))).split(",")
          selected_path["caminho"] = ",".join(map(lambda f: f.path, event.files)).split(",")

def salvar_imagens(event,selected_format,load,pb, app):
          if selected_format == None:
               load.value="Você precisa selecionar um formato de arquivo!"
               load.update()
          if event.path == None:
               load.value="Canceled..."
               load.update()
          else:
               load.value="Convertendo imagens, por favor aguarde!"
               load.update()
               if pb.visible==False:
                     pb.visible=True
               try:
                    global pasta_caminho
                    path = event.path if event.path else "Cancelled!"
                    pasta_caminho=path
                    cont=1
                    for nome, caminho in zip(selected_path["nome"],selected_path["caminho"]):
                         
                         with Image.open(caminho) as img:
                              # Verificar o modo da imagem e converter se necessário
                              if img.mode == "RGBA" and selected_format.upper() in ["JPEG","JPG"]:
                                   img = img.convert("RGB")  # Remove transparência

                              imagem=Conversor(nome,caminho,selected_format,path)
                              imagem.converter_imagem()
                         if nome:
                              pb.value=cont/len(selected_path["nome"])
                              cont+=1
                              sleep(0.1)
                              app.update()
                         print(f"Nome: {str(nome).split('.')[0]} \nCaminho: {caminho} \nTipo de arquivo: {selected_format} \nNovo caminho: {path}\\{nome}.{selected_format} \n")
                         print("================")


                    load.value="CONCLUIDO!"
                    load.update()
               except Exception as img_error:
                    load.value=f"Erro ao processar imagem: {img_error}"
                    load.update()
                    print(f"Erro ao processar imagem: {img_error}")
               

def abrir_pasta(event):
      os.startfile(pasta_caminho)

class Conversor():
     def __init__(self,input_name,input_path,output_format,output_path):
          self.input_name = input_name
          self.input_path = input_path
          self.output_format = output_format
          self.output_path=output_path


     # Função para converter imagens
     def converter_imagem(self):
          try:
               # Abrir a imagem
               with Image.open(self.input_path) as img:
                    # Verificar o modo da imagem e converter se necessário
                    if img.mode == "RGBA" and self.output_format.upper() in ["JPEG","JPG"]:
                         img = img.convert("RGB")  # Remove transparência
                    
                    nome_arquivo = f"{self.output_path}\\{str (self.input_name).split('.')[0]}.{str (self.output_format).lower()}"
                    
                    # Salvar a imagem no novo formato
                    img.save(nome_arquivo)

                    print(f"Imagem convertida com sucesso: {self.input_path}")
          except (Exception,TypeError,ValueError) as error:
               print(f"Erro ao converter imagem: {error}")


           