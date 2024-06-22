import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def complex_fitness_function(x):
    """A more complex fitness function to provide a challenging optimization problem."""
    return np.sum(np.sin(5 * np.pi * x) ** 6 + x ** 2)

# Constants
population_size = 100
num_generations = 100
num_dimensions = 10

# Genetic Algorithm
class GeneticAlgorithm:
    def __init__(self):
        self.population = np.random.rand(population_size, num_dimensions)
        self.fitness = np.zeros(population_size)

    def evaluate(self):
        self.fitness = np.array([complex_fitness_function(ind) for ind in self.population])

    def select(self):
        indices = np.argsort(self.fitness)[-population_size//2:]
        return self.population[indices]

    def crossover(self, parent1, parent2):
        point = np.random.randint(1, num_dimensions - 1)
        child1 = np.concatenate([parent1[:point], parent2[point:]])
        child2 = np.concatenate([parent2[:point], parent1[point:]])
        return child1, child2

    def mutate(self, individual):
        point = np.random.randint(num_dimensions)
        individual[point] = np.random.rand()
        return individual

    def run(self):
        best_fitness = []
        best_individuals = []
        for generation in range(num_generations):
            self.evaluate()
            best_fitness.append(np.max(self.fitness))
            best_individuals.append(self.population[np.argmax(self.fitness)])
            parents = self.select()
            new_population = []
            for i in range(0, len(parents), 2):
                parent1, parent2 = parents[i], parents[i + 1]
                child1, child2 = self.crossover(parent1, parent2)
                new_population.append(self.mutate(child1))
                new_population.append(self.mutate(child2))
            self.population = np.array(new_population)
            print(f"Generation {generation+1}/{num_generations} - Best Fitness: {best_fitness[-1]}")
        return best_fitness, best_individuals

# Tabu Search
import numpy as np

# Tabu Search
class TabuSearch:
    def __init__(self):
        self.solution = np.random.rand(num_dimensions)
        self.fitness = complex_fitness_function(self.solution)
        self.tabu_list = []
        self.tabu_list_size = 5

    def run(self):
        best_fitness = []
        for iteration in range(num_generations):
            neighbors = [self.solution + np.random.normal(0, 0.1, num_dimensions) for _ in range(20)]
            neighbors_fitness = [complex_fitness_function(neighbor) for neighbor in neighbors]
            best_neighbor = neighbors[np.argmax(neighbors_fitness)]
            if not any(np.array_equal(best_neighbor, t) for t in self.tabu_list):
                self.solution = best_neighbor
                self.fitness = np.max(neighbors_fitness)
                self.tabu_list.append(best_neighbor)
                if len(self.tabu_list) > self.tabu_list_size:
                    self.tabu_list.pop(0)
            best_fitness.append(self.fitness)
            print(f"Tabu Iteration {iteration+1}/{num_generations} - Best Fitness: {self.fitness}")
        return best_fitness, self.solution


# Hill-Climbing
class HillClimbing:
    def __init__(self):
        self.solution = np.random.rand(num_dimensions)
        self.fitness = complex_fitness_function(self.solution)

    def run(self):
        best_fitness = []
        for iteration in range(num_generations):
            neighbors = [self.solution + np.random.normal(0, 0.1, num_dimensions) for _ in range(20)]
            neighbors_fitness = [complex_fitness_function(neighbor) for neighbor in neighbors]
            best_neighbor = neighbors[np.argmax(neighbors_fitness)]
            if np.max(neighbors_fitness) > self.fitness:
                self.solution = best_neighbor
                self.fitness = np.max(neighbors_fitness)
            best_fitness.append(self.fitness)
            print(f"Hill-Climbing Iteration {iteration+1}/{num_generations} - Best Fitness: {self.fitness}")
        return best_fitness, self.solution

# Simulated Annealing
class SimulatedAnnealing:
    def __init__(self):
        self.solution = np.random.rand(num_dimensions)
        self.fitness = complex_fitness_function(self.solution)
        self.temperature = 1.0
        self.cooling_rate = 0.99

    def run(self):
        best_fitness = []
        for iteration in range(num_generations):
            neighbor = self.solution + np.random.normal(0, 0.1, num_dimensions)
            neighbor_fitness = complex_fitness_function(neighbor)
            if neighbor_fitness > self.fitness or np.random.rand() < np.exp((neighbor_fitness - self.fitness) / self.temperature):
                self.solution = neighbor
                self.fitness = neighbor_fitness
            self.temperature *= self.cooling_rate
            best_fitness.append(self.fitness)
            print(f"Simulated Annealing Iteration {iteration+1}/{num_generations} - Best Fitness: {self.fitness}")
        return best_fitness, self.solution

def combined_optimization():
    ga = GeneticAlgorithm()
    ga_best_fitness, ga_best_individuals = ga.run()

    tabu_search = TabuSearch()
    tabu_best_fitness, _ = tabu_search.run()

    hill_climbing = HillClimbing()
    hc_best_fitness, _ = hill_climbing.run()

    simulated_annealing = SimulatedAnnealing()
    sa_best_fitness, _ = simulated_annealing.run()

    return ga_best_fitness, ga_best_individuals, tabu_best_fitness, hc_best_fitness, sa_best_fitness

ga_best_fitness, ga_best_individuals, tabu_best_fitness, hc_best_fitness, sa_best_fitness = combined_optimization()

# Plotting
fig = plt.figure(figsize=(18, 8))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122, projection='3d')

ax1.plot(range(num_generations), ga_best_fitness, label='GA')
ax1.plot(range(num_generations), tabu_best_fitness, label='Tabu')
ax1.plot(range(num_generations), hc_best_fitness, label='Hill-Climbing')
ax1.plot(range(num_generations), sa_best_fitness, label='Simulated Annealing')
ax1.set_xlabel('Generations')
ax1.set_ylabel('Best Fitness')
ax1.legend()
ax1.set_title('Combined Optimization Best Fitness Over Generations')

X = np.arange(population_size)
Y = np.arange(num_dimensions)
X, Y = np.meshgrid(X, Y)
Z = np.array(ga_best_individuals).T
ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.set_xlabel('Individuals')
ax2.set_ylabel('Dimension')
ax2.set_zlabel('Gene Value')
ax2.set_title('Best Individuals Over Generations')

plt.show()
