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

from UQEBM_EnhancedBitDescription import EnhancedBitDescription


class IntegratedBitDescription(EnhancedBitDescription):
    def encode_with_quantum(self, decimal_value):
        bit_coordinates = self.decimal_to_bit(decimal_value)
        quantum_encoded_bits = [(coord, encode_quantum_bit(self.quantum_states.get(i, {}))) for i, coord in enumerate(bit_coordinates)]
        return quantum_encoded_bits

    def decode_with_quantum(self, quantum_encoded_bits):
        bit_coordinates = [coord for coord, _ in quantum_encoded_bits]
        reconstructed_decimal = self.bit_to_decimal(bit_coordinates)
        return reconstructed_decimal, quantum_encoded_bits

    def describe_layers(self):
        descriptions = []
        ranges = [
            (-1, 0, 1), (-Decimal(np.pi), 0, Decimal(np.pi)), (-5, 0, 5), (-10, 0, 10),
            (-13, 0, 13), (-60, 0, 60), (-360, 0, 360)
        ]
        scales = [
            1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 15, 16, 19, 22, 24, 25,
            28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64,
            94, 128, 171, 196, 206, 345, 360, 512, 720, 845, 1080, 4096, 4394, 5239, 5261
        ]
        
        for i, base in enumerate(self.number_bases):
            descriptions.append({
                'layer': i,
                'range': ranges[i] if i < len(ranges) else (-base, 0, base),
                'quantum_description': self.quantum_states.get(i, {}),
                'scale': scales[i] if i < len(scales) else None  # Handle cases where there are more layers than scales
            })
        return descriptions
