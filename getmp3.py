import os
import yt_dlp
from moviepy.audio.io.AudioFileClip import AudioFileClip

# Link do vídeo
url = "https://www.youtube.com/watch?v=zLahOd6MyYQ"

# Pasta de saída
output_folder = "audios"
os.makedirs(output_folder, exist_ok=True)

# Configurações do yt-dlp
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
    'quiet': True
}

# Baixa o áudio
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)
    title = info.get('title', 'audio')
    ext = info.get('ext', 'webm')
    input_path = os.path.join(output_folder, f"{title}.{ext}")
    output_path = os.path.join(output_folder, f"{title}.mp3")

# Converte para MP3
print(f"🎧 Convertendo {input_path} para MP3...")
audio = AudioFileClip(input_path)
audio.write_audiofile(output_path)

print(f"✅ MP3 salvo em: {output_path}")