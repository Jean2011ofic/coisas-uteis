import os
import cv2
from moviepy.video.io.VideoFileClip import VideoFileClip

# Caminho base do script
caminho_base = os.path.dirname(os.path.abspath(__file__))

# Cria pasta principal
pasta_projeto = os.path.join(caminho_base, "projeto_video")
os.makedirs(pasta_projeto, exist_ok=True)

# Caminho para pasta de frames
pasta_frames = os.path.join(pasta_projeto, "frames")
os.makedirs(pasta_frames, exist_ok=True)

# Extrai áudio
video = VideoFileClip("video.mp4")
video.audio.write_audiofile(os.path.join(pasta_projeto, "audio.mp3"))

# Extrai frames
video_cv = cv2.VideoCapture("video.mp4")
frame_count = 0
while True:
    success, frame = video_cv.read()
    if not success:
        break
    caminho_frame = os.path.join(pasta_frames, f"frame_{frame_count:04d}.png")
    cv2.imwrite(caminho_frame, frame)
    frame_count += 1

video_cv.release()

# Informações extras
duracao = video.duration
fps = video_cv.get(cv2.CAP_PROP_FPS)
tempo_por_frame = 1 / fps if fps else 0

print(f"✅ Áudio salvo em: {pasta_projeto}")
print(f"✅ {frame_count} frames salvos em: {pasta_frames}")
print(f"🎬 Duração do vídeo: {duracao:.2f} segundos")
print(f"🎞️ Tempo entre cada frame: {tempo_por_frame:.4f} segundos")