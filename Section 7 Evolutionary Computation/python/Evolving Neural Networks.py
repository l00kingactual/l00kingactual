import logging
import json
import random
import numpy as np
from datetime import datetime, timezone
import tensorflow as tf
import matplotlib.pyplot as plt

# Set up logging
logger = logging.getLogger('genetic_algorithm_logger')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log_to_json(level, message, **kwargs):
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "message": message,
        "extra": kwargs
    }
    logger.log(level, json.dumps(log_entry))

# Define the mock dataset
data = np.random.rand(100, 10)
labels = np.random.rand(100, 1)

# Genetic Algorithm setup
POPULATION_SIZE = 10
GENERATIONS = 20
MUTATION_RATE = 0.1

@tf.keras.utils.register_keras_serializable()
class CustomDense(tf.keras.layers.Dense):
    pass

class NeuralNetwork:
    def __init__(self, architecture):
        self.model = self.build_model(architecture)
        self.fitness = 0

    def build_model(self, architecture):
        model = tf.keras.Sequential()
        for i, layer_config in enumerate(architecture):
            if layer_config['class_name'] == 'InputLayer':
                input_shape = layer_config['config'].get('batch_input_shape', [None, 10])[1:]
                model.add(tf.keras.Input(shape=input_shape))
            else:
                layer = self.custom_layer_deserialize(layer_config)
                model.add(layer)
        model.compile(optimizer='adam', loss='mse')
        return model

    def custom_layer_deserialize(self, layer_config):
        try:
            if layer_config['class_name'] == 'Dense':
                return CustomDense.from_config(layer_config['config'])
            else:
                return tf.keras.layers.deserialize(layer_config)
        except KeyError as e:
            log_to_json(logging.ERROR, f"KeyError during deserialization: {e}")
            raise

    def evaluate_fitness(self, data, labels):
        try:
            if self.model is None or data is None or labels is None:
                raise ValueError("Model, data, or labels are not properly initialized.")
            self.fitness = self.model.evaluate(data, labels, verbose=0)
        except Exception as e:
            log_to_json(logging.ERROR, f"Error during fitness evaluation: {e}")
            raise

    @staticmethod
    def crossover(parent1, parent2):
        try:
            parent1_config = parent1.model.get_config()['layers']
            parent2_config = parent2.model.get_config()['layers']
            child_config = []

            for p1_layer, p2_layer in zip(parent1_config, parent2_config):
                chosen_layer = p1_layer if random.random() > 0.5 else p2_layer
                child_config.append(chosen_layer)

            # Ensure the first layer is always an InputLayer with the correct input shape
            if child_config[0]['class_name'] != 'InputLayer':
                input_shape = parent1_config[0]['config'].get('batch_input_shape', [None, 10])[1:]
                child_config.insert(0, {
                    'class_name': 'InputLayer',
                    'config': {'batch_input_shape': (None, *input_shape), 'dtype': 'float32', 'sparse': False, 'name': 'input_1'}
                })

            return NeuralNetwork(child_config)
        except KeyError as e:
            log_to_json(logging.ERROR, f"KeyError during crossover: {e}")
            raise
        except Exception as e:
            log_to_json(logging.ERROR, f"Error during crossover: {e}")
            raise

    def mutate(self):
        try:
            if random.random() < MUTATION_RATE:
                layer_index = random.randint(1, len(self.model.layers) - 1)  # Avoid mutating the input layer
                layer = self.model.layers[layer_index]
                if isinstance(layer, CustomDense):
                    units = layer.units + random.randint(-10, 10)
                    units = max(1, units)
                    new_layer = CustomDense(units=units, activation=layer.activation)
                    self.model.layers[layer_index] = new_layer
                    self.model.compile(optimizer='adam', loss='mse')
        except Exception as e:
            log_to_json(logging.ERROR, f"Error during mutation: {e}")
            raise

def genetic_algorithm_nn():
    try:
        population = [NeuralNetwork(architecture=[
            {'class_name': 'InputLayer', 'config': {'batch_input_shape': (None, 10), 'dtype': 'float32', 'sparse': False, 'name': 'input_1'}},
            {'class_name': 'Dense', 'config': {'units': 10, 'activation': 'relu', 'use_bias': True, 'kernel_initializer': {'class_name': 'GlorotUniform', 'config': {'seed': None}}, 'bias_initializer': {'class_name': 'Zeros', 'config': {}}, 'kernel_regularizer': None, 'bias_regularizer': None, 'activity_regularizer': None, 'kernel_constraint': None, 'bias_constraint': None, 'name': 'dense_1'}},
            {'class_name': 'Dense', 'config': {'units': 1, 'activation': 'linear', 'use_bias': True, 'kernel_initializer': {'class_name': 'GlorotUniform', 'config': {'seed': None}}, 'bias_initializer': {'class_name': 'Zeros', 'config': {}}, 'kernel_regularizer': None, 'bias_regularizer': None, 'activity_regularizer': None, 'kernel_constraint': None, 'bias_constraint': None, 'name': 'dense_2'}}
        ]) for _ in range(POPULATION_SIZE)]

        fitness_history = []

        for generation in range(GENERATIONS):
            log_to_json(logging.INFO, "Generation", generation=generation)
            for nn in population:
                nn.evaluate_fitness(data, labels)
            population.sort(key=lambda nn: nn.fitness)
            fitness_history.append(population[0].fitness)
            next_generation = population[:POPULATION_SIZE // 2]
            while len(next_generation) < POPULATION_SIZE:
                parents = random.sample(population[:POPULATION_SIZE // 4], 2)
                child = NeuralNetwork.crossover(parents[0], parents[1])
                child.mutate()
                next_generation.append(child)
            population = next_generation

        best_nn = min(population, key=lambda nn: nn.fitness)
        log_to_json(logging.INFO, "Best Neural Network", fitness=best_nn.fitness)

        # Plotting fitness history
        plt.plot(fitness_history)
        plt.title('Fitness Over Generations')
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        plt.show()

        return best_nn
    except Exception as e:
        log_to_json(logging.ERROR, f"Error in genetic algorithm: {e}")
        raise

best_nn = genetic_algorithm_nn()
