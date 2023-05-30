def speak(string):
    tamanho = 10
    palavras = string.split()
    segmentos = []
    segmento = ""
    for palavra in palavras:
        if len(segmento) + len(palavra) <= tamanho:
            segmento += palavra + " "
        else:
            segmentos.append(segmento.strip())
            segmento = palavra + " "
    segmentos.append(segmento.strip())
    return segmentos

# Exemplo de uso
string_original = "Python é uma linguagem de programação poderosa e versátil"

segmentos = speak(string_original)

# Juntando todos os segmentos em uma única string
contador = 0
while len(segmentos) != contador:
    resultado = segmentos[contador]
    print(resultado)

    contador = contador+1
