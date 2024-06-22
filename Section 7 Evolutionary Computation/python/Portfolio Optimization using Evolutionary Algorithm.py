import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define parameters for portfolio optimization
num_assets = 5
population_size = 50
generations = 100
mutation_rate = 0.01
crossover_rate = 0.8
elitism_size = 5

# Generate random expected returns and covariance matrix for the assets
np.random.seed(42)
expected_returns = np.random.uniform(0.05, 0.2, num_assets)
cov_matrix = np.random.uniform(0.01, 0.05, (num_assets, num_assets))
cov_matrix = (cov_matrix + cov_matrix.T) / 2  # Make it symmetric
np.fill_diagonal(cov_matrix, np.random.uniform(0.02, 0.1, num_assets))

# Fitness function: Sharpe ratio
def fitness(weights, returns, cov_matrix, risk_free_rate=0.01):
    portfolio_return = np.sum(weights * returns)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
    return sharpe_ratio

# Initialize population with random weights
def initialize_population(pop_size, num_assets):
    population = []
    for _ in range(pop_size):
        weights = np.random.uniform(0, 1, num_assets)
        weights /= np.sum(weights)  # Normalize to sum to 1
        population.append(weights)
    return np.array(population)

# Evaluate fitness of the population
def evaluate_population(population, returns, cov_matrix):
    return np.array([fitness(ind, returns, cov_matrix) for ind in population])

# Tournament selection
def tournament_selection(population, fitness, k=3):
    selected = np.random.choice(range(len(population)), k, replace=False)
    best = selected[np.argmax(fitness[selected])]
    return population[best]

# Crossover (single-point crossover)
def crossover(parent1, parent2):
    if np.random.rand() < crossover_rate:
        point = np.random.randint(1, len(parent1))
        child1 = np.concatenate((parent1[:point], parent2[point:]))
        child2 = np.concatenate((parent2[:point], parent1[point:]))
        return child1, child2
    return parent1, parent2

# Mutation
def mutate(individual):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] += np.random.uniform(-0.1, 0.1)
    individual = np.clip(individual, 0, 1)
    individual /= np.sum(individual)  # Normalize to sum to 1
    return individual

# Evolutionary Algorithm
population = initialize_population(population_size, num_assets)
best_scores = []

fig, ax = plt.subplots()
ax.set_xlim(0, generations)
ax.set_ylim(0, 2)
scat = ax.scatter(range(population_size), evaluate_population(population, expected_returns, cov_matrix), c='blue', marker='o')

def animate(i):
    global population
    fitness_values = evaluate_population(population, expected_returns, cov_matrix)
    best_scores.append(np.max(fitness_values))
    
    # Elitism
    elite_indices = np.argsort(fitness_values)[-elitism_size:]
    elite_population = population[elite_indices]
    
    # Create new population
    new_population = list(elite_population)
    while len(new_population) < population_size:
        parent1 = tournament_selection(population, fitness_values)
        parent2 = tournament_selection(population, fitness_values)
        offspring1, offspring2 = crossover(parent1, parent2)
        new_population.append(mutate(offspring1))
        if len(new_population) < population_size:
            new_population.append(mutate(offspring2))
    
    population = np.array(new_population)
    scat.set_offsets(np.c_[range(population_size), evaluate_population(population, expected_returns, cov_matrix)])
    ax.set_title(f'Generation {i + 1}, Best Sharpe Ratio: {best_scores[-1]:.4f}')

ani = FuncAnimation(fig, animate, frames=generations, interval=200, repeat=False)
plt.show()

# Plot the best scores over generations
plt.figure()
plt.plot(best_scores)
plt.title('Best Sharpe Ratio over Generations')
plt.xlabel('Generation')
plt.ylabel('Best Sharpe Ratio')
plt.show()

# Best portfolio allocation
best_index = np.argmax(evaluate_population(population, expected_returns, cov_matrix))
best_portfolio = population[best_index]
best_sharpe_ratio = evaluate_population(population, expected_returns, cov_matrix)[best_index]
print(f'Best Portfolio Allocation: {best_portfolio}, Best Sharpe Ratio: {best_sharpe_ratio:.4f}')
