# Imports
from wave import Error
import speech_recognition as sr
from datetime import datetime
import random
import sys
import openai
import subprocess
import webbrowser
import os
import time
import pyodbc
import threading
import pyautogui
import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
import keyboard






# Classes Criadas
import Classes.voices.Voices
import Classes.reproduzir_som.reproduzir_som
import Classes.ReconhecimentoFacial.ReconhecimentoFacial
import Classes.spotfy.Spotfy
import Classes.reproduzir_gif.reproduzir_gif
import Classes.senhas.senhas
import Classes.prev_tempo.clima
import Classes.env_email.env_email
import Classes.notificacoes.notificacoes
import Classes.keylogger.keylogger





# Pre-Definições de Váriaveis
audio_tratado = ""
retorno = ""





def main():
    global label_user, label_jarvis, button
    global audio_tratado, text_edit

    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("Janela com GIF Animado")
    window.setWindowState(window.windowState() | QtCore.Qt.WindowFullScreen)

    # Define a cor de fundo como preto
    palette = window.palette()
    palette.setColor(window.backgroundRole(), QColor(0, 0, 0))
    window.setPalette(palette)

    # Mostra o GIF do centro da tela
    gif = QLabel(window)
    movie = QMovie(r"Interface\Graficos\centro.gif")
    gif.setMovie(movie)
    movie.start()
    window_frame = window.frameGeometry()
    center_point = QDesktopWidget().availableGeometry().center()
    window_frame.moveCenter(center_point)
    window.move(window_frame.topLeft())
    gif.setAlignment(Qt.AlignCenter)
    gif.setGeometry(0, 0, window_frame.width(), window_frame.height())


    # Mostra o GIF da imagem da assitente girando
    imagem_girando = QLabel(window)
    imagem_girando.setGeometry(1550, 480, 700, 700)
    movie_girando = QMovie(r"Interface\Graficos\Pi-Slices.gif")
    imagem_girando.setMovie(movie_girando)
    movie_girando.start()


    # Mostra o GIF da imagem topografica
    imagem_topografica = QLabel(window)
    imagem_topografica.setScaledContents(True)
    imagem_topografica.setFixedSize(250, 350)
    imagem_topografica.setGeometry(1650, 50, 700, 700)
    movie_topo = QMovie(r"Interface\Graficos\Tumblr.gif")
    imagem_topografica.setMovie(movie_topo)
    movie_topo.start()


    # Mostra o GIF do qrcode
    imagem_qrcode = QLabel(window)
    imagem_qrcode.setScaledContents(True)
    imagem_qrcode.setFixedSize(300, 300)
    imagem_qrcode.setGeometry(0, 500, 700, 700)
    movie_qrcode = QMovie(r"Interface\Graficos\necessary disorder_ Photo.gif")
    imagem_qrcode.setMovie(movie_qrcode)
    movie_qrcode.start()
    
    # Mostra o GIF do planets
    imagem_planets = QLabel(window)
    imagem_planets.setScaledContents(True)
    imagem_planets.setFixedSize(300, 300)
    imagem_planets.setGeometry(0, 750, 700, 700)
    movie_planets = QMovie(r"Interface\Graficos\AK KAO on Behance.gif")
    imagem_planets.setMovie(movie_planets)
    movie_planets.start()

    # Mostra o GIF do gravidade
    imagem_gravidade = QLabel(window)
    imagem_gravidade.setScaledContents(True)
    imagem_gravidade.setFixedSize(300, 300)
    imagem_gravidade.setGeometry(17, 50, 700, 700)
    movie_gravidade = QMovie(r"Interface\Graficos\Space Oddity.gif")
    imagem_gravidade.setMovie(movie_gravidade)
    movie_gravidade.start()

    # Mostra o GIF do tenis da nike
    imagem_tenis = QLabel(window)
    imagem_tenis.setScaledContents(True)
    imagem_tenis.setFixedSize(300, 200)
    imagem_tenis.setGeometry(10, 350, 700, 700)
    movie_tenis = QMovie(r"Interface\Graficos\CypherAudio 03.gif")
    imagem_tenis.setMovie(movie_tenis)
    movie_tenis.start()

    # Mostra o GIF das letras
    imagem_letras = QLabel(window)
    imagem_letras.setScaledContents(True)
    imagem_letras.setFixedSize(200, 200)
    imagem_letras.setGeometry(1700, 400, 700, 700)
    movie_letras = QMovie(r"Interface\Graficos\Accept & Forget.gif")
    imagem_letras.setMovie(movie_letras)
    movie_letras.start()

    # Mostra o GIF das do audio
    imagem_audio = QLabel(window)
    imagem_audio.setScaledContents(True)
    imagem_audio.setFixedSize(640, 360)
    imagem_audio.setGeometry(620, 830, 700, 700)
    movie_audio = QMovie(r"Interface\Graficos\صوتية-موجات-المدة.gif")
    imagem_audio.setMovie(movie_audio)
    movie_audio.start()

    # Crie um QLabel
    label_user = QLabel('...', window)
    # Habilitar a quebra de linha automática
    label_user.setWordWrap(True)
    label_user.setAlignment(Qt.AlignCenter)
    font = QFont("Courier New", 12)  # Fonte Arial com tamanho 12
    label_user.setFont(font)
    # Criar uma instância de QPalette
    palette = QPalette()
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    label_user.setPalette(palette)
    # Definir tamanho fixo para o rótulo
    label_user.setFixedSize(300, 300)
    # Configure a posição do QLabel
    label_user.move(580, 0)
    label_user.show()

    # Crie um QLabel
    label_jarvis = QLabel('...', window)
    # Habilitar a quebra de linha automática
    label_jarvis.setWordWrap(True)
    label_jarvis.setAlignment(Qt.AlignCenter)
    font = QFont("Courier New", 12)  # Fonte Arial com tamanho 12
    label_jarvis.setFont(font)
    # Criar uma instância de QPalette
    palette = QPalette()
    # Definir a cor do texto para branco
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    # Definir a paleta do QLabel
    label_jarvis.setPalette(palette)
    # Definir tamanho fixo para o rótulo
    label_jarvis.setFixedSize(300, 300)
    # Configure a posição do QLabel
    label_jarvis.move(980, 0)
    label_jarvis.show()


    # Caixa de texto
    text_edit = QTextEdit(window)
    text_edit.setGeometry(780, 800, 300, 100)
    # Estilo para a caixa de texto
    style_sheet = """
        QTextEdit {
            background-color: #030202; /* Fundo cinza escuro */
            color: white; /* Texto branco */
            border: 1px solid white; /* Borda branca */
            font-family: Arial; /* Fonte */
            font-size: 12px; /* Tamanho da fonte */
        }
    """
    text_edit.setStyleSheet(style_sheet)
    
    def vall():
        texto = text_edit.toPlainText()
        print(texto)
        return texto

    # Botão
    button = QPushButton("Enviar", window)
    button.setGeometry(880, 920, 100, 30)
    button.clicked.connect(vall)
    # Estilo para o botão
    style_sheet = """
        QPushButton {
            background-color: #030202; /* Fundo cinza escuro */
            color: white; /* Texto branco */
            border: 1px solid white; /* Borda branca */
            font-family: Courier New; /* Fonte */
            font-size: 12px; /* Tamanho da fonte */
        }
        QPushButton:hover {
            background-color: #333333; /* Fundo cinza médio quando o mouse passa por cima */
        }
    """
    button.setStyleSheet(style_sheet)

    window.show()
    sys.exit(app.exec())







# Função principal de back-end
def code():
    global audio_tratado
    global retorno
    global label_user, label_jarvis, button


    # Cria o reconhecedor de voz e o leitor de texto automatizado
    print("<Criando reconhecedor de voz>")
    r = sr.Recognizer()
    print("<Leitor de texto automatizado criado>")


    # Define a Localização no tempo(Horas)
    def horario():
        global hora, minutos, segundos, Dia_da_semana, Mes_do_ano, Ano
        tempo=datetime.now() 
        hora = int(tempo.strftime("%H"))
        minutos = int(tempo.strftime("%M"))
        segundos = tempo.strftime("%S")
        Dia_da_semana = tempo.strftime("%A")
        Mes_do_ano = tempo.strftime("%B")
        Ano = tempo.strftime("%Y")

    print("<Conectando com o banco de dados>")
    # Definir a string de conexão com o banco de dados do Access
    conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=Banco_de_dados\jar.accdb;'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("<Banco de dados conectado>")



    # Função para consultas na tabela perguntas no banco de dados
    def consulta_db(funcao):
        try:
            # Executar uma consulta
            cursor.execute('SELECT perg FROM perguntas WHERE func = '+"'"+funcao+"';")
            # Recuperar os resultados da consulta
            rows = cursor.fetchall()
            for row in rows:
                roww = str(row[0])
                if roww in audio_tratado:
                    return True
        except pyodbc.Error as e:
            print(e)

    # Função para consultas na tabela respostas no banco de dados
    def resposta_db(resp):
        global retorno
        try:
            # Executar uma consulta
            cursor.execute('SELECT resp FROM respostas WHERE func = '+"'"+resp+"';")
            # Recuperar os resultados da consulta
            rows = cursor.fetchall()
            pre_retorno = []
            cont = 0
            for row in rows:
                cont = cont + 1
                roww = str(row[0])
                pre_retorno.append(roww)

            cont = cont-1
            numero = random.randint(0, cont)
            retorno = pre_retorno[numero]
            return retorno
        except pyodbc.Error as e:
            print(e)

    # Função para logs na tabela logs no banco de dados
    def inserir_logs(audio_tratado_log, retorno_log):
        tempo1=datetime.now() 
        hora1 = int(tempo1.strftime("%H"))
        minutos1 = int(tempo1.strftime("%M"))
        segundos1 = tempo1.strftime("%S")
        dia_do_mes1 = tempo1.strftime("%d")
        Dia_da_semana1 = tempo1.strftime("%A")
        Mes_do_ano1 = tempo1.strftime("%B")
        Ano1 = tempo1.strftime("%Y")
        try:
            Ano1 = str(Ano1)
            Mes_do_ano1 = str(Mes_do_ano1)
            Dia_da_semana1 = str(Dia_da_semana1)
            dia_do_mes1 = str(dia_do_mes1)
            hora1 = str(hora1)
            minutos1 = str(minutos1)
            segundos1 = str(segundos1)

            data_log = str(Ano1+"/"+Mes_do_ano1+"/"+dia_do_mes1+":"+Dia_da_semana1+"/"+hora1+":"+minutos1+":"+segundos1)

            cursor.execute("INSERT INTO logs(usuario, jarvis, data) VALUES ('"+audio_tratado_log+"','"+retorno_log+"','"+data_log+"');")
            # Salva as alterações no banco de dados
            conn.commit()
        except pyodbc.Error as e:
            print(e)



# Tabela Agenda no banco de dado
    # Função para consultas na tabela agenda no banco de dados
    def consulta_agenda():
        # Executar uma consulta
        cursor.execute('SELECT compromissos, data  FROM agendamentos')
        # Recuperar os resultados da consulta
        rows = cursor.fetchall()
        for row in rows:
            compromissos = str(row[0])
            print(compromissos)
            data = str(row[1])
            print(data)

    # Função para consultas na tabela agenda no banco de dados
    def inserir_agenda(incompromissos, indata):
        # Executar uma consulta
        cursor.execute("INSERT INTO agendamentos(compromissos, data) VALUES ('"+incompromissos+"','"+indata+"');")
        conn.commit()
                

    # Função modo soneca
    def modo_soneca():
        loop = 1
        with sr.Microphone() as source:
            while loop == 1:
                try:
                    audio = r.listen(source)
                    audio_tratado=(' ')
                    audio_tratado=(r.recognize_google(audio, language='pt-br'))
                    audio_tratado = audio_tratado.lower()
                    if audio_tratado == "ativar" or audio_tratado=="acorde" or audio_tratado=="acordar":
                        print("<<<--------------->>>")
                        print(audio_tratado)
                        Classes.voices.Voices.speak("Ativando")
                        print("<<<--------------->>>")     
                        loop = 2
                    else:
                        print("Modo soneca, para me ativar novamente fale 'Acorde' ou 'Ativar'")

                except sr.UnknownValueError:
                    print("Modo soneca, para me ativar novamente fale 'Acorde' ou 'Ativar'")



    #Abre o microfone pra captura
    contexto = ""
    retorno = ""
    modo_jarvis = ""
    with sr.Microphone() as source:
        print("<Ajustando o ruido do ambiente>")
        r.adjust_for_ambient_noise(source, duration=3)
        print("<Ruido do ambiente ajustado>")
        Classes.reproduzir_som.reproduzir_som.reproduzir_som(r"Sons\Beeps\Beep_ja_pode_falar.mp3")
        while True:
            print("Ouvindo...\n")
            try:
                audio = r.listen(source)
                audio_tratado=('...')
                audio_tratado=(r.recognize_google(audio, language="pt-br"))
                audio_tratado = audio_tratado.lower() 
                print("Reconhecendo...\n")
                print(audio_tratado + "\n")
                
                label_user.setText("Usuário: " + audio_tratado)
                

            #Codigos das respostas
                if modo_jarvis in audio_tratado:
                    print("Pensando...\n")

                    #Modo suspenção
                    if consulta_db('modo soneca'):
                        retorno = "Ativando o modo soneca"
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        Classes.reproduzir_som.reproduzir_som.reproduzir_som(r"Sons\Beeps\Beep_ja_pode_falar.mp3")
                        print("------------")
                        print("Modo Soneca")
                        print("------------")
                        retorno = "Modo Soneca"
                        modo_soneca()



                    elif consulta_db('desativar modo jarvis'):
                        modo_jarvis = ""
                        resposta_db("desativar modo jarvis")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)



                    elif consulta_db('modo jarvis'):
                        modo_jarvis = "jarvis"
                        resposta_db("modo jarvis")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)


                        
                    # Gera imagens com base nas descrições do usuario
                    elif consulta_db('modo geracao de imagem'):
                        openai.api_key = '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'
                        Classes.voices.Voices.speak("Descreva a imagem que você deseja Gerar")
                        try:
                            r.adjust_for_ambient_noise(source, duration=1)
                            audios = r.listen(source)
                            audio_tratados=('O')
                            audio_tratados=(r.recognize_google(audios, language='pt-br'))
                            print(audio_tratados)
                        except:
                            print("Deu um Erro!!")
                        Classes.voices.Voices.speak("Gerando Imagem")
                        response = openai.Image.create(
                        prompt = "Imagem com o estilo cartoon realista e meio aquarela e criativa sobre: " + audio_tratados,
                        n=1,
                        size="1024x1024"
                        )
                        image_url = response['data'][0]['url']
                        print(image_url)
                        # Abre o link no navegador padrão
                        retorno = "Abrindo a Imagem Gerada"
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        webbrowser.open(image_url)



                    # Abre um aplicativo
                    elif  consulta_db('abrir aplicativo'):
                        # Dicionário com os atalhos e caminhos dos aplicativos
                        aplicativos = {
                            'calculadora': 'C:\\Windows\\System32\\calc.exe',
                            'bloco de notas': 'C:\\Windows\\System32\\notepad.exe',
                            'explorador de arquivos': 'C:\\Windows\\explorer.exe',
                            'ópera': 'C:\\Users\\t4iga\\AppData\\Local\\Programs\\Opera\\launcher.exe',
                            'navegador': 'C:\\Users\\t4iga\\AppData\\Local\\Programs\\Opera\\launcher.exe',
                            'canva': 'C:\\Users\\t4iga\\AppData\\Local\\Programs\\Canva\\Canva.exe',
                        }
                        # Função para abrir um aplicativo a partir de um atalho
                        def abrir_aplicativo(atalho):
                            if atalho in aplicativos:
                                caminho = aplicativos[atalho]
                                subprocess.Popen(caminho)
                                print(f"Aplicativo '{atalho}' aberto.")
                                Classes.voices.Voices.speak("Abrindo " + atalho)
                            else:
                                print(f"Atalho '{atalho}' não encontrado.")
                                Classes.voices.Voices.speak(atalho + "Não encontrado")
                        # Pede qual aplicativo deseja abrir
                        Classes.voices.Voices.speak("Qual aplicativo voce deseja abrir?")
                        try:
                            r.adjust_for_ambient_noise(source, duration=1)
                            audios = r.listen(source)
                            atalho=(r.recognize_google(audios, language='pt-br'))
                            print(atalho)
                        except:
                            print("Deu um Erro!!")
                        abrir_aplicativo(atalho)

                    

                    # Fala o horario
                    elif consulta_db('horas'):
                        horario()
                        retorno=("São %d e %d minutos" %(hora,minutos))
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        print(retorno)

                    

                    # https://www.youtube.com/search?client=opera&q= para pesquisas no youtube
                    # https://www.google.com/search?client=opera&q= para pesquisas no google


                    
                    # Finaliza o código
                    elif consulta_db('desligamento'):
                        resposta_db("desligamento")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno) 
                        Classes.reproduzir_som.desligamento_sound()
                        exit()

                    

                    # Reseta a variavel contexto do chat-gpt
                    elif consulta_db('mudar de assunto'):
                        contexto = " "
                        resposta_db("mudar de assunto")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno) 



                    # Pula uma musica do spotfy
                    elif consulta_db('pular musica'):
                        resposta_db("pular musica")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        Classes.spotfy.Spotfy.pular()

                    # Da play em uma musica do spotfy
                    elif consulta_db('play musica'):
                        resposta_db("play musica")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        Classes.spotfy.Spotfy.play()

                    # Pausa uma musica do spotfy
                    elif consulta_db('pausar musica'):
                        resposta_db("pausar musica")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        Classes.spotfy.Spotfy.pausar()
                    
                    # Seleciona uma musica do spotfy
                    elif consulta_db('selecionar musica'):
                        Classes.voices.Voices.speak("Diga o nome da musica que você quer que eu toque")
                        retorno = "Diga o nome da musica que você quer que eu toque"
                        try:
                            r.adjust_for_ambient_noise(source, duration=1)
                            audios = r.listen(source)
                            musica=('O')
                            musica=(r.recognize_google(audios, language='pt-br'))
                        except:
                            print("Deu um Erro!!")
                        retorno = "Reproduzindo a música que você pediu!"
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        Classes.spotfy.Spotfy.tocar_uma_musica(musica)
            
                    # Toca uma playlist do spotfy
                    elif consulta_db('tocar playlist'):
                        Classes.voices.Voices.speak("Diga o nome da playlist que você quer que eu toque")
                        retorno = "Diga o nome da playlist que você quer que eu toque"
                        try:
                            r.adjust_for_ambient_noise(source, duration=1)
                            audios = r.listen(source)
                            musica=('O')
                            musica=(r.recognize_google(audios, language='pt-br'))
                        except:
                            print("Deu um Erro!!") 
                        retorno = "Reproduzindo a playlist que você pediu!"
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        Classes.spotfy.Spotfy.tocar_playlist(musica)


             

                    # Consulta os valores que estão cadastrados na tabela agenda do banco de dados
                    elif consulta_db('consulta agenda'):
                        resposta_db("consulta agenda")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        consulta_agenda()
                        


                    # Insere um novo compromisso na tabela agenda do banco de dados
                    elif consulta_db('inserir agenda'):
                        Classes.voices.Voices.speak("Abrindo agenda")
                        retorno = "Abrindo agenda"
                        Classes.voices.Voices.speak("Diga o nome do compromisso que você quer que eu agende!")
                        retorno = "Diga o nome do compromisso que você quer que eu agende!"
                        try:
                            r.adjust_for_ambient_noise(source, duration=1)
                            audios = r.listen(source)
                            incomprom=('O')
                            incomprom=(r.recognize_google(audios, language='pt-br'))
                        except:
                            print("Deu um Erro!!")

                        Classes.voices.Voices.speak("Diga a data desse compromisso!")
                        retorno = "Diga a data desse compromisso!"
                        try:
                            r.adjust_for_ambient_noise(source, duration=1)
                            audios = r.listen(source)
                            indata=('O')
                            indata=(r.recognize_google(audios, language='pt-br'))
                        except:
                            print("Deu um Erro!!")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak("Compromisso agendado")
                        retorno = "Compromisso agendado"
                        inserir_agenda(incomprom, indata)


                    # Códigos para executar ações do sistema principal
                    elif consulta_db("desligar sistema"):
                        resposta_db("desligar sistema")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        time.sleep(5)
                        os.system("shutdown /s /t 1")

                    elif consulta_db("sair sistema"):
                        resposta_db("sair sistema")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        time.sleep(5)
                        os.system("shutdown -l")

                    elif consulta_db("reiniciar sistema"):
                        resposta_db("reiniciar sistema")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        time.sleep(5)
                        os.system("shutdown /r /t 1")


                    # PyAutoGUI
                    elif consulta_db("abrir gerenciador de tarefas"):
                        resposta_db("abrir gerenciador de tarefas")
                        pyautogui.hotkey("ctrl", "shift", "esc")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)

                    elif consulta_db("visao geral das tarefas"):
                        resposta_db("visao geral das tarefas")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        pyautogui.hotkey("winleft", "tab")

                    elif consulta_db("nova area de trabalho"):
                        resposta_db("nova area de trabalho")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        pyautogui.hotkey("ctrl", "winleft", "d")

                    elif consulta_db("deletar area de trabalho"):
                        resposta_db("deletar area de trabalho")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        pyautogui.hotkey("ctrl", "winleft", "f4")

                    elif consulta_db("mover para a are de trabalho a esquerda"):
                        resposta_db("mover para a are de trabalho a esquerda")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        pyautogui.hotkey("ctrl", "winleft", "left")

                    elif consulta_db("mover para a are de trabalho a direita"):
                        resposta_db("mover para a are de trabalho a direita")
                        label_jarvis.setText("Jarvis: "+retorno)
                        Classes.voices.Voices.speak(retorno)
                        pyautogui.hotkey("ctrl", "winleft", "right")
                        

                    # Manda todos os conteúdos que não se encaixam em nenhuma condição anterior para a api do chat-gpt e ele responde
                    else:
                        #Classes.SisSons.reproduzir_som(r"Sons\Beeps\beep_pensando.mp3")
                        try:
                            entrada = contexto + "\n" + audio_tratado + "\n"
                            openai.api_key = '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'
                            response = openai.ChatCompletion.create(
                                model="gpt-3.5-turbo",
                                messages=[
                                    {"role": "system", "content":entrada}
                                ],
                                max_tokens=150
                            )
                            retorno = response['choices'][0]['message']['content']
                            contexto += audio_tratado + "\n" + retorno + "\n"
                            label_jarvis.setText("Jarvis: "+retorno)
                            print(retorno)
                            Classes.voices.Voices.fast_speak(retorno)
                        except:
                            print("Erro... Openai não respondendo...")
                            Classes.voices.Voices.speak("Erro... Openai não respondendo...")

                    inserir_logs(audio_tratado, retorno)
                

            # Para valores não identificados
            except sr.UnknownValueError:
                resposta_db("nao identificado")
                print(retorno+"\n")







def init():
    app = QApplication(sys.argv)

    initt = QMainWindow()
    initt.setWindowTitle("Janela com GIF Animado")
    initt.setWindowState(initt.windowState() | QtCore.Qt.WindowFullScreen)

    # Define a cor de fundo como preto
    palette = initt.palette()
    palette.setColor(initt.backgroundRole(), QColor(0, 0, 0))
    initt.setPalette(palette)

    # Mostra o GIF do centro da tela
    gif = QLabel(initt)
    movie = QMovie(r"Interface\Graficos\GEEKtyper_com - Aperture Science.gif")
    gif.setMovie(movie)
    movie.start()
    window_frame = initt.frameGeometry()
    center_point = QDesktopWidget().availableGeometry().center()
    window_frame.moveCenter(center_point)
    initt.move(window_frame.topLeft())
    gif.setAlignment(Qt.AlignCenter)
    gif.setGeometry(0, 0, window_frame.width(), window_frame.height())

    initt.show()
    sys.exit(app.exec())







def info():
    while True:
        Classes.keylogger.keylogger.key()





# Inicia o reconhecimento facial, se der verdadeiro ele acessa o código
# Inicia a função init
#thread_init = threading.Thread(target=init)
#thread_init.start()

if __name__ == "__main__":
    Classes.voices.Voices.speak("Verificação de identidade requisitada!")
    Classes.voices.Voices.speak("Iniciando reconhecimento facial!")
    if Classes.ReconhecimentoFacial.ReconhecimentoFacial.global_reconhecimento_facial():
        print("@+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++@")
        print("Verificação de identidade Bem Sussedida, Bem vindo Matheus")
        print("@+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++@")
        Classes.reproduzir_som.reproduzir_som.reproduzir_som(r"Sons\Beeps\Beep_reconhecimento_facial_bem_sussedido.mp3")
        Classes.voices.Voices.speak("Verificação de identidade Bem Sussedida, Bem vindo Matheus!")

        # Inicia a função main
        thread_code = threading.Thread(target=code)
        thread_code.start()

    # Se não ele fecha a execução
    else:
        print("@+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++@")
        print("Verificação de identidade Mal Sussedida, Por favor fale com o Administrador do sistema")
        print("@+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++@")
        Classes.voices.Voices.speak("Verificação de identidade Mal Sussedida, Por favor fale com o Administrador do sistema!")
        exit()
    
    main()