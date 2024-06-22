import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Evolutionary Algorithm parameters
population_size = 50
generations = 20  # Increased number of generations
mutation_rate = 0.000001  # Increased mutation rate slightly
crossover_rate = 0.0005  # Adjusted crossover rate
elitism_size = 5
sigma_share = 50  # Parameter for fitness sharing
alpha = 1  # Parameter for fitness sharing
k = 50  # Increased value of k for tournament selection

# Initialize population with random hyperparameters
def initialize_population(pop_size):
    population = []
    for _ in range(pop_size):
        individual = {
            'C': np.random.uniform(0.1, 1000),
            'gamma': np.random.uniform(0.0001, 1),
            'kernel': np.random.choice(['linear', 'rbf'])
        }
        population.append(individual)
    return population

# Evaluate fitness of the population using cross-validation
def evaluate_population(population):
    fitness = []
    for individual in population:
        model = SVC(C=individual['C'], gamma=individual['gamma'], kernel=individual['kernel'])
        scores = cross_val_score(model, X, y, cv=5)
        fitness.append(scores.mean())
    return np.array(fitness)

# Tournament selection
def tournament_selection(population, fitness, k=2):
    selected = np.random.choice(range(len(population)), k, replace=False)
    best = selected[np.argmax(fitness[selected])]
    return population[best]

# Crossover (blend crossover for numerical values, uniform crossover for categorical values)
def crossover(parent1, parent2):
    if np.random.rand() < crossover_rate:
        child = {}
        child['C'] = (parent1['C'] + parent2['C']) / 2
        child['gamma'] = (parent1['gamma'] + parent2['gamma']) / 2
        child['kernel'] = parent1['kernel'] if np.random.rand() > 0.5 else parent2['kernel']
        return child
    return parent1

# Mutation
def mutate(individual):
    if np.random.rand() < mutation_rate:
        individual['C'] += np.random.uniform(-1, 1)
        individual['C'] = max(0.1, individual['C'])  # Ensure C is positive
    if np.random.rand() < mutation_rate:
        individual['gamma'] += np.random.uniform(-0.01, 0.01)
        individual['gamma'] = max(0.0001, individual['gamma'])  # Ensure gamma is positive
    if np.random.rand() < mutation_rate:
        individual['kernel'] = np.random.choice(['linear', 'rbf'])
    return individual

# Fitness sharing
def fitness_sharing(fitness, population, sigma_share, alpha):
    shared_fitness = np.copy(fitness)
    for i in range(len(population)):
        sharing_sum = 0
        for j in range(len(population)):
            # Calculate distance only for numerical values
            dist = np.linalg.norm(
                np.array([population[i]['C'], population[i]['gamma']]) - 
                np.array([population[j]['C'], population[j]['gamma']])
            )
            if dist < sigma_share:
                sharing_sum += 1 - (dist / sigma_share) ** alpha
        shared_fitness[i] /= sharing_sum
    return shared_fitness

# Evolutionary Algorithm
population = initialize_population(population_size)
best_scores = []

for gen in range(generations):
    fitness = evaluate_population(population)
    fitness = fitness_sharing(fitness, population, sigma_share, alpha)  # Apply fitness sharing
    best_scores.append(np.max(fitness))
    
    # Elitism
    elite_indices = np.argsort(fitness)[-elitism_size:]
    elite_population = [population[i] for i in elite_indices]
    
    # Create new population
    new_population = list(elite_population)
    while len(new_population) < population_size:
        parent1 = tournament_selection(population, fitness, k)
        parent2 = tournament_selection(population, fitness, k)
        offspring = crossover(parent1, parent2)
        offspring = mutate(offspring)
        new_population.append(offspring)
    
    population = new_population
    print(f'Generation {gen + 1}, Best Score: {best_scores[-1]:.4f}')

# Plot the best scores over generations
plt.figure()
plt.plot(best_scores)
plt.title('Best Score over Generations')
plt.xlabel('Generation')
plt.ylabel('Best Cross-Validation Score')
plt.show()

# Best hyperparameters
best_index = np.argmax(evaluate_population(population))
best_individual = population[best_index]
print(f'Best Hyperparameters: {best_individual}')
