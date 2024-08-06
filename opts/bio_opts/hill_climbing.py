# hill_climbing.py

import numpy as np
import sys
import os

# Adjust the system path to import from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bit_description import BitDescription, scales, quantum_bases


def objective_function(x):
    return -np.sum((x - 0.5)**2)

class HillClimber:
    def __init__(self, dimensionality, num_iterations, epsilon, early_stopping_rounds=50):
        self.dimensionality = dimensionality
        self.num_iterations = num_iterations
        self.epsilon = epsilon
        self.early_stopping_rounds = early_stopping_rounds
        self.current_solution = np.random.uniform(0, 1, dimensionality)
        self.current_fitness = objective_function(self.current_solution)
        self.best_solution = np.copy(self.current_solution)
        self.best_fitness = self.current_fitness
        self.no_improvement_count = 0

        # Initialize Bit and TetraLogix
        self.bit_desc = BitDescription(range_min=0, range_max=100, bases=scales, quantum_bases=quantum_bases)
        self.integrated_system = IntegratedSystem(self.bit_desc)

    def perturb(self):
        new_solution = self.current_solution + np.random.uniform(-self.epsilon, self.epsilon, self.dimensionality)
        return np.clip(new_solution, 0, 1)

    def log_iteration(self, iteration):
        print(f"Iteration {iteration + 1}/{self.num_iterations}, Current Best Fitness: {self.best_fitness}")

    def optimize(self):
        for iteration in range(self.num_iterations):
            new_solution = self.perturb()
            new_fitness = objective_function(new_solution)

            if new_fitness > self.current_fitness:
                self.current_solution = new_solution
                self.current_fitness = new_fitness
                self.no_improvement_count = 0
            else:
                self.no_improvement_count += 1

            if self.current_fitness > self.best_fitness:
                self.best_solution = np.copy(self.current_solution)
                self.best_fitness = self.current_fitness

            self.log_iteration(iteration)

            if self.no_improvement_count >= self.early_stopping_rounds:
                print(f"No improvement for {self.early_stopping_rounds} iterations. Stopping early.")
                break

        return self.best_solution, self.best_fitness

# Example usage
if __name__ == "__main__":
    hc = HillClimber(dimensionality=10, num_iterations=1000, epsilon=0.1)
    best_solution, best_fitness = hc.optimize()
    print(f"Best Solution: {best_solution}, Best Fitness: {best_fitness}")
