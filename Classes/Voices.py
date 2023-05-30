import os
import pygame
import re
import unicodedata


def speak(data):
    voice = 'en-US-SteffanNeural'
    voice2 = 'pt-BR-AntonioNeural'
    voice3 = 'pt-BR-FranciscaNeural'

    data = data.replace('\n'," ")
    
    command = f'edge-tts --rate="+10%" --voice "{voice3}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")
    

    try:
        pygame.mixer.music.play()
        print(data)

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()