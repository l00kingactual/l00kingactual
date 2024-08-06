import numpy as np
import random
import matplotlib.pyplot as plt

# Define the individual class for the evolutionary algorithm

class Individual:
    def __init__(self, chromosome_length):
        self.chromosome = np.random.rand(chromosome_length)
        self.fitness = None

    def evaluate_fitness(self, fitness_function):
        self.fitness = fitness_function(self.chromosome)

# Define the Genetic Algorithm class

class GeneticAlgorithm:
    def __init__(self, population_size, chromosome_length, fitness_function, mutation_rate=0.01, crossover_rate=0.7):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.fitness_function = fitness_function
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = [Individual(chromosome_length) for _ in range(population_size)]
        self.history = []

    def evaluate_population(self):
        for individual in self.population:
            individual.evaluate_fitness(self.fitness_function)

    def select_parents(self):
        total_fitness = sum(individual.fitness for individual in self.population)
        selection_probs = [individual.fitness / total_fitness for individual in self.population]
        parents = np.random.choice(self.population, size=self.population_size, p=selection_probs)
        return parents

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, self.chromosome_length - 1)
            child1_chromosome = np.concatenate((parent1.chromosome[:crossover_point], parent2.chromosome[crossover_point:]))
            child2_chromosome = np.concatenate((parent2.chromosome[:crossover_point], parent1.chromosome[crossover_point:]))
            return Individual(self.chromosome_length), Individual(self.chromosome_length)
        else:
            return parent1, parent2

    def mutate(self, individual):
        for i in range(self.chromosome_length):
            if random.random() < self.mutation_rate:
                individual.chromosome[i] += np.random.randn() * 0.1
                individual.chromosome[i] = np.clip(individual.chromosome[i], 0, 1)

    def create_next_generation(self, parents):
        next_generation = []
        for i in range(0, self.population_size, 2):
            parent1, parent2 = parents[i], parents[i+1]
            child1, child2 = self.crossover(parent1, parent2)
            self.mutate(child1)
            self.mutate(child2)
            next_generation.append(child1)
            next_generation.append(child2)
        return next_generation

    def run(self, generations):
        self.evaluate_population()
        for generation in range(generations):
            parents = self.select_parents()
            self.population = self.create_next_generation(parents)
            self.evaluate_population()
            avg_fitness = np.mean([individual.fitness for individual in self.population])
            self.history.append(avg_fitness)
            print(f'Generation {generation + 1}: Average Fitness = {avg_fitness}')

    def plot_fitness(self):
        plt.plot(self.history)
        plt.title('Average Fitness Over Generations')
        plt.xlabel('Generation')
        plt.ylabel('Average Fitness')
        plt.show()

# Example Usage

def fitness_function(chromosome):
    return -np.sum((chromosome - 0.5) ** 2)

if __name__ == "__main__":
    ga = GeneticAlgorithm(population_size=100, chromosome_length=10, fitness_function=fitness_function, mutation_rate=0.01, crossover_rate=0.7)
    ga.run(generations=50)
    ga.plot_fitness()
