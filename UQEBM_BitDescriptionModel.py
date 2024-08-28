import numpy as np
import json
import os
import tensorflow as tf
from datetime import datetime
from decimal import Decimal, getcontext
import logging
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from compute_metrics import compute_metrics, save_metrics_to_json
from quantum.quantum_layer import QuantumCircuitLayer
from quantum.quantum_bit_utils import encode_quantum_bit, decode_quantum_bit
from quantum.quantum_circuit_tuning import tune_quantum_circuit
from search.grid_search import run_search_optimization as grid_search_optimization
from search.bayesian import bayesian_optimization
from search.random_search import run_random_search_optimization
from search.simulated_annealing import simulated_annealing_optimization
from search.hyperband import hyperband_optimization
from search.optuna_optimization import optuna_optimization
from search.pso import run_pso_optimization
from neural_network import build_enhanced_nn as NeuralNetworkModel  # Correct import statement
from sklearn.base import BaseEstimator, ClassifierMixin

from UQEMB_IntegratedBitDescription import IntegratedBitDescription

class BitDescriptionModel(BaseEstimator, ClassifierMixin):
    def __init__(self, range_min=0, range_max=100, number_bases=None, quantum_states=None, scales=None):
        self.range_min = range_min
        self.range_max = range_max
        self.number_bases = number_bases if number_bases is not None else [1, np.pi, np.e, 5, 10, 13, 60]
        self.quantum_states = quantum_states if quantum_states is not None else {}
        self.scales = scales if scales is not None else [1] * len(self.number_bases)
        self.classes_ = None
        self.neural_net = None  # Neural network is not initialized here

    def initialize_neural_net(self, input_shape, num_classes, num_layers=5, units_0=64, dropout_0=0.2, units_1=32, dropout_1=0.2, learning_rate=0.001):
        # Initialize the neural network with the required parameters
        self.neural_net = NeuralNetworkModel(
            input_shape=input_shape,
            num_classes=num_classes,
            num_layers=num_layers,
            units_0=units_0,
            dropout_0=dropout_0,
            units_1=units_1,
            dropout_1=dropout_1,
            learning_rate=learning_rate
        )

    def fit(self, X, y):
        if self.neural_net is None:
            raise ValueError("Neural network is not initialized. Call `initialize_neural_net` first.")
        self.classes_ = np.unique(y)
        self.model_ = IntegratedBitDescription(self.range_min, self.range_max, self.number_bases, self.quantum_states, self.scales)
        
        # Training the neural network using the `fit` method
        self.neural_net.fit(X, y, epochs=50, batch_size=32)  # Adjust `epochs` and `batch_size` as necessary
        return self


    def predict(self, X):
        if self.neural_net is None:
            raise ValueError("Neural network is not initialized. Call `initialize_neural_net` first.")
        predictions = self.neural_net.predict(X)
        return predictions

    def predict_proba(self, X):
        if self.neural_net is None:
            raise ValueError("Neural network is not initialized. Call `initialize_neural_net` first.")
        # Use `predict` directly to get probabilities
        return self.neural_net.predict(X)


    def score(self, X, y):
        predictions = self.predict(X)
        return accuracy_score(y, predictions)

# Define a combined model building function with quantum integration
def build_combined_model(input_shape, num_classes, k=None, q=None, epsilon=None, **params):
    # Ensure input_shape is a tuple of integers
    if not isinstance(input_shape, tuple):
        raise ValueError(f"Expected input_shape to be a tuple, but got {type(input_shape).__name__}")

    inputs = tf.keras.layers.Input(shape=input_shape)
    
    # Quantum Circuit Layer Integration
    if k is not None and q is not None and epsilon is not None:
        x = QuantumCircuitLayer(units=input_shape[0], k=k, q=q, epsilon=epsilon)(inputs)
    else:
        x = QuantumCircuitLayer(units=input_shape[0])(inputs)
    
    x = tf.keras.layers.Dense(params.get('units_0', 400), activation='relu')(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dropout(params.get('dropout_0', 0.3))(x)

    # Standard Layers with Janus symmetry considerations
    for i in range(params.get('num_layers', 6) - 2):
        units = params.get('units_0', 400) // (2 ** (i % 3))
        x_forward = tf.keras.layers.Dense(units, activation='relu')(x)
        x_backward = tf.keras.layers.Dense(units, activation='relu')(x)
        x = tf.keras.layers.Add()([x_forward, x_backward])
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Dropout(params.get('dropout_1', 0.3))(x)

    outputs = tf.keras.layers.Dense(num_classes, activation='softmax')(x)

    model = tf.keras.models.Model(inputs, outputs)
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=params.get('learning_rate', 0.001)),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model