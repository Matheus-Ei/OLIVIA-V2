import pyttsx3
from pydub import AudioSegment
from pydub.playback import play

texto = "Olá mundo!"

# Inicializa o mecanismo de síntese de voz
engine = pyttsx3.init()
# Sintetiza o texto
engine.save_to_file(texto, "data.mp3")
engine.runAndWait()
# Carrega o áudio gerado
audio = AudioSegment.from_wav("data.mp3")
# Ajusta o volume (por exemplo, 6 dB para aumentar em 6 decibéis)
volume_adjustment = 6
audio = audio + volume_adjustment

# Reproduz o áudio com o volume aumentado
play(audio)
