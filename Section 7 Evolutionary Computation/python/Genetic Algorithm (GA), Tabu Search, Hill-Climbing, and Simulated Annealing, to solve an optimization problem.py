import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Objective Function
def objective_function(x):
    return np.sum(x)

# Genetic Algorithm
class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, generations, dimensions):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.dimensions = dimensions
        self.population = np.random.rand(self.population_size, self.dimensions)
        self.best_individuals = []

    def selection(self):
        fitness = np.apply_along_axis(objective_function, 1, self.population)
        selected_indices = np.argsort(fitness)[-self.population_size//2:]
        return self.population[selected_indices, :]

    def crossover(self, parents):
        offspring = np.empty((self.population_size - parents.shape[0], self.dimensions))
        crossover_point = np.random.randint(1, self.dimensions - 1)
        for k in range(offspring.shape[0]):
            parent1_idx = k % parents.shape[0]
            parent2_idx = (k + 1) % parents.shape[0]
            offspring[k, :crossover_point] = parents[parent1_idx, :crossover_point]
            offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
        return offspring

    def mutate(self, offspring):
        for i in range(offspring.shape[0]):
            if np.random.rand() < self.mutation_rate:
                mutation_point = np.random.randint(self.dimensions)
                offspring[i, mutation_point] = np.random.rand()
        return offspring

    def evolve(self):
        parents = self.selection()
        offspring = self.crossover(parents)
        offspring = self.mutate(offspring)
        self.population[:parents.shape[0], :] = parents
        self.population[parents.shape[0]:, :] = offspring

    def run(self):
        best_fitness = []
        for generation in range(self.generations):
            self.evolve()
            fitness = np.apply_along_axis(objective_function, 1, self.population)
            best_fitness.append(np.max(fitness))
            self.best_individuals.append(self.population[np.argmax(fitness), :])
        return best_fitness, self.best_individuals

# Tabu Search
class TabuSearch:
    def __init__(self, dimensions, iterations, tabu_list_size):
        self.dimensions = dimensions
        self.iterations = iterations
        self.tabu_list_size = tabu_list_size
        self.best_solution = np.random.rand(self.dimensions)
        self.best_fitness = objective_function(self.best_solution)
        self.tabu_list = [self.best_solution.copy()]

    def get_neighbors(self, solution):
        neighbors = []
        for i in range(self.dimensions):
            neighbor = solution.copy()
            neighbor[i] = np.random.rand()
            neighbors.append(neighbor)
        return neighbors

    def run(self):
        best_fitness = []
        for iteration in range(self.iterations):
            neighbors = self.get_neighbors(self.best_solution)
            best_neighbor = max(neighbors, key=objective_function)
            if not any(np.array_equal(best_neighbor, tabu) for tabu in self.tabu_list):
                self.best_solution = best_neighbor
                self.best_fitness = objective_function(best_neighbor)
                self.tabu_list.append(best_neighbor.copy())
                if len(self.tabu_list) > self.tabu_list_size:
                    self.tabu_list.pop(0)
            best_fitness.append(self.best_fitness)
        return best_fitness, self.best_solution

# Hill-Climbing
class HillClimbing:
    def __init__(self, dimensions, iterations):
        self.dimensions = dimensions
        self.iterations = iterations
        self.best_solution = np.random.rand(self.dimensions)
        self.best_fitness = objective_function(self.best_solution)

    def get_neighbor(self, solution):
        neighbor = solution.copy()
        index = np.random.randint(self.dimensions)
        neighbor[index] = np.random.rand()
        return neighbor

    def run(self):
        best_fitness = []
        for iteration in range(self.iterations):
            neighbor = self.get_neighbor(self.best_solution)
            neighbor_fitness = objective_function(neighbor)
            if neighbor_fitness > self.best_fitness:
                self.best_solution = neighbor
                self.best_fitness = neighbor_fitness
            best_fitness.append(self.best_fitness)
        return best_fitness, self.best_solution

# Simulated Annealing
class SimulatedAnnealing:
    def __init__(self, dimensions, iterations, initial_temp, cooling_rate):
        self.dimensions = dimensions
        self.iterations = iterations
        self.temperature = initial_temp
        self.cooling_rate = cooling_rate
        self.current_solution = np.random.rand(self.dimensions)
        self.current_fitness = objective_function(self.current_solution)

    def get_neighbor(self, solution):
        neighbor = solution.copy()
        index = np.random.randint(self.dimensions)
        neighbor[index] = np.random.rand()
        return neighbor

    def run(self):
        best_fitness = []
        for iteration in range(self.iterations):
            neighbor = self.get_neighbor(self.current_solution)
            neighbor_fitness = objective_function(neighbor)
            if neighbor_fitness > self.current_fitness or np.random.rand() < np.exp(
                    (neighbor_fitness - self.current_fitness) / self.temperature):
                self.current_solution = neighbor
                self.current_fitness = neighbor_fitness
            self.temperature *= self.cooling_rate
            best_fitness.append(self.current_fitness)
        return best_fitness, self.current_solution

# Combined Optimization
def combined_optimization():
    dimensions = 10
    generations = 100
    ga = GeneticAlgorithm(population_size=100, mutation_rate=0.01, generations=generations, dimensions=dimensions)
    ga_best_fitness, ga_best_individuals = ga.run()

    tabu_search = TabuSearch(dimensions=dimensions, iterations=generations, tabu_list_size=10)
    tabu_best_fitness, _ = tabu_search.run()

    hill_climbing = HillClimbing(dimensions=dimensions, iterations=generations)
    hc_best_fitness, _ = hill_climbing.run()

    simulated_annealing = SimulatedAnnealing(dimensions=dimensions, iterations=generations, initial_temp=100, cooling_rate=0.95)
    sa_best_fitness, _ = simulated_annealing.run()

    return ga_best_fitness, ga_best_individuals, tabu_best_fitness, hc_best_fitness, sa_best_fitness

# Run optimization and get results
ga_best_fitness, ga_best_individuals, tabu_best_fitness, hc_best_fitness, sa_best_fitness = combined_optimization()

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Best Fitness Over Generations
axs[0].plot(range(100), ga_best_fitness, label='GA')
axs[0].plot(range(100), tabu_best_fitness, label='Tabu')
axs[0].plot(range(100), hc_best_fitness, label='Hill-Climbing')
axs[0].plot(range(100), sa_best_fitness, label='Simulated Annealing')
axs[0].set_title('Combined Optimization Best Fitness Over Generations')
axs[0].set_xlabel('Generations')
axs[0].set_ylabel('Best Fitness')
axs[0].legend()

# 3D plot of Best Individuals
ax = fig.add_subplot(122, projection='3d')
individuals = np.array(ga_best_individuals)
X, Y = np.meshgrid(range(individuals.shape[0]), range(individuals.shape[1]))
Z = individuals.T

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Best Individuals Over Generations')
ax.set_xlabel('Individuals')
ax.set_ylabel('Dimension')
ax.set_zlabel('Gene Value')

plt.tight_layout()
plt.show()
