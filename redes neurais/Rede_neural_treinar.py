import requests
from bs4 import BeautifulSoup
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Dados de treinamento inicial
textos = [
    "Olá, como você está?",
    "Estou bem, obrigado por perguntar."
]

# Criação do tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(textos)

num_iterations = 1

# Loop para coletar e adicionar dados de treinamento
for i in range(num_iterations):
    # Faz a solicitação para a página aleatória da Wikipedia
    random_url = "https://pt.wikipedia.org/wiki/Especial:Aleat%C3%B3ria?lg=pt"
    response = requests.get(random_url)
    
    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Cria o objeto BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extrai o conteúdo do artigo
        content_div = soup.find("div", {"id": "mw-content-text"})
        
        # Remove referências numéricas
        for sup in content_div.find_all("sup"):
            sup.extract()
        
        # Remove links internos
        for link in content_div.find_all("a"):
            link.extract()
        
        # Extrai apenas o texto do conteúdo
        text = content_div.get_text()

        print(text)
        
        # Adiciona o novo texto aos dados de treinamento
        textos.append(text)
        
        # Atualiza o tokenizer com o novo texto
        tokenizer.fit_on_texts([text])
        
    else:
        print("Erro ao acessar a página da Wikipedia.")

# Obtém as sequências de treinamento
sequences = tokenizer.texts_to_sequences(textos)

# Obtém o vocabulário e o tamanho do vocabulário
word_index = tokenizer.word_index
vocab_size = len(word_index) + 1

# Gera os pares de sequências de entrada e saída
input_sequences = []
output_sequences = []
for sequence in sequences:
    for i in range(1, len(sequence)):
        n_gram_sequence = sequence[:i+1]
        input_sequences.append(n_gram_sequence[:-1])
        output_sequences.append(n_gram_sequence[-1])

# Pad das sequências de entrada para ter o mesmo tamanho
max_sequence_length = max([len(sequence) for sequence in input_sequences])
input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_length)

# One-hot encoding das saídas
output_sequences = tf.keras.utils.to_categorical(output_sequences, num_classes=vocab_size)

# Criação do modelo
model = Sequential()
model.add(Embedding(vocab_size, 100, input_length=max_sequence_length))
model.add(LSTM(150, return_sequences=True))
model.add(LSTM(150))
model.add(Dense(vocab_size, activation='softmax'))

# Compilação do modelo
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Treinamento do modelo
model.fit(input_sequences, output_sequences, epochs=100, verbose=1)

# Salvar o modelo treinado
model.save('modelo.h5')

# Salvar o tokenizer usado para treinar o modelo
with open('tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)
