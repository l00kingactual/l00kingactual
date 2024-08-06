import numpy as np
import random
import sys
import os

# Adjust the system path to import from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bit_description import BitDescription, scales, quantum_bases

from optimisation.hill_climbing import HillClimber
from local_search import hill_climbing as local_hill_climbing, simulated_annealing, nearest_neighbor_heuristic
from genetic_algorithm import GeneticAlgorithm
from environment import Environment  # Ensure this import is correct

class CoreLogic:
    def __init__(self, problem_size, environment_params):
        self.problem_size = problem_size
        self.environment_params = environment_params
        self.env = Environment(*environment_params)
        self.bit_desc = self.env.bit_desc
        self.integrated_system = self.env.integrated_system

    def objective_function(self, x):
        # Dummy objective function; replace with actual problem-specific function
        return -np.sum((x - 0.5)**2)

    def hill_climbing(self, num_iterations=1000, epsilon=0.1):
        hill_climber = HillClimber(self.problem_size, num_iterations, epsilon)
        best_solution, best_fitness = hill_climber.optimize()
        return best_solution, best_fitness

    def local_search(self, distance_matrix, max_iterations=1000):
        initial_solution = np.arange(self.problem_size)
        hc_solution, hc_distance = local_hill_climbing(initial_solution, distance_matrix, max_iterations)
        sa_solution, sa_distance = simulated_annealing(initial_solution, distance_matrix, num_iterations=max_iterations)
        return hc_solution, hc_distance, sa_solution, sa_distance

    def genetic_algorithm(self, population_size=100, num_generations=100, mutation_rate=0.01):
        ga = GeneticAlgorithm(self.problem_size, population_size, num_generations, mutation_rate)
        best_solution, best_fitness = ga.run()
        return best_solution, best_fitness

    def apply_environmental_factors(self, data):
        transformed_env = self.env.transform_environment()
        return transformed_env

    def execute(self):
        # Example of executing a hill climbing algorithm
        best_solution_hc, best_fitness_hc = self.hill_climbing()
        print(f"Hill Climbing: Best solution = {best_solution_hc}, Best fitness = {best_fitness_hc}")

        # Example of executing a local search algorithm
        distance_matrix = np.random.rand(self.problem_size, self.problem_size)
        distance_matrix = (distance_matrix + distance_matrix.T) / 2  # Make it symmetric
        np.fill_diagonal(distance_matrix, 0)

        hc_solution, hc_distance, sa_solution, sa_distance = self.local_search(distance_matrix)
        print(f"Local Search - Hill Climbing: Best distance = {hc_distance}, Solution = {hc_solution}")
        print(f"Local Search - Simulated Annealing: Best distance = {sa_distance}, Solution = {sa_solution}")

        # Example of executing a genetic algorithm
        best_solution_ga, best_fitness_ga = self.genetic_algorithm()
        print(f"Genetic Algorithm: Best solution = {best_solution_ga}, Best fitness = {best_fitness_ga}")

        # Apply environmental factors
        data = np.random.rand(10)
        transformed_data = self.apply_environmental_factors(data)
        print(f"Transformed data with environmental factors: {transformed_data}")

# Example usage
if __name__ == "__main__":
    environment_params = (25, 70, 12, 5, 2)  # Example parameters: temperature, humidity, daylight, wind, tide
    core_logic = CoreLogic(problem_size=10, environment_params=environment_params)
    core_logic.execute()
