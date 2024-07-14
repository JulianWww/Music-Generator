from tensorflow.keras.layers import Embedding, GRU, Activation, Add, Dense, LSTM
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras import Layer, Model, Input
from tensorflow.random import uniform
from config import DIALATIONS, LR, INPUT_SIZE, OUT_SIZE
import numpy as np

class Generator(Model):
  def __init__(self, vocab_size, embedding_dim, rnn_units):
    super().__init__()
    self.embedding = Embedding(vocab_size, embedding_dim, input_shape=(2,))
    self.gru = GRU(rnn_units,
                   return_sequences=True,
                   return_state=True
                )
    self.dense = Dense(vocab_size)

  def call(self, inputs, states=None, return_state=False, training=False):
    x = inputs
    x = self.embedding(x, training=training)
    print(x.shape)
    if states is None:
      states = self.gru.get_initial_state(x)
    x, states = self.gru(x, initial_state=states, training=training)
    x = self.dense(x, training=training)

    if return_state:
      return x, states
    else:
      return x

def get_input():
    return np.random.uniform(-1,1,2)

model = Generator(32, 32, 256)
model.summary()
model.predict(get_input())