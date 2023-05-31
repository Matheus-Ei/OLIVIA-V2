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
import pygame
import imageio
from PIL import Image, ImageTk

    
def reproduzirgif(arquivo_gif):
    pygame.init()
    aaaa = False

    # Carrega o arquivo GIF usando a biblioteca Pillow
    imagem_gif = Image.open(arquivo_gif)
    num_frames = imagem_gif.n_frames

    largura_janela = imagem_gif.width
    altura_janela = imagem_gif.height

    clock = pygame.time.Clock()

    quadros_gif = []
    for i in range(num_frames):
        imagem_gif.seek(i)
        quadro = imagem_gif.convert("RGBA")
        quadros_gif.append(pygame.image.fromstring(quadro.tobytes(), quadro.size, quadro.mode))
        aaaa = True

    if aaaa == True:
        janela = pygame.display.set_mode((largura_janela, altura_janela))
        pygame.display.set_caption("Janela com GIF")

    indice = 0

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        janela.blit(quadros_gif[indice], (0, 0))

        indice += 1
        if indice >= num_frames:
            indice = 0

        pygame.display.flip()
        clock.tick(30)  # Define o FPS (30 quadros por segundo)

    pygame.quit()

