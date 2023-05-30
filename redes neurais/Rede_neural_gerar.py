import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Carregar o modelo treinado
model = load_model('Redes_Neurais\modelo.h5')

# Carregar o tokenizer usado para treinar o modelo
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Parâmetros para geração de texto
seed_text = "Olá,"
num_words = 10

# Gerar texto
result = seed_text
for _ in range(num_words):
    sequence = tokenizer.texts_to_sequences([seed_text])[0]
    sequence = pad_sequences([sequence], maxlen=model.input_shape[1])
    prediction = model.predict_classes(sequence, verbose=0)
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == prediction:
            output_word = word
            break
    seed_text += " " + output_word
    result += " " + output_word

print(result)
