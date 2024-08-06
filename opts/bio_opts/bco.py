import numpy as np
import random
import sys
import os
#from environment import Environment


import os
import sys
import numpy as np

# Adjust the system path to import from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bit_description import BitDescription, scales, quantum_bases
from tetralogix import IntegratedSystem

class Environment:
    def __init__(self, temperature, humidity, daylight, wind, tide):
        self.temperature = temperature
        self.humidity = humidity
        self.daylight = daylight
        self.wind = wind
        self.tide = tide

        # Initialize BitDescription and IntegratedSystem
        self.bit_desc = BitDescription(range_min=0, range_max=100, bases=scales, quantum_bases=quantum_bases)
        self.integrated_system = IntegratedSystem(bit_description=self.bit_desc)

    def get_environment_vector(self):
        return np.array([self.temperature, self.humidity, self.daylight, self.wind, self.tide])

    def transform_environment(self):
        env_vector = self.get_environment_vector()
        env_bit_vector = self.bit_desc.vectorized_decimal_to_bit(env_vector)
        transformed_env = self.integrated_system.execute(env_bit_vector.reshape(1, -1))  # Reshape to ensure correct dimensions
        return transformed_env.flatten()


# Adjust the system path to import from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bit_description import BitDescription, scales, quantum_bases
from tetralogix import IntegratedSystem

class Bee:
    def __init__(self, position, fitness_func, bit_desc, integrated_system):
        self.position = position
        self.fitness_func = fitness_func
        self.bit_desc = bit_desc
        self.integrated_system = integrated_system
        self.fitness = self.evaluate_fitness()
        self.pbest_position = position
        self.pbest_fitness = self.fitness

    def evaluate_fitness(self):
        return self.fitness_func(self.position)

    def update_position(self, new_position):
        self.position = new_position
        self.fitness = self.evaluate_fitness()
        if self.fitness < self.pbest_fitness:
            self.pbest_position = new_position
            self.pbest_fitness = self.fitness

class BeeColonyOptimization:
    def __init__(self, num_bees, num_iterations, fitness_func, env):
        self.num_bees = num_bees
        self.num_iterations = num_iterations
        self.fitness_func = fitness_func
        self.env = env

        # Initialize environment transformations
        self.bit_desc = env.bit_desc
        self.integrated_system = env.integrated_system

        self.bees = [Bee(self.random_position(), self.fitness_func, self.bit_desc, self.integrated_system) for _ in range(self.num_bees)]

    def random_position(self):
        return np.random.rand(self.fitness_func.dimension)

    def run(self):
        global_best_fitness = float('inf')
        global_best_position = None

        for iteration in range(self.num_iterations):
            for bee in self.bees:
                new_position = self.explore(bee.position)
                bee.update_position(new_position)
                if bee.fitness < global_best_fitness:
                    global_best_fitness = bee.fitness
                    global_best_position = bee.position

            self.apply_environmental_factors()

        return global_best_position, global_best_fitness

    def explore(self, position):
        new_position = position + np.random.uniform(-1, 1, len(position))
        new_position = np.clip(new_position, 0, 1)  # Assuming the position is within [0, 1]
        return new_position

    def apply_environmental_factors(self):
        # Integrate environmental transformations
        transformed_env = self.env.transform_environment()
        temp_factor = transformed_env[0]
        humidity_factor = transformed_env[1]
        daylight_factor = transformed_env[2]
        wind_factor = transformed_env[3]
        tide_factor = transformed_env[4]

        # Apply factors to bees' positions
        for bee in self.bees:
            bee.position *= (1 + temp_factor / 100)
            bee.position *= (1 + humidity_factor / 100)
            bee.position *= (1 + daylight_factor / 100)
            bee.position *= (1 + wind_factor / 100)
            bee.position *= (1 + tide_factor / 100)
            bee.position = np.clip(bee.position, 0, 1)  # Ensure positions stay within bounds

# Example fitness function
class FitnessFunction:
    def __init__(self, dimension):
        self.dimension = dimension

    def __call__(self, position):
        return np.sum(position ** 2)  # Example: Sphere function

# Example usage
if __name__ == '__main__':
    env = Environment(temperature=25, humidity=70, daylight=12, wind=5, tide=2)
    fitness_func = FitnessFunction(dimension=10)
    bco = BeeColonyOptimization(num_bees=10, num_iterations=100, fitness_func=fitness_func, env=env)
    best_position, best_fitness = bco.run()
    print(f"Best Position: {best_position}, Best Fitness: {best_fitness}")
