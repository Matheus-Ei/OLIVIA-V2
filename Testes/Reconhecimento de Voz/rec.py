import speech_recognition as sr

# Crie um objeto de reconhecimento de fala
r = sr.Recognizer()

# Abra o arquivo de áudio
with sr.AudioFile(r'Reconhecimento de Voz') as source:
    # Carregue o arquivo de áudio para a memória
    audio = r.record(source)

# Configure o caminho para os arquivos de modelo acústico e de linguagem
acoustic_model_path = r'Reconhecimento de Voz\cmusphinx-pt-br-5.2'
language_model_path = r'Reconhecimento de Voz\cmusphinx-pt-br-5.2'
dictionary_path = r'Reconhecimento de Voz\br-pt.dic'

# Configure o reconhecimento de fala usando o CMUSphinx
r.recognize_sphinx(audio, acoustic_model=acoustic_model_path, language_model=language_model_path, dictionary=dictionary_path)

# Obtenha o texto reconhecido
recognized_text = r.recognize_sphinx(audio, acoustic_model=acoustic_model_path, language_model=language_model_path, dictionary=dictionary_path)

# Imprima o texto reconhecido
print(recognized_text)
