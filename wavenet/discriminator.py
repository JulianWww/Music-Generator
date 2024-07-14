from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.losses import BinaryCrossEntropy
import numpy as np

def loss(real_output, fake_output):
    cross_entropy = 
    real_loss = cross

def create_discriminator():
    model = Sequential()
    model.add(Embedding(input_dim=256, output_dim=32, input_shape=(2,)))
    model.add(LSTM(128))
    model.add(Dense(1048, activation="tanh"))
    model.add(Dense(256, activation="tanh"))
    model.add(Dense(64, activation="tanh"))
    model.add(Dense(16, activation="tanh"))
    model.add(Dense(4, activation="tanh"))
    model.add(Dense(1, activation="sigmoid"))

    model.compile(loss=BinaryCrossEntropy(from_logits=True), optimizer=Adam(learning_rate=0.01))
    model.summary()

create_discriminator()
