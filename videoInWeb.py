

def gerar_embed_completo(url):
    if "watch?v=" in url:
        video_id = url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[-1].split("?")[0]
    else:
        raise ValueError("URL inválida do YouTube")

    embed_code = f'''
<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
'''
    return embed_code.strip()


import tkinter as tk

def escrever(texto):
    resultado.config(state="normal")         # Libera edição
    resultado.delete("1.0", tk.END)          # Limpa conteúdo anterior
    resultado.insert(tk.END, texto)          # Insere novo texto
    resultado.config(state="disabled")       # Bloqueia edição, mas permite copiar

def ao_clicar():
    link = entrada.get()
    escrever(gerar_embed_completo(link))

janela = tk.Tk()
janela.title("Conversor de Link(Criado por Jean-Victor)")
janela.geometry("500x300")

# Título
titulo = tk.Label(janela, text="Escreva o link para converter", font=("Arial", 16))
titulo.pack(pady=10)

# Campo de entrada
entrada = tk.Entry(janela, font=("Arial", 14), width=40)
entrada.pack(pady=10)

# Botão
botao = tk.Button(janela, text="Converter", font=("Arial", 12), command=ao_clicar)
botao.pack(pady=10)

# Campo de texto copiável
resultado = tk.Text(janela, height=4, width=50, font=("Arial", 12))
resultado.pack(pady=10)
resultado.config(state="disabled")  # Inicialmente bloqueado

janela.mainloop()