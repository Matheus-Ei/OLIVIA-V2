#Imports
from calendar import c
from inspect import EndOfBlock
from math import log
from re import X
from typing import Text
from wave import Error
from xmlrpc.client import boolean
import keyboard
from pynput.keyboard import Listener, Key
import speech_recognition as sr
import pyttsx3
from Bibliotecas.playsound import playsound
import gtts
from datetime import datetime
import random
import sys
import requests
from bs4 import BeautifulSoup
import mysql.connector
import serial
import openai
import tkinter as tk
import multiprocessing
import subprocess
import webbrowser
import os
from PIL import Image, ImageTk
import time
import pyodbc
from tkinter import messagebox
from PIL import ImageTk
from moviepy.editor import VideoFileClip


def reproduzir_video(caminho):
    janela = tk.Tk()
    janela.attributes("-fullscreen", True)

    video = VideoFileClip(caminho)
    
    # Obtém a duração do vídeo em segundos
    duracao = video.duration

    # Cria uma janela Tkinter
    janela = tk.Tk()

    # Configura a janela
    janela.geometry(f"{video.size[0]}x{video.size[1]}")  # Define o tamanho da janela
    janela.title('Reproduzindo vídeo')

    # Cria um widget Canvas para exibir o vídeo
    canvas = tk.Canvas(janela, width=video.size[0], height=video.size[1])
    canvas.pack()

    # Converte o quadro do vídeo em uma imagem PIL para exibir no Canvas
    def convert_frame_to_image(frame):
        return ImageTk.PhotoImage(image=Image.fromarray(frame))
    
    # Função para atualizar o frame exibido no Canvas
    def atualizar_frame():
        if video.pos > duracao:
            encerrar_reproducao()
            return
        frame = video.get_frame(video.pos)
        imagem = convert_frame_to_image(frame)
        canvas.create_image(0, 0, anchor=tk.NW, image=imagem)
        video.set_duration(duracao)
        janela.after(1, atualizar_frame)


    # Reproduz o vídeo chamando a função de atualização de frame
    atualizar_frame()

    def encerrar_reproducao():
        messagebox.showinfo('Fim do vídeo', 'A reprodução do vídeo terminou!')
        janela.destroy()

    janela.mainloop()

reproduzir_video('Interface\Globo.mp4')