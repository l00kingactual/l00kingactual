import numpy as np

class GeneticAlgorithm:
    def __init__(self, problem_size, population_size, num_generations, mutation_rate):
        self.problem_size = problem_size
        self.population_size = population_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.population = self._initialize_population()

    def _initialize_population(self):
        return np.random.permutation([np.random.permutation(self.problem_size) for _ in range(self.population_size)])

    def _fitness(self, individual):
        return -np.sum((individual - 0.5)**2)

    def _select_parents(self):
        fitness_scores = np.array([self._fitness(ind) for ind in self.population])
        probabilities = fitness_scores / fitness_scores.sum()
        parents_indices = np.random.choice(range(self.population_size), size=self.population_size, p=probabilities)
        return self.population[parents_indices]

    def _crossover(self, parent1, parent2):
        crossover_point = np.random.randint(1, self.problem_size - 1)
        child1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
        child2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
        return child1, child2

    def _mutate(self, individual):
        for i in range(self.problem_size):
            if np.random.rand() < self.mutation_rate:
                j = np.random.randint(0, self.problem_size)
                individual[i], individual[j] = individual[j], individual[i]
        return individual

    def _create_next_generation(self, parents):
        next_generation = []
        for i in range(0, self.population_size, 2):
            parent1, parent2 = parents[i], parents[i + 1]
            child1, child2 = self._crossover(parent1, parent2)
            next_generation.append(self._mutate(child1))
            next_generation.append(self._mutate(child2))
        return np.array(next_generation)

    def run(self):
        for generation in range(self.num_generations):
            parents = self._select_parents()
            self.population = self._create_next_generation(parents)
            best_individual = max(self.population, key=self._fitness)
            best_fitness = self._fitness(best_individual)
            print(f"Generation {generation + 1}: Best fitness = {best_fitness}")
        best_individual = max(self.population, key=self._fitness)
        best_fitness = self._fitness(best_individual)
        return best_individual, best_fitness

# Example usage
if __name__ == "__main__":
    ga = GeneticAlgorithm(problem_size=10, population_size=100, num_generations=100, mutation_rate=0.01)
    best_solution, best_fitness = ga.run()
    print(f"Genetic Algorithm: Best solution = {best_solution}, Best fitness = {best_fitness}")
