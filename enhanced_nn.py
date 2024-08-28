# enhanced_nn.py
import tensorflow as tf
from quantum.quantum_layer import QuantumCircuitLayer  # Assuming this is your custom quantum layer

def build_enhanced_nn(input_shape, num_classes, num_layers, units_0, dropout_0, units_1, dropout_1, learning_rate):
    inputs = tf.keras.layers.Input(shape=input_shape)
    
    # Initial Quantum Circuit Layer
    x = QuantumCircuitLayer(units=input_shape[0])(inputs)
    
    # Initial Dense Layer
    x = tf.keras.layers.Dense(units_0, activation='relu')(x)
    x = tf.keras.layers.Dropout(dropout_0)(x)

    # Implementing trigonometric "wave" architecture with Janus symmetry
    for i in range(num_layers - 2):
        if i % 4 == 0:
            units = units_0 // 2
            x = tf.keras.layers.Dense(units, activation='relu')(x)
            x = tf.keras.layers.Lambda(lambda x: tf.sin(x))(x)
        elif i % 4 == 1:
            units = units_1
            x = tf.keras.layers.Dense(units, activation='relu')(x)
            x = tf.keras.layers.Lambda(lambda x: tf.cos(x))(x)
        elif i % 4 == 2:
            units = units_1 // 2
            x = tf.keras.layers.Dense(units, activation='relu')(x)
            x = tf.keras.layers.Lambda(lambda x: tf.tan(x))(x)
        else:
            units = units_0
            x_forward = tf.keras.layers.Dense(units, activation='relu')(x)
            x_backward = tf.keras.layers.Dense(units, activation='relu')(x)
            x = tf.keras.layers.Add()([x_forward, x_backward])
            x = tf.keras.layers.Dropout(dropout_1)(x)

    outputs = tf.keras.layers.Dense(num_classes, activation='softmax')(x)

    model = tf.keras.models.Model(inputs, outputs)
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model
