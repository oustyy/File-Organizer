import os
import time
import tkinter as tk
from tkinter.filedialog import askdirectory
from colorama import init, Fore, Back, Style
from tqdm import tqdm

init(autoreset=True)

# ASCII art welcome message
def display_welcome_message():
    print(Style.BRIGHT + Fore.MAGENTA + r"""
_____________________________________________________________________________________________________      
   ___      ___                                                                                    
 /'___\ __ /\_ \                                                         __                        
/\ \__//\_\\//\ \      __             ___   _ __    __      __      ___ /\_\  ____      __   _ __  
\ \ ,__\/\ \ \ \ \   /'__`\ _______  / __`\/\`'__\/'_ `\  /'__`\  /' _ `\/\ \/\_ ,`\  /'__`\/\`'__\
 \ \ \_/\ \ \ \_\ \_/\  __//\______\/\ \L\ \ \ \//\ \L\ \/\ \L\.\_/\ \/\ \ \ \/_/  /_/\  __/\ \ \/ 
  \ \_\  \ \_\/\____\ \____\/______/\ \____/\ \_\\ \____ \ \__/.\_\ \_\ \_\ \_\/\____\ \____\\ \_\ 
   \/_/   \/_/\/____/\/____/         \/___/  \/_/ \/___L\ \/__/\/_/\/_/\/_/\/_/\/____/\/____/ \/_/ 
                                                    /\____/                                        
                                                    \_/__/                                         
_____________________________________________________________________________________________________
    """)
    print(Style.BRIGHT + Fore.GREEN + "Type 'start' to open folder selection dialog.")
    print(Style.BRIGHT + Fore.GREEN + "Type 'path' to manually enter a folder path.")
    print(Style.BRIGHT + Fore.YELLOW + "Type 'exit' to quit the application.\n")

def gerar_nome_unico(caminho_destino, nome_arquivo):
    base, extensao = os.path.splitext(nome_arquivo)
    contador = 1
    novo_nome = nome_arquivo
    while os.path.exists(os.path.join(caminho_destino, novo_nome)):
        novo_nome = f"{base}_{contador}{extensao}"
        contador += 1
    return novo_nome, contador > 1  

start_time = time.time()

pastas_criadas = 0
pastas_deletadas = 0
arquivos_movidos = 0
arquivos_renomeados = 0
arquivos_deletados = 0
pastas_encontradas = 0
arquivos_imagem = 0
arquivos_documentos = 0
arquivos_planilhas = 0
arquivos_apresentacoes = 0
arquivos_videos = 0
arquivos_audio = 0
arquivos_compactados = 0
arquivos_codigo = 0
arquivos_webp = 0
arquivos_webm = 0
arquivos_apks = 0
arquivos_fontes = 0
arquivos_outros = 0

# Display welcome message and wait for user command
display_welcome_message()
while True:
    user_input = input().strip().lower()
    if user_input == 'start':
        print(Style.BRIGHT + Fore.CYAN + "Attempting to open folder selection dialog...")
        print(Fore.YELLOW + "If the dialog does not appear, please enter the folder path manually.")
        try:
            root = tk.Tk()
            root.withdraw()  # Hide the main Tkinter window
            time.sleep(0.5)  # Brief delay to ensure system readiness
            caminho = askdirectory(title="Selecione uma pasta")
            root.destroy()  # Destroy the Tkinter root after selection
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + f"Error opening folder selection dialog: {e}")
            print(Style.BRIGHT + Fore.YELLOW + "Please enter the folder path manually (e.g., C:/Users/YourName/Folder):")
            caminho = input().strip()
        break
    elif user_input == 'path':
        print(Style.BRIGHT + Fore.YELLOW + "Please enter the folder path (e.g., C:/Users/YourName/Folder):")
        caminho = input().strip()
        break
    elif user_input == 'exit':
        print(Style.BRIGHT + Fore.RED + "Application terminated by user.")
        exit()
    else:
        print(Style.BRIGHT + Fore.RED + "Invalid input. Please type 'start', 'path', or 'exit'.")

if not caminho or not os.path.isdir(caminho):  
    print(Style.BRIGHT + Fore.RED + "Nenhuma pasta válida selecionada.")
    exit()

# Exibir o diretório selecionado e pedir confirmação
print(Style.BRIGHT + Fore.BLUE + f"Diretório selecionado: {caminho}")
print(Style.BRIGHT + Fore.RED + f"(!!!!A aplicação vai apagar todas as pastas vazias do diretório selecionado após a organização!!!!)")
print(Style.BRIGHT + Fore.YELLOW + "Deseja iniciar o processo? (Digite 'yes' para confirmar ou 'no' para cancelar): ")
confirmacao = input().strip().lower()
if confirmacao != 'yes':
    print(Style.BRIGHT + Fore.RED + "Processo cancelado pelo usuário.")
    exit()

locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".heic"],
    "documentos": [".txt", ".doc", ".docx", ".pdf", ".rtf"],
    "planilhas": [".xls", ".xlsx", ".csv"],
    "apresentacoes": [".ppt", ".pptx"],
    "videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "audio": [".mp3", ".wav", ".flac", ".aac", ".opus", ".m4a", ".ogg"],
    "compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "codigo": [".py", ".java", ".cpp", ".c", ".js", ".html", ".css"],
    "WEBP": [".webp"],
    "WEBM": [".webm"],
    "Apks": [".apk"],
    "Fontes": [".ttf", ".woff", ".woff2"],
    "outros": []  
}

pasta_duplicados = "duplicados"

total_arquivos = 0
for root, dirs, files in os.walk(caminho):
    pastas_encontradas += 1
    for arquivo in files:
        if os.path.isfile(os.path.join(root, arquivo)):  
            total_arquivos += 1

print(Style.BRIGHT + Fore.BLUE + "======================================")
print(Style.BRIGHT + Fore.GREEN + f"Quantidade de arquivos: {total_arquivos}")
print(Style.BRIGHT + Fore.GREEN + f"Quantidade de pastas: {pastas_encontradas}")
print(Style.BRIGHT + Fore.BLUE + "======================================")

with tqdm(total=total_arquivos, desc="Processando arquivos", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]") as pbar:
    for root, _, files in os.walk(caminho):
        for arquivo in files:
            if root == os.path.join(caminho, pasta_duplicados) or any(os.path.join(caminho, pasta) == root for pasta in locais):
                pbar.update(1)
                continue

            nome, extensao = os.path.splitext(arquivo)
            caminho_completo = os.path.join(root, arquivo)

            if not os.path.isfile(caminho_completo):
                pbar.update(1)
                continue

            caminho_relativo = os.path.relpath(caminho_completo, caminho)

            if arquivo.lower() == ".nomedia":
                print(Style.BRIGHT + Fore.YELLOW + f"Arquivo .nomedia encontrado: {caminho_relativo}")
                print(Style.BRIGHT + Fore.RED + "Deletando arquivo...")
                print(Style.BRIGHT + Fore.CYAN + "--------------------------------------------")
                os.remove(caminho_completo)
                arquivos_deletados += 1
                pbar.update(1)
                continue

            movido = False
            for pasta, extensoes in locais.items():
                if pasta == "outros" and not movido:  
                    pasta_destino = os.path.join(caminho, pasta)
                    if not os.path.exists(pasta_destino):
                        print(Style.BRIGHT + Fore.GREEN + f"Pasta criada: {pasta}")
                        os.makedirs(pasta_destino)
                        pastas_criadas += 1

                    destino_arquivo = os.path.join(pasta_destino, arquivo)
                    if os.path.exists(destino_arquivo):
                        pasta_duplicados_caminho = os.path.join(caminho, pasta_duplicados)
                        if not os.path.exists(pasta_duplicados_caminho):
                            print(Style.BRIGHT + Fore.GREEN + f"Pasta criada: {pasta_duplicados}")
                            os.makedirs(pasta_duplicados_caminho)
                            pastas_criadas += 1
                        
                        novo_nome, foi_renomeado = gerar_nome_unico(pasta_duplicados_caminho, arquivo)
                        destino_duplicado = os.path.join(pasta_duplicados_caminho, novo_nome)
                        print(Style.BRIGHT + Fore.YELLOW + f"Arquivo duplicado: {caminho_relativo}")
                        print(Style.BRIGHT + Fore.BLUE + f"Formato: {extensao or 'sem extensão'}")
                        print(Style.BRIGHT + Fore.MAGENTA + f"Movendo para: {pasta_duplicados}")
                        print(Style.BRIGHT + Fore.CYAN + "--------------------------------------------")
                        os.rename(caminho_completo, destino_duplicado)
                        arquivos_movidos += 1
                        if foi_renomeado:
                            arquivos_renomeados += 1
                    else:
                        print(Style.BRIGHT + Fore.GREEN + f"Arquivo encontrado: {caminho_relativo}")
                        print(Style.BRIGHT + Fore.BLUE + f"Formato: {extensao or 'sem extensão'}")
                        print(Style.BRIGHT + Fore.MAGENTA + f"Movendo para: {pasta}")
                        print(Style.BRIGHT + Fore.CYAN + "--------------------------------------------")
                        os.rename(caminho_completo, destino_arquivo)
                        arquivos_movidos += 1
                    arquivos_outros += 1
                    movido = True
                    break
                elif extensao.lower() in extensoes:
                    pasta_destino = os.path.join(caminho, pasta)
                    if not os.path.exists(pasta_destino):
                        print(Style.BRIGHT + Fore.GREEN + f"Pasta criada: {pasta}")
                        os.makedirs(pasta_destino)
                        pastas_criadas += 1

                    destino_arquivo = os.path.join(pasta_destino, arquivo)
                    if os.path.exists(destino_arquivo):
                        pasta_duplicados_caminho = os.path.join(caminho, pasta_duplicados)
                        if not os.path.exists(pasta_duplicados_caminho):
                            print(Style.BRIGHT + Fore.GREEN + f"Pasta criada: {pasta_duplicados}")
                            os.makedirs(pasta_duplicados_caminho)
                            pastas_criadas += 1
                        
                        novo_nome, foi_renomeado = gerar_nome_unico(pasta_duplicados_caminho, arquivo)
                        destino_duplicado = os.path.join(pasta_duplicados_caminho, novo_nome)
                        print(Style.BRIGHT + Fore.YELLOW + f"Arquivo duplicado: {caminho_relativo}")
                        print(Style.BRIGHT + Fore.BLUE + f"Formato: {extensao}")
                        print(Style.BRIGHT + Fore.MAGENTA + f"Movendo para: {pasta_duplicados}")
                        print(Style.BRIGHT + Fore.CYAN + "--------------------------------------------")
                        os.rename(caminho_completo, destino_duplicado)
                        arquivos_movidos += 1
                        if foi_renomeado:
                            arquivos_renomeados += 1
                    else:
                        print(Style.BRIGHT + Fore.GREEN + f"Arquivo encontrado: {caminho_relativo}")
                        print(Style.BRIGHT + Fore.BLUE + f"Formato: {extensao}")
                        print(Style.BRIGHT + Fore.MAGENTA + f"Movendo para: {pasta}")
                        print(Style.BRIGHT + Fore.CYAN + "--------------------------------------------")
                        os.rename(caminho_completo, destino_arquivo)
                        arquivos_movidos += 1
                   
                    if pasta == "imagens":
                        arquivos_imagem += 1
                    elif pasta == "documentos":
                        arquivos_documentos += 1
                    elif pasta == "planilhas":
                        arquivos_planilhas += 1
                    elif pasta == "apresentacoes":
                        arquivos_apresentacoes += 1
                    elif pasta == "videos":
                        arquivos_videos += 1
                    elif pasta == "audio":
                        arquivos_audio += 1
                    elif pasta == "compactados":
                        arquivos_compactados += 1
                    elif pasta == "codigo":
                        arquivos_codigo += 1
                    elif pasta == "WEBP":
                        arquivos_webp += 1
                    elif pasta == "WEBM":
                        arquivos_webm += 1
                    elif pasta == "Apks":
                        arquivos_apks += 1
                    elif pasta == "Fontes":
                        arquivos_fontes += 1
                    movido = True
                    break
            pbar.update(1)

while True:
    removidas = False
    for root, dirs, files in os.walk(caminho, topdown=False):
        for pasta in dirs:
            caminho_pasta = os.path.join(root, pasta)
            try:
                if not os.listdir(caminho_pasta):  
                    print(Style.BRIGHT + Fore.RED + f"Removendo pasta vazia: {os.path.relpath(caminho_pasta, caminho)}")
                    os.rmdir(caminho_pasta)
                    pastas_deletadas += 1
                    removidas = True
            except OSError as e:
                print(Style.BRIGHT + Fore.RED + f"Erro ao tentar remover {caminho_pasta}: {e}")
    if not removidas:  
        break

# Resumo
end_time = time.time()
tempo_total = end_time - start_time
print(Style.BRIGHT + Fore.BLUE + "======================================")
print(Style.BRIGHT +  Fore.MAGENTA  + "Resumo do processo")
print(Style.BRIGHT + Fore.BLUE + f"Tempo total: {tempo_total:.2f} segundos")
print(Style.BRIGHT + Fore.CYAN + f"Pastas encontradas: {pastas_encontradas}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos encontrados: {total_arquivos}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos de imagem: {arquivos_imagem}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos de documentos: {arquivos_documentos}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos de planilhas: {arquivos_planilhas}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos de apresentações: {arquivos_apresentacoes}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos de vídeos: {arquivos_videos}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos de áudio: {arquivos_audio}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos compactados: {arquivos_compactados}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos de código: {arquivos_codigo}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos WEBP: {arquivos_webp}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos WEBM: {arquivos_webm}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos de Apks: {arquivos_apks}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos de fontes: {arquivos_fontes}")
print(Style.BRIGHT + Fore.GREEN + f"Arquivos outros: {arquivos_outros}")
print(Style.BRIGHT + Fore.RED + f"Pastas deletadas: {pastas_deletadas}")
print(Style.BRIGHT + Fore.RED + f"Arquivos deletados: {arquivos_deletados}")
print(Style.BRIGHT + Fore.YELLOW + f"Pastas criadas: {pastas_criadas}")
print(Style.BRIGHT + Fore.YELLOW + f"Arquivos movidos: {arquivos_movidos}")
print(Style.BRIGHT + Fore.YELLOW + f"Arquivos renomeados: {arquivos_renomeados}")
print(Style.BRIGHT + Fore.BLUE + "======================================")