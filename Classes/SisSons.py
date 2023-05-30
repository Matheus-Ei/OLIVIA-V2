import pygame



def inicializacao_sound():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Sons\Inicialização\Inicialização 1.mp3")
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def desligamento_sound():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Sons\Desligamento\Desligamento 1.mp3")
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def atv_soneca_sound():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Sons\Modo Soneca\Ativando Modo Soneca.mp3")
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def datv_soneca_sound():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Sons\Modo Soneca\DesAtivando Modo Soneca.mp3")
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def beep_pensando():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(r"C:\Users\t4iga\OneDrive\Projetos\Programação\Assistente_Pessoal\Sons\Beeps\beep_pensando.mp3")
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def reproduzir_som(caminho):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(caminho)
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()