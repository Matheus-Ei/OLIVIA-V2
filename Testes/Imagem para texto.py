from PIL import Image, ImageDraw, ImageFont
import cv2
import pygame

# Inicialize a câmera
camera = cv2.VideoCapture(0)

def capturar():
    # Captura um quadro (foto)
    ret, quadro = camera.read()
    # Salva a foto em um arquivo
    cv2.imwrite("foto.jpg", quadro)



capturar()
# Carregue a imagem original
imagem_original = Image.open("foto.jpg")
# Defina a cor do texto
cor_texto = (0, 255, 0)  # Verde
# Defina a fonte do texto
fonte = ImageFont.truetype("Testes\ARIALI.TTF", 100)  # Substitua pelo caminho da sua fonte e tamanho desejado
# Crie uma nova imagem do mesmo tamanho da imagem original
imagem_texto = Image.new("RGB", imagem_original.size)
desenho = ImageDraw.Draw(imagem_texto)
# Defina os caracteres a serem usados para diferentes níveis de intensidade de verde
caracteres_verdes = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]
total_caracteres = len(caracteres_verdes)
# Converta a imagem para o modo HSV
imagem_hsv = imagem_original.convert("HSV")
# Percorra cada pixel da imagem original
largura, altura = imagem_original.size
for y in range(altura):
    for x in range(largura):
        # Obtenha o valor do pixel
        pixel = imagem_original.getpixel((x, y))
        # Obtenha o valor de luminosidade do pixel (canal V do HSV)
        pixel_hsv = imagem_hsv.getpixel((x, y))
        pixel_hsv = tuple(elemento / 2 for elemento in pixel_hsv)
        luminosidade = pixel_hsv[2]
        carac = " "
        if luminosidade < 20:
                carac = "."
        elif luminosidade < 40:
                carac = "," 
        elif luminosidade < 60:
                carac = ";" 
        elif luminosidade < 100:
                carac = "-" 
        elif luminosidade < 110:
                carac = "+" 
        elif luminosidade < 130:
                carac = "=" 
        elif luminosidade < 140:
                carac = "#" 
        else:
               carac = "@" 
        print(carac, end=' ')
    print("\n")
# Salve a imagem resultante
imagem_texto.save("Testes\imagetext\png.png")