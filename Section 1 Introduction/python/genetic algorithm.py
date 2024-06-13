import random
import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

# Genetic Algorithm function
def genetic_algorithm(f, n_gen, pop_size):
    # Create the necessary DEAP classes
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    
    # Initialize the toolbox
    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.uniform, -10, 10)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=1)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("mate", tools.cxUniform, indpb=0.5)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", lambda x: (f(x[0]),))
    
    # Create the population
    pop = toolbox.population(n=pop_size)
    
    # List to store the fitness evolution
    fitness_evolution = []
    
    # Evolve the population
    for gen in range(n_gen):
        # Evaluate the entire population
        fitnesses = list(map(toolbox.evaluate, pop))
        for ind, fit in zip(pop, fitnesses):
            ind.fitness.values = fit
        
        # Record the best fitness in the current generation
        fits = [ind.fitness.values[0] for ind in pop]
        best_fit = min(fits)
        fitness_evolution.append(best_fit)
        
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))
        
        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < 0.5:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
        
        for mutant in offspring:
            if random.random() < 0.2:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        
        # Replace the population with the offspring
        pop[:] = offspring
    
    # Select the best individual
    best_ind = tools.selBest(pop, k=1)[0]
    return best_ind, fitness_evolution

# Example usage
f = lambda x: x**2 + 2*x + 1
x_opt, fitness_evolution = genetic_algorithm(f, n_gen=50, pop_size=100)
print(f"Optimal solution: {x_opt[0]}")

# Plotting the fitness evolution
plt.figure()
plt.plot(fitness_evolution, label='Best Fitness')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.title('Genetic Algorithm Fitness Evolution')
plt.legend()
plt.grid(True)
plt.show()
