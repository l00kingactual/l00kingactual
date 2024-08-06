import tensorflow as tf
from tensorflow.keras.layers import Layer

class QuantumCircuitLayer(Layer):
    def __init__(self, units=10, **kwargs):
        super(QuantumCircuitLayer, self).__init__(**kwargs)
        self.units = units

    def build(self, input_shape):
        self.theta = self.add_weight(name='theta', shape=(self.units,), initializer='uniform', trainable=True)

    def call(self, inputs):
        if inputs.shape[-1] != self.units:
            raise ValueError(f"Input shape {inputs.shape[-1]} does not match expected shape {self.units}")

        output = tf.math.cos(self.theta) * inputs
        return output

    def compute_output_shape(self, input_shape):
        return input_shape

    def get_config(self):
        config = super(QuantumCircuitLayer, self).get_config()
        config.update({'units': self.units})
        return config
