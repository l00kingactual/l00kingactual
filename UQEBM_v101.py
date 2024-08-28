import numpy as np
import json
import os
from datetime import datetime
from decimal import Decimal, getcontext
import logging
from sklearn.model_selection import GridSearchCV
from skopt import BayesSearchCV
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from compute_metrics import compute_metrics, save_metrics_to_json
from quantum_states import quantum_states

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Set precision for decimal operations
getcontext().prec = 100

# Functions to encode and decode quantum bits
def encode_quantum_bit(quantum_state):
    n = quantum_state['n']
    l = quantum_state['l']
    m_l = quantum_state['m_l']
    m_s = int(quantum_state['m_s'] * 2)  # Convert -0.5 or 0.5 to -1 or 1
    
    encoded_value = (n << 3) | (l << 2) | (m_l << 1) | (m_s & 0b1)
    return encoded_value

def decode_quantum_bit(encoded_value):
    quantum_state = {
        'n': (encoded_value >> 3) & 0b111,
        'l': (encoded_value >> 2) & 0b1,
        'm_l': (encoded_value >> 1) & 0b1,
        'm_s': ((encoded_value & 0b1) * 2 - 1) / 2  # Convert back to -0.5 or 0.5
    }
    return quantum_state

class EnhancedBitDescription:
    def __init__(self, range_min, range_max, number_bases, quantum_states):
        self.range_min = Decimal(range_min)
        self.range_max = Decimal(range_max)
        if not isinstance(number_bases, list):
            number_bases = [number_bases]  # Ensure it's a list
        self.number_bases = [Decimal(b) for b in number_bases if b != 0]
        self.max_value = Decimal(1)
        self.quantum_states = quantum_states

        for base in self.number_bases:
            self.max_value *= base
        logging.debug(f"Initialized with range_min={self.range_min}, range_max={self.range_max}, max_value={self.max_value}")

    def decimal_to_bit(self, decimal_value):
        decimal_value = Decimal(decimal_value)
        normalized_value = (decimal_value - self.range_min) / (self.range_max - self.range_min)
        scaled_value = normalized_value * self.max_value
        return self._convert_to_layers(scaled_value)

    def bit_to_decimal(self, bit_coordinates):
        scaled_value = self._convert_from_layers(bit_coordinates)
        normalized_value = scaled_value / self.max_value
        decimal_value = normalized_value * (self.range_max - self.range_min) + self.range_min
        return float(decimal_value)

    def _convert_to_layers(self, value):
        coordinates = []
        remaining_value = value
        for i, base in enumerate(self.number_bases):
            coord = (remaining_value % base).quantize(Decimal('1.'))
            remaining_value = (remaining_value // base).quantize(Decimal('1.'))
            quantum_adjustment = self.quantum_states.get(i, {}).get('n', 1)
            refined_coord = coord * Decimal(quantum_adjustment)
            coordinates.append(refined_coord)
        return coordinates

    def _convert_from_layers(self, coordinates):
        value = Decimal(0)
        multiplier = Decimal(1)
        for coord, base in zip(coordinates, self.number_bases):
            value += coord * multiplier
            multiplier *= base
        return value

class IntegratedBitDescription(EnhancedBitDescription):
    def __init__(self, range_min, range_max, number_bases, quantum_states):
        super().__init__(range_min, range_max, number_bases, quantum_states)

    def encode_with_quantum(self, decimal_value):
        bit_coordinates = self.decimal_to_bit(decimal_value)

        quantum_encoded_bits = []
        for i, coord in enumerate(bit_coordinates):
            quantum_state = self.quantum_states.get(i, {'n': 1, 'l': 0, 'm_l': 0, 'm_s': 0})
            quantum_bit = encode_quantum_bit(quantum_state)
            quantum_encoded_bits.append((coord, quantum_bit))

        return quantum_encoded_bits

    def decode_with_quantum(self, quantum_encoded_bits):
        bit_coordinates = []
        for coord, quantum_bit in quantum_encoded_bits:
            quantum_state = decode_quantum_bit(quantum_bit)
            bit_coordinates.append(coord)

        reconstructed_decimal = self.bit_to_decimal(bit_coordinates)
        return reconstructed_decimal, quantum_encoded_bits

    def describe_layers(self):
        descriptions = []
        ranges = [
            (-1, 0, 1), (-np.pi, 0, np.pi), (-5, 0, 5), (-10, 0, 10),
            (-13, 0, 13), (-60, 0, 60), (-360, 0, 360)
        ]
        for i, base in enumerate(self.number_bases):
            descriptions.append({
                'layer': i,
                'range': ranges[i] if i < len(ranges) else (-base, 0, base),
                'quantum_description': self.quantum_states.get(i, {})
            })
        return descriptions

   

import numpy as np
from decimal import Decimal
from sklearn.model_selection import train_test_split, GridSearchCV
from skopt import BayesSearchCV
from sklearn.metrics import accuracy_score
from sklearn.base import BaseEstimator, ClassifierMixin
from compute_metrics import compute_metrics, save_metrics_to_json
from quantum_states import quantum_states
import logging
import json
import os
from datetime import datetime

# Additional functions for saving and loading
def load_previous_best(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return None

def save_best_bit_description(best_bit_desc, metrics, file_prefix='best_bit_desc'):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    best_bit_desc_data = {
        'range_min': str(best_bit_desc.range_min),
        'range_max': str(best_bit_desc.range_max),
        'number_bases': [str(base) for base in best_bit_desc.number_bases],
        'metrics': metrics
    }
    os.makedirs('analysis/UQEBM', exist_ok=True)
    with open(f'analysis/UQEBM/{file_prefix}_{current_time}.json', 'w') as file:
        json.dump(best_bit_desc_data, file, indent=4)
    print(f"Best bit description saved to analysis/UQEBM/{file_prefix}_{current_time}.json")

class BitDescriptionModel(BaseEstimator, ClassifierMixin):
    def __init__(self, range_min=0, range_max=100, number_bases=None, quantum_states=None):
        self.range_min = range_min
        self.range_max = range_max
        self.number_bases = number_bases if number_bases is not None else [1, np.pi, np.e, 5, 10, 13, 60]
        self.quantum_states = quantum_states if quantum_states is not None else {}
        self.classes_ = None

    def fit(self, X, y):
        self.classes_ = np.unique(y)
        self.model_ = IntegratedBitDescription(self.range_min, self.range_max, self.number_bases, self.quantum_states)
        return self

    def predict(self, X):
        # Implement prediction logic using the model
        predictions = np.zeros(len(X))  # Placeholder, should be replaced with real logic
        return predictions

    def predict_proba(self, X):
        # Implement prediction probabilities logic if needed
        proba = np.zeros((len(X), len(self.classes_)))
        return proba

    def score(self, X, y):
        predictions = self.predict(X)
        return accuracy_score(y, predictions)

def optimize_and_train_model(X_train, y_train, X_test, y_test):
    # Grid search setup
    bit_model = BitDescriptionModel()
    param_grid = {'number_bases': [[1, np.pi, np.e, 5, 10, 13, 60]]}
    best_params_grid = perform_grid_search(param_grid, bit_model, X_train, y_train)
    logging.info(f"Best parameters from grid search: {best_params_grid}")

    # Bayesian optimization setup
    param_bayes = {'number_bases': [(1, np.pi, np.e, 5, 10, 13, 60)]}
    best_params_bayes = perform_bayesian_optimization(param_bayes, bit_model, X_train, y_train)
    logging.info(f"Best parameters from Bayesian optimization: {best_params_bayes}")

    # Combine best parameters
    combined_bases = list(set(best_params_grid['number_bases'] + [best_params_bayes['number_bases']]))
    logging.info(f"Combined best bases: {combined_bases}")

    # Train final model with combined parameters
    final_model = BitDescriptionModel(number_bases=combined_bases)
    final_model.fit(X_train, y_train)

    # Evaluate the model on test data
    test_score = final_model.score(X_test, y_test)
    logging.info(f"Final model accuracy on test data: {test_score}")

    # Save the final model description
    save_best_bit_description(final_model.model_, {"test_accuracy": test_score})


    def describe_layers(self):
        descriptions = []
        ranges = [
            (-1, 0, 1), (-np.pi, 0, np.pi), (-5, 0, 5), (-10, 0, 10),
            (-13, 0, 13), (-60, 0, 60), (-360, 0, 360)
        ]
        for i, base in enumerate(self.number_bases):
            descriptions.append({
                'layer': i,
                'range': ranges[i] if i < len(ranges) else (-base, 0, base),
                'quantum_description': self.quantum_states.get(i, {}) if self.quantum_states else {}
            })
        return descriptions

def perform_grid_search(parameters, model, X_train, y_train):
    grid_search = GridSearchCV(model, parameters, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    return grid_search.best_params_

from skopt.space import Categorical

def perform_bayesian_optimization(parameters, model, X_train, y_train):
    search_space = {
        'number_bases': Categorical([1, np.pi, np.e, 5, 10, 13, 60])
    }

    bayes_search = BayesSearchCV(model, search_space, n_iter=32, cv=5, scoring='accuracy')
    bayes_search.fit(X_train, y_train)
    return bayes_search.best_params_

def load_previous_best(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return None

def save_best_bit_description(best_bit_desc, metrics, file_prefix='best_bit_desc'):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    best_bit_desc_data = {
        'range_min': str(best_bit_desc.range_min),
        'range_max': str(best_bit_desc.range_max),
        'number_bases': [str(base) for base in best_bit_desc.number_bases],
        'metrics': metrics
    }
    os.makedirs('analysis/UQEBM', exist_ok=True)
    with open(f'analysis/UQEBM/{file_prefix}_{current_time}.json', 'w') as file:
        json.dump(best_bit_desc_data, file, indent=4)
    print(f"Best bit description saved to analysis/UQEBM/{file_prefix}_{current_time}.json")




def main():
    # Load dataset
    data = load_iris()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define bases and quantum states
    alternative_bases = [1, np.pi, np.e, 5, 10, 13, 60]
    previous_best_file = 'path_to_previous_best_file.json'
    previous_best = load_previous_best(previous_best_file)

    if previous_best:
        bases = [Decimal(base) for base in previous_best['number_bases']]
    else:
        bases = alternative_bases

    # Create the integrated bit description instance
    integrated_bit_desc = IntegratedBitDescription(
        range_min=0, 
        range_max=100, 
        number_bases=bases, 
        quantum_states=quantum_states
    )

    # Example decimal value to encode
    decimal_value = 1234567890
    
    # Encode the decimal value into quantum encoded bits
    quantum_encoded_bits = integrated_bit_desc.encode_with_quantum(decimal_value)
    
    # Decode the quantum encoded bits back into the original decimal value and quantum states
    reconstructed_decimal, reconstructed_quantum_states = integrated_bit_desc.decode_with_quantum(quantum_encoded_bits)

    # Output results
    print("Original decimal value:", decimal_value)
    print("Quantum encoded bits:", quantum_encoded_bits)
    print("Reconstructed decimal value:", reconstructed_decimal)
    print("Reconstructed quantum states:", reconstructed_quantum_states)

    # Describe layers
    layer_descriptions = integrated_bit_desc.describe_layers()
    for description in layer_descriptions:
        print(f"Layer {description['layer']} range: {description['range']} quantum description: {description['quantum_description']}")

    # Example metrics computation
    y_true = [0, 1, 2, 3, 0, 2, 1, 3, 0, 2, 1, 3]
    y_pred = [0, 1, 1, 3, 0, 3, 2, 3, 0, 1, 2, 2]
    y_proba = [
        [0.9, 0.05, 0.03, 0.02],
        [0.2, 0.7, 0.05, 0.05],
        [0.1, 0.5, 0.3, 0.1],
        [0.05, 0.1, 0.15, 0.7],
        [0.85, 0.1, 0.03, 0.02],
        [0.15, 0.1, 0.6, 0.15],
        [0.2, 0.4, 0.3, 0.1],
        [0.05, 0.05, 0.1, 0.8],
        [0.8, 0.15, 0.03, 0.02],
        [0.25, 0.5, 0.2, 0.05],
        [0.2, 0.5, 0.25, 0.05],
        [0.1, 0.2, 0.6, 0.1]
    ]

    epoch_times = [0.12, 0.25, 0.18, 0.15, 0.22, 0.27, 0.2, 0.19, 0.14, 0.24, 0.21, 0.23]
    k_values = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    q_values = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    epsilon_values = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

    # Compute and save metrics
    metrics = compute_metrics(y_true, y_pred, y_proba, epoch_times, k_values, q_values, epsilon_values)
    
    # Print metrics to console
    print("Metrics Dump:")
    for key, value in metrics.items():
        print(f"{key}: {value}")

    # Save metrics to JSON
    save_metrics_to_json(metrics)

    # Save best bit description
    metrics_summary = {"accuracy": metrics['accuracy'], "precision": metrics['precision']}
    save_best_bit_description(integrated_bit_desc, metrics_summary)

    # Define the model
    bit_model = BitDescriptionModel()

    # Perform grid search
    param_grid = {'number_bases': [[1, np.pi, np.e, 5, 10, 13, 60]]}
    best_params = perform_grid_search(param_grid, bit_model, X_train, y_train)
    print("Best parameters from grid search:", best_params)

    # Perform Bayesian optimization
    param_bayes = {'number_bases': [(1, np.pi, np.e, 5, 10, 13, 60)]}
    best_params_bayes = perform_bayesian_optimization(param_bayes, bit_model, X_train, y_train)
    print("Best parameters from Bayesian optimization:", best_params_bayes)

if __name__ == "__main__":
    main()
