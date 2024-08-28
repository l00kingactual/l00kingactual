import tensorflow as tf
from tensorflow.keras.layers import Layer

class QuantumCircuitLayer(Layer):
    def __init__(self, units=10, k=None, q=None, epsilon=None, **kwargs):
        super(QuantumCircuitLayer, self).__init__(**kwargs)
        self.units = units
        self.k = k
        self.q = q
        self.epsilon = epsilon

    def build(self, input_shape):
        self.theta = self.add_weight(name='theta', shape=(self.units,), initializer='uniform', trainable=True)
        self.phi = self.add_weight(name='phi', shape=(self.units,), initializer='uniform', trainable=True)

    def call(self, inputs):
        # Ensure that the weights have been initialized
        if not hasattr(self, 'theta'):
            self.build(inputs.shape)

        # Quantum operation using k, q, epsilon if they are not None
        if self.k is not None and self.q is not None and self.epsilon is not None:
            forward_output = tf.math.cos(self.theta * self.k) * inputs
            backward_output = tf.math.sin(self.phi * self.q) * inputs
            output = forward_output + backward_output + self.epsilon
        else:
            forward_output = tf.math.cos(self.theta) * inputs
            backward_output = tf.math.sin(self.phi) * inputs
            output = forward_output + backward_output

        return output

    def compute_output_shape(self, input_shape):
        return input_shape  # Ensuring output shape matches input shape

    def get_config(self):
        config = super(QuantumCircuitLayer, self).get_config()
        config.update({
            'units': self.units,
            'k': self.k,
            'q': self.q,
            'epsilon': self.epsilon,
        })
        return config
