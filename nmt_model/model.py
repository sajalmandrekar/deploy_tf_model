import tensorflow as tf
import tensorflow_text as tf_text
import numpy as np
import os


def load_model(MODEL_NAME, MODEL_PATH):
    print('loading model...')
    reloaded = tf.saved_model.load(MODEL_PATH)

    #warming up
    print('warming up...')
    test_input='how are you?'
    _ = reloaded(tf.constant(test_input)) #warmup
    del _

    print(f'Model {MODEL_NAME} loaded!')
    return reloaded

def translate_text(model, input_text):
    return model(tf.constant(input_text)).numpy().decode()
