import os
import time
from tkinter.filedialog import askdirectory
from colorama import init, Fore,Back, Style
from tqdm import tqdm

init(autoreset=True)
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


caminho = askdirectory(title="Selecione uma pasta")
if not caminho:  
    print(Fore.RED + "Nenhuma pasta selecionada.")
    exit()


locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff",".heic"],
    "documentos": [".txt", ".doc", ".docx", ".pdf", ".rtf"],
    "planilhas": [".xls", ".xlsx", ".csv"],
    "apresentacoes": [".ppt", ".pptx"],
    "videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "audio": [".mp3", ".wav", ".flac", ".aac",".opus",".m4a",".ogg"],
    "compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "codigo": [".py", ".java", ".cpp", ".c", ".js", ".html", ".css"],
    "WEBP": [".webp"],
    "WEBM": [".webm"],
    "Apks": [".apk"],
    "Fontes": [".ttf",".woff",".woff2"],
    "outros": []  
}

pasta_duplicados = "duplicados"

total_arquivos = 0
for root, _, files in os.walk(caminho):
    for arquivo in files:
        if os.path.isfile(os.path.join(root, arquivo)):  
            total_arquivos += 1

print(Fore.BLUE + "======================================")
print(Fore.GREEN + f"Quantidade de arquivos: {total_arquivos}")
print(Fore.BLUE + "======================================")
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
                print(Fore.YELLOW + f"Arquivo .nomedia encontrado: {caminho_relativo}")
                print(Fore.RED + "Deletando arquivo...")
                print(Fore.CYAN + "--------------------------------------------")
                os.remove(caminho_completo)
                arquivos_deletados += 1
                pbar.update(1)
                continue

            movido = False
            for pasta, extensoes in locais.items():
                if pasta == "outros" and not movido:  
                    pasta_destino = os.path.join(caminho, pasta)
                    if not os.path.exists(pasta_destino):
                        print(Fore.GREEN + f"Pasta criada: {pasta}")
                        os.makedirs(pasta_destino)
                        pastas_criadas += 1

                    destino_arquivo = os.path.join(pasta_destino, arquivo)
                    if os.path.exists(destino_arquivo):
                        pasta_duplicados_caminho = os.path.join(caminho, pasta_duplicados)
                        if not os.path.exists(pasta_duplicados_caminho):
                            print(Fore.GREEN + f"Pasta criada: {pasta_duplicados}")
                            os.makedirs(pasta_duplicados_caminho)
                            pastas_criadas += 1
                        
                        novo_nome, foi_renomeado = gerar_nome_unico(pasta_duplicados_caminho, arquivo)
                        destino_duplicado = os.path.join(pasta_duplicados_caminho, novo_nome)
                        print(Fore.YELLOW + f"Arquivo duplicado: {caminho_relativo}")
                        print(Fore.BLUE + f"Formato: {extensao or 'sem extensão'}")
                        print(Back.MAGENTA + f"Movendo para: {pasta_duplicados}")
                        print(Fore.CYAN + "--------------------------------------------")
                        os.rename(caminho_completo, destino_duplicado)
                        arquivos_movidos += 1
                        if foi_renomeado:
                            arquivos_renomeados += 1
                    else:
                        print(Fore.GREEN + f"Arquivo encontrado: {caminho_relativo}")
                        print(Fore.BLUE + f"Formato: {extensao or 'sem extensão'}")
                        print(Fore.MAGENTA + f"Movendo para: {pasta}")
                        print(Fore.CYAN + "--------------------------------------------")
                        os.rename(caminho_completo, destino_arquivo)
                        arquivos_movidos += 1
                    movido = True
                    break
                elif extensao.lower() in extensoes:
                    pasta_destino = os.path.join(caminho, pasta)
                    if not os.path.exists(pasta_destino):
                        print(Fore.GREEN + f"Pasta criada: {pasta}")
                        os.makedirs(pasta_destino)
                    
                        pastas_criadas += 1

                    destino_arquivo = os.path.join(pasta_destino, arquivo)
                    if os.path.exists(destino_arquivo):
                        pasta_duplicados_caminho = os.path.join(caminho, pasta_duplicados)
                        if not os.path.exists(pasta_duplicados_caminho):
                            print(Fore.GREEN + f"Pasta criada: {pasta_duplicados}")
                            os.makedirs(pasta_duplicados_caminho)
                            pastas_criadas += 1
                        
                        novo_nome, foi_renomeado = gerar_nome_unico(pasta_duplicados_caminho, arquivo)
                        destino_duplicado = os.path.join(pasta_duplicados_caminho, novo_nome)
                        print(Fore.YELLOW + f"Arquivo duplicado: {caminho_relativo}")
                        print(Fore.BLUE + f"Formato: {extensao}")
                        print(Back.MAGENTA + f"Movendo para: {pasta_duplicados}")
                        print(Fore.CYAN + "--------------------------------------------")
                        os.rename(caminho_completo, destino_duplicado)
                        arquivos_movidos += 1
                        if foi_renomeado:
                            arquivos_renomeados += 1
                    else:
                        print(Fore.GREEN + f"Arquivo encontrado: {caminho_relativo}")
                        print(Fore.BLUE + f"Formato: {extensao}")
                        print(Back.MAGENTA + f"Movendo para :{pasta}" )
                        print(Fore.CYAN + "--------------------------------------------")
                        os.rename(caminho_completo, destino_arquivo)
                        arquivos_movidos += 1
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
                    print(Fore.RED + f"Removendo pasta vazia: {os.path.relpath(caminho_pasta, caminho)}")
                    os.rmdir(caminho_pasta)
                    pastas_deletadas += 1
                    removidas = True
            except OSError as e:
                print(Fore.RED + f"Erro ao tentar remover {caminho_pasta}: {e}")
    if not removidas:  
        break

# Summary
end_time = time.time()
tempo_total = end_time - start_time
print(Fore.BLUE + "======================================")
print(Back.GREEN + Fore.BLACK + "Resumo do processo")
print(Fore.BLUE + f"Tempo total: {tempo_total:.2f} segundos")
print(Fore.GREEN + f"Pastas criadas: {pastas_criadas}")
print(Fore.RED + f"Pastas deletadas: {pastas_deletadas}")
print(Fore.MAGENTA + f"Arquivos movidos: {arquivos_movidos}")
print(Fore.GREEN + f"Arquivos renomeados: {arquivos_renomeados}")
print(Fore.RED + f"Arquivos deletados: {arquivos_deletados}")
print(Fore.BLUE + "======================================")