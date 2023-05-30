import vosk
import sys
import speech_recognition as sr

# Carregar o modelo de idioma do Vosk
model = vosk.Model(r'Testes\\vosk_model')
vosk.SetLogLevel(-1)

# Configurar o objeto Recognizer do Vosk
rec = vosk.KaldiRecognizer(model, 16000)

# Configurar o objeto Microphone da SpeechRecognition
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    while True:
        try:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

            # Converter o áudio em formato necessário pelo Vosk
            audio_data = audio.get_raw_data(convert_rate=16000, convert_width=2)

            # Realizar o reconhecimento de fala com o Vosk
            rec.AcceptWaveform(audio_data)
            result = rec.Result()

            # Obter o texto transcrito
            transcribed_text = result

            # Exibir o texto transcrito
            print("<<<--------------->>>")
            print(transcribed_text)
            print("<<<--------------->>>")
        except KeyboardInterrupt:
            break
