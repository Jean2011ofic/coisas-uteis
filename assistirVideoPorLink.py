import tkinter as tk
from pytube import YouTube
import os
import yt_dlp
import threading
import io
import io
import contextlib
baixado = False
def escrever(texto):
    resultado.config(state="normal")         # Libera edição
    resultado.delete("1.0", tk.END)          # Limpa conteúdo anterior
    resultado.insert(tk.END, texto)          # Insere novo texto
    resultado.config(state="disabled")       # Bloqueia edição, mas permite copiar
def aparecer():
    botao2.pack(pady=10)
yt_path = ""
def ao_clicar():
    thread = threading.Thread(target=baixar_video)
    thread.start()

def delete(path):
    try:
        os.remove(path)
    except Exception as e:
        print(f"Erro ao deletar o arquivo: {e}")

def baixar_video():
        


    global  yt_path, baixado
    import yt_dlp

    if baixado:
        delete(yt_path)
        baixado = False
    baixado = True
    info = "baixando video. Isso pode levar alguns minutos..."
    resultado.config(text=info)

    link = entrada.get()

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': 'video.mp4',
        'quiet': True,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=True)
        titulo = info_dict.get('title', 'Sem título')
        duracao = info_dict.get('duration', 0)
        info = f"Título: {titulo} Duração: {duracao} segundos"
        resultado.config(text=info)
        yt_path = ydl.prepare_filename(info_dict)
        aparecer()






def rodar_video():
    os.startfile(yt_path)

janela = tk.Tk()
janela.title("Assistir videos bloqueados(Criado por Jean-Victor)")
janela.geometry("500x300")
janela.state('zoomed')
print("Quem ler e muito gay kkkk")
print("Desenvolvido por Jean-Victor")
# Título
titulo = tk.Label(janela, text="Escreva o link para converter", font=("Arial", 16))
titulo.pack(pady=10)

# Campo de entrada
entrada = tk.Entry(janela, font=("Arial", 14), width=40)
entrada.pack(pady=10)

# Botão
botao = tk.Button(janela, text="Converter", font=("Arial", 12), command=ao_clicar)
botao.pack(pady=10)


resultado = tk.Label(janela, text="", font=("Arial", 12))
resultado.pack(pady=10)

botao2 = tk.Button(janela, text="Voce quer rodar esse video", font=("Arial", 12), command=rodar_video)



janela.mainloop()