import pyautogui
import pytesseract
from pywinauto import Application
import time

# Função para localizar o texto na tela
def localizar_texto(valor):
    # Captura uma screenshot da tela
    screenshot = pyautogui.screenshot()
    
    # Usa o pytesseract para extrair o texto da imagem
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    #C:\Program Files\Tesseract-OCR
    texto = pytesseract.image_to_string(screenshot)
    print(texto)
    
    # Verifica se o valor está presente no texto
    if valor in texto:
        # Encontra a posição do texto na tela
        posicao = pyautogui.locateOnScreen(screenshot, confidence=0.8)
        print(posicao)
        
        centro_x = posicao.left + (posicao.width / 2)
        centro_y = posicao.top + (posicao.height / 2)
        pyautogui.click(centro_x, centro_y)
        

# Exemplo de uso
valor_procurado = "DRAG"
localizar_texto(valor_procurado)