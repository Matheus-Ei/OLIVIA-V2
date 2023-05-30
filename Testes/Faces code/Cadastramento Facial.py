import cv2
import face_recognition

def pre_processamento(imagem):
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    return gray

# Carregar o modelo pré-treinado para detecção de faces
detector_rosto = cv2.CascadeClassifier("Testes\Faces code\haarcascade_frontalface_default.xml")

# Iniciar a captura de vídeo da câmera
captura = cv2.VideoCapture(0)

def capturar_imagens(caminho, nome_pessoa, quantidade_imagens):
    contador = 0
    imagens = []

    while contador < quantidade_imagens:
        ret, frame = captura.read()
        gray = pre_processamento(frame)
        faces = detector_rosto.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        tamanho_face = (100, 100)

        for (x, y, w, h) in faces:
            roi_gray = cv2.resize(gray[y:y+h, x:x+w], tamanho_face)
            caminho_imagem = caminho + "/" + nome_pessoa + "_" + str(contador) + ".jpg"
            cv2.imwrite(caminho_imagem, roi_gray)
            imagens.append(roi_gray)
            contador += 1

        cv2.imshow("Capturando Imagens", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    return imagens

caminho_pasta = "Testes\Faces code\Faces"
nome_pessoa = "Matheus"
quantidade_imagens = 1

imagens_capturadas = capturar_imagens(caminho_pasta, nome_pessoa, quantidade_imagens)







# Carregar imagem em que deseja realizar o reconhecimento facial
Referencia = face_recognition.load_image_file("Testes\Faces code\Faces\Cadastros\Matheus_1.jpg")
Referencia_encode = face_recognition.face_encodings(Referencia)[0]

Camera = face_recognition.load_image_file("Testes\Faces code\Faces\Matheus_0.jpg")
Camera_encode = face_recognition.face_encodings(Camera)[0]


# Encontrar localização dos rostos na imagem
face_locations = face_recognition.face_locations(Camera)


# Comparar o rosto encontrado com o rosto de referência
matches = face_recognition.compare_faces([Referencia_encode], Camera_encode)
face_distance = face_recognition.face_distance([Referencia_encode], Camera_encode)
print(matches)
print(face_distance)

if matches == [True]:
    print("São semelhantes")
else:
    print("São Diferentes")




# Desenhar retângulos ao redor dos rostos encontrados na imagem
for top, right, bottom, left in face_locations:
    cv2.rectangle(Camera, (left, top), (right, bottom), (0, 255, 0), 2)

# Exibir a imagem com os retângulos
cv2.imshow("Reconhecimento Facial", Camera)
cv2.waitKey(0)
cv2.destroyAllWindows()






