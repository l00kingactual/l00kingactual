import numpy as np
import json
import os
from datetime import datetime
from decimal import Decimal, getcontext
import logging
from sklearn.model_selection import GridSearchCV, train_test_split
from skopt import BayesSearchCV
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from compute_metrics import compute_metrics, save_metrics_to_json
from quantum.quantum_states import quantum_states
from neural_network import build_enhanced_nn as NeuralNetworkModel, train_neural_network
from epsilon_greedy import epsilon_greedy
from skopt.space import Categorical
from sklearn.base import BaseEstimator, ClassifierMixin

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Set precision for decimal operations
getcontext().prec = 1000

# Functions for encoding and decoding quantum bits
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

# EnhancedBitDescription class
class EnhancedBitDescription:
    def __init__(self, range_min, range_max, number_bases, quantum_states):
        self.range_min = Decimal(range_min)
        self.range_max = Decimal(range_max)
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
            # Calculate initial coordinate
            coord = (remaining_value % base).quantize(Decimal('1.'))
            remaining_value = (remaining_value // base).quantize(Decimal('1.'))
            
            # Quantum adjustment
            quantum_adjustment = self.quantum_states.get(i, {}).get('n', 1)
            refined_coord = coord * Decimal(quantum_adjustment)
            
            # Scale adjustment
            scale = self.scales[i] if i < len(self.scales) else 1
            refined_coord *= Decimal(scale)
            
            # Append the refined coordinate
            coordinates.append(refined_coord)
        
        return coordinates


    def _convert_from_layers(self, coordinates):
        value = Decimal(0)
        multiplier = Decimal(1)
        for i, (coord, base) in enumerate(zip(coordinates, self.number_bases)):
            # Apply scale adjustment
            scale = self.scales[i] if i < len(self.scales) else 1
            scaled_coord = coord / Decimal(scale)
            
            # Reconstruct the value
            value += scaled_coord * multiplier
            multiplier *= base
        
        return value


# IntegratedBitDescription class that extends EnhancedBitDescription
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


# Model class integrating bit description with neural networks

# updated 02:21 20/08/2024
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
        self.neural_net.train(X, y)
        return self

    def predict(self, X):
        if self.neural_net is None:
            raise ValueError("Neural network is not initialized. Call `initialize_neural_net` first.")
        predictions = self.neural_net.predict(X)
        return predictions

    def predict_proba(self, X):
        if self.neural_net is None:
            raise ValueError("Neural network is not initialized. Call `initialize_neural_net` first.")
        return self.neural_net.predict_proba(X)

    def score(self, X, y):
        predictions = self.predict(X)
        return accuracy_score(y, predictions)



# Updated Optimization functions

def perform_grid_search(param_grid, model, X_train, y_train):
    """
    Performs grid search to find the best hyperparameters for the given model.
    """
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    best_params = grid_search.best_params_
    logger.info(f"Best parameters from Grid Search: {best_params}")
    return best_params

def perform_bayesian_optimization(param_bayes, model, X_train, y_train):
    """
    Performs Bayesian optimization to find the best hyperparameters for the given model.
    """
    search_space = {
        'number_bases': Categorical(param_bayes['number_bases']),
        'scales': Categorical(param_bayes['scales'])
    }
    bayes_search = BayesSearchCV(estimator=model, search_spaces=search_space, n_iter=32, cv=5, scoring='accuracy')
    bayes_search.fit(X_train, y_train)
    best_params = bayes_search.best_params_
    logger.info(f"Best parameters from Bayesian Optimization: {best_params}")
    return best_params


# additional optimization functions

from sklearn.model_selection import RandomizedSearchCV

def perform_random_search(param_dist, model, X_train, y_train, n_iter=100):
    random_search = RandomizedSearchCV(estimator=model, param_distributions=param_dist, n_iter=n_iter, cv=5, scoring='accuracy', random_state=42)
    random_search.fit(X_train, y_train)
    best_params = random_search.best_params_
    logger.info(f"Best parameters from Random Search: {best_params}")
    return best_params


from scipy.optimize import dual_annealing

def perform_simulated_annealing(objective_func, bounds, X_train, y_train):
    result = dual_annealing(objective_func, bounds, args=(X_train, y_train))
    logger.info(f"Best parameters from Simulated Annealing: {result.x}")
    return result.x


from deap import base, creator, tools, algorithms

def perform_genetic_algorithm(objective_func, param_ranges, n_gen=50, population_size=100):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    for i, (low, high) in enumerate(param_ranges):
        toolbox.register(f"attr_{i}", np.random.uniform, low, high)
    toolbox.register("individual", tools.initCycle, creator.Individual, [toolbox.__getattribute__(f"attr_{i}") for i in range(len(param_ranges))], n=1)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", objective_func)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    population = toolbox.population(n=population_size)
    algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.2, ngen=n_gen, verbose=False)

    best_individual = tools.selBest(population, k=1)[0]
    logger.info(f"Best parameters from Genetic Algorithm: {best_individual}")
    return best_individual


from hyperopt import fmin, tpe, hp, Trials

def perform_hyperopt_optimization(objective_func, space, max_evals=100):
    trials = Trials()
    best = fmin(fn=objective_func, space=space, algo=tpe.suggest, max_evals=max_evals, trials=trials)
    logger.info(f"Best parameters from Hyperopt: {best}")
    return best


import optuna

def perform_optuna_optimization(objective_func, n_trials=100):
    study = optuna.create_study(direction='maximize')
    study.optimize(objective_func, n_trials=n_trials)
    logger.info(f"Best parameters from Optuna: {study.best_params}")
    return study.best_params


import cma

def perform_cma_es(objective_func, initial_guess, sigma, bounds):
    es = cma.CMAEvolutionStrategy(initial_guess, sigma, {'bounds': bounds})
    es.optimize(objective_func)
    logger.info(f"Best parameters from CMA-ES: {es.result.xbest}")
    return es.result.xbest


# Save and load utility functions
import os
import json
import logging
from datetime import datetime
from decimal import Decimal

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



def load_previous_best(file_path):
    """Load the best bit description from a JSON file if it exists."""
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Example of data validation (add your own conditions)
                if 'range_min' in data and 'range_max' in data and 'number_bases' in data:
                    return data
                else:
                    print(f"Data format in {file_path} is not as expected.")
                    return None
        else:
            print(f"File {file_path} not found.")
            return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {file_path}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error occurred while loading {file_path}: {e}")
        return None


def save_metrics_to_json(metrics, directory='analysis/UQEBM_v103'):
    try:
        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)
        logger.debug(f"Directory {directory} checked/created successfully.")

        # Create a filename with a timestamp
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'metrics_{current_time}.json'
        filepath = os.path.join(directory, filename)

        logger.debug(f"Saving metrics to {filepath}...")

        # Write the metrics to the JSON file
        with open(filepath, 'w') as file:
            json.dump(metrics, file, indent=4)
        
        print(f"Metrics saved to {filepath}")
        logging.info(f"Metrics saved to {filepath}")
        
    except Exception as e:
        logger.error(f"Failed to save metrics: {e}")
        print(f"Failed to save metrics: {e}")

def save_best_bit_description(best_bit_desc, metrics, file_prefix='best_bit_desc'):
    try:
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        best_bit_desc_data = {
            'range_min': str(best_bit_desc['range_min']),
            'range_max': str(best_bit_desc['range_max']),
            'number_bases': [str(base) for base in best_bit_desc['number_bases']],
            'metrics': metrics
        }
        os.makedirs('analysis/UQEBM_v103', exist_ok=True)
        
        # Saving to a temporary file first
        temp_file_path = f'analysis/UQEBM_v103/{file_prefix}_{current_time}.tmp'
        final_file_path = f'analysis/UQEBM_v103/{file_prefix}_{current_time}.json'
        
        with open(temp_file_path, 'w') as file:
            json.dump(best_bit_desc_data, file, indent=4)
        
        # Atomically move the temporary file to the final file path
        os.rename(temp_file_path, final_file_path)
        print(f"Best bit description saved to {final_file_path}")
    except Exception as e:
        logger.error(f"Unexpected error occurred while saving best bit description: {e}")
        print(f"Unexpected error occurred while saving best bit description: {e}")



    

# Main function


import numpy as np
import os
import logging
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from compute_metrics import compute_metrics, save_metrics_to_json
from neural_network import build_enhanced_nn as NeuralNetworkModel, train_neural_network
from epsilon_greedy import create_epsilon_greedy_space

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        # Load sample data (Iris dataset for this example)
        data = load_iris()
        X, y = data.data, data.target

        # Split the data into training, validation, and test sets
        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

        # Initialize and train the neural network
        model = NeuralNetworkModel(
            input_shape=X_train.shape[1:], 
            num_classes=len(np.unique(y)), 
            num_layers=5, 
            units_0=64, 
            dropout_0=0.2, 
            units_1=32, 
            dropout_1=0.2, 
            learning_rate=0.001
        )

        # Pass validation data to the training function
        train_neural_network(model, X_train, y_train, X_val, y_val, epochs=10)

        # Make predictions
        y_pred = model.predict(X_test).argmax(axis=1)
        y_proba = model.predict(X_test)

        # Generate the epsilon greedy space
        epsilon_greedy_space = create_epsilon_greedy_space()  # Correctly call the function

        # Compute some example epoch times, k, q, and epsilon values
        epoch_times = np.random.uniform(0.1, 0.3, size=len(y_pred)).tolist()
        k_values = np.random.choice([2, 4, 6, 8], size=len(y_pred)).tolist()
        q_values = np.random.choice([1, 2, 3], size=len(y_pred)).tolist()
        epsilon_values = np.random.choice(epsilon_greedy_space, size=len(y_pred)).tolist()

        # Compute the metrics
        metrics = compute_metrics(y_test, y_pred, y_proba, epoch_times, k_values, q_values, epsilon_values)

        # Save the metrics to the 'UQEBM_v103' directory with a timestamp
        save_metrics_to_json(metrics, directory='analysis/UQEBM_v103')

        logger.info("Metrics computation and saving complete.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
