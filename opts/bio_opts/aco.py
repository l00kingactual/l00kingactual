import numpy as np
import json
import os
from datetime import datetime
import logging
from sklearn.cluster import KMeans
from UQEBM import EnhancedBitDescription, IntegratedBitDescription

# Import value spaces
from epsilon_value_space import epsilon_value_space
from q_value_space import q_value_space
from k_value_space import k_value_space

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Environment:
    def __init__(self, temperature, humidity, daylight, wind, tide):
        self.temperature = temperature
        self.humidity = humidity
        self.daylight = daylight
        self.wind = wind
        self.tide = tide
        self.range_min = 0
        self.range_max = 100

class AntColonyOptimization:
    def __init__(self, num_ants, num_iterations, decay, alpha, beta, env, quantum_states):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        self.env = env
        self.quantum_states = quantum_states
        self.epsilon = np.random.choice(epsilon_value_space)
        self.q = np.random.choice(q_value_space)
        self.k = np.random.choice(k_value_space)
        self.pheromone = np.ones((self.env.range_max - self.env.range_min, self.env.range_max - self.env.range_min))
        self.bit_desc = IntegratedBitDescription(env.range_min, env.range_max, [1, np.pi, 5, 10, 13, 60, 360], quantum_states)

    def run(self):
        best_solutions = []
        best_costs = []
        epsilon_values = []
        q_values = []
        k_values = []
        role_assignments = ['forager', 'resource_gatherer', 'defender']

        for iteration in range(self.num_iterations):
            all_solutions = self.construct_solutions()
            self.update_pheromones(all_solutions)
            best_solution, best_cost = self.get_best_solution(all_solutions)
            best_solutions.append(best_solution)
            best_costs.append(best_cost)
            epsilon_values.append(self.epsilon)
            q_values.append(self.q)
            k_values.append(self.k)

            self.adapt_parameters(all_solutions, role_assignments, iteration)
            logger.info(f"Iteration {iteration}: Avg Cost = {np.mean([sol['cost'] for sol in all_solutions])}, Min Cost = {min([sol['cost'] for sol in all_solutions])}, Max Cost = {max([sol['cost'] for sol in all_solutions])}")
            logger.info(f"Iteration {iteration}: Epsilon = {self.epsilon}, Q = {self.q}, K = {self.k}")

        self.save_results(best_solutions, best_costs, epsilon_values, q_values, k_values)
        return best_solutions, best_costs, epsilon_values, q_values, k_values

    def construct_solutions(self):
        all_solutions = []
        for _ in range(self.num_ants):
            solution = self.construct_solution()
            all_solutions.append(solution)
        return all_solutions

    def construct_solution(self):
        solution = {}
        cost = np.random.uniform(self.env.range_min, self.env.range_max)
        solution['path'] = [cost]
        solution['cost'] = cost
        return solution

    def update_pheromones(self, all_solutions):
        self.pheromone *= self.decay
        for solution in all_solutions:
            path = solution['path']
            cost = solution['cost']
            for i in range(len(path) - 1):
                self.pheromone[path[i]][path[i + 1]] += 1.0 / cost

    def get_best_solution(self, all_solutions):
        best_solution = min(all_solutions, key=lambda x: x['cost'])
        return best_solution, best_solution['cost']

    def adapt_parameters(self, all_solutions, role_assignments, iteration):
        role_clusters = self.cluster_roles(all_solutions, role_assignments)
        for role, solutions in role_clusters.items():
            if role == 'forager':
                self.adapt_epsilon(solutions, iteration)
            elif role == 'resource_gatherer':
                self.adapt_q(solutions, iteration)
            elif role == 'defender':
                self.adapt_k(solutions, iteration)

    def cluster_roles(self, all_solutions, role_assignments):
        solutions_array = np.array([sol['cost'] for sol in all_solutions]).reshape(-1, 1)
        kmeans = KMeans(n_clusters=len(role_assignments))
        labels = kmeans.fit_predict(solutions_array)
        role_clusters = {role: [] for role in role_assignments}
        for label, solution in zip(labels, all_solutions):
            role = role_assignments[label]
            role_clusters[role].append(solution)
        return role_clusters

    def adapt_epsilon(self, solutions, iteration):
        avg_cost = np.mean([sol['cost'] for sol in solutions])
        adjustment_factor = np.random.uniform(0.95, 1.05)
        self.epsilon = max(self.env.range_min, min(self.env.range_max, self.epsilon * adjustment_factor + avg_cost * 0.005))
        if iteration % 50 == 0:
            self.epsilon = self.epsilon * (1 + np.random.uniform(-0.1, 0.1))
        self.epsilon = np.random.choice(epsilon_value_space)

    def adapt_q(self, solutions, iteration):
        avg_cost = np.mean([sol['cost'] for sol in solutions])
        adjustment_factor = np.random.uniform(0.95, 1.05)
        self.q = max(self.env.range_min, min(self.env.range_max, self.q * adjustment_factor + avg_cost * 0.005))
        if iteration % 50 == 0:
            self.q = self.q * (1 + np.random.uniform(-0.1, 0.1))
        self.q = np.random.choice(q_value_space)

    def adapt_k(self, solutions, iteration):
        avg_cost = np.mean([sol['cost'] for sol in solutions])
        adjustment_factor = np.random.uniform(0.95, 1.05)
        self.k = max(self.env.range_min, min(self.env.range_max, self.k * adjustment_factor + avg_cost * 0.005))
        if iteration % 50 == 0:
            self.k = self.k * (1 + np.random.uniform(-0.1, 0.1))
        self.k = np.random.choice(k_value_space)

    def save_results(self, best_solutions, best_costs, epsilon_values, q_values, k_values):
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        directory = "analysis/aoc"
        os.makedirs(directory, exist_ok=True)
        file_name = f"aoc_results_{current_datetime}.json"
        file_path = os.path.join(directory, file_name)
        results = {
            "best_solutions": best_solutions,
            "best_costs": best_costs,
            "epsilon_values": epsilon_values,
            "q_values": q_values,
            "k_values": k_values
        }
        with open(file_path, 'w') as json_file:
            json.dump(results, json_file, indent=4)
        logger.info(f"Results saved to {file_path}")

if __name__ == "__main__":
    from quantum_states import quantum_states
    
    env = Environment(temperature=20, humidity=80, daylight=16, wind=1.5, tide=4)
    aco = AntColonyOptimization(num_ants=1000, num_iterations=500, decay=0.8, alpha=1.2, beta=2.5, env=env, quantum_states=quantum_states)
    best_solutions, best_costs, epsilon_values, q_values, k_values = aco.run()
