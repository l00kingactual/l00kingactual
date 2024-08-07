import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from deap import base, creator, tools, algorithms

# Function to perform the genetic algorithm optimization
def genetic_algorithm(f, n_gen, pop_size):
    # Create necessary DEAP classes
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
    
    # List to store the evolution of the population
    pop_evolution = []
    
    # Evolve the population
    for gen in range(n_gen):
        # Evaluate the entire population
        fitnesses = list(map(toolbox.evaluate, pop))
        for ind, fit in zip(pop, fitnesses):
            ind.fitness.values = fit
        
        # Record the current population
        pop_evolution.append([(gen, ind[0], ind.fitness.values[0]) for ind in pop])
        
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
    
    # Return the final population and its evolution
    return pop, pop_evolution

# Example usage
f = lambda x: x**2 + 2*x + 1
n_gen = 50
pop_size = 100
final_pop, pop_evolution = genetic_algorithm(f, n_gen=n_gen, pop_size=pop_size)

# Prepare data for 3D animation
gen_data = np.array([item for sublist in pop_evolution for item in sublist])
gens, xs, ys = gen_data[:, 0], gen_data[:, 1], gen_data[:, 2]

# Create 3D animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(xs, ys, gens, c=ys, cmap='viridis', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Fitness')
ax.set_zlabel('Generation')
ax.set_title('Genetic Algorithm Optimization')

# Update function for animation
def update(num, gens, xs, ys, scatter):
    current_gen = gens <= num
    scatter._offsets3d = (xs[current_gen], ys[current_gen], gens[current_gen])
    scatter.set_array(ys[current_gen])
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, n_gen, 1), fargs=(gens, xs, ys, scatter), interval=200, blit=False)

# Add color bar outside the animation
cbar = plt.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Fitness')

plt.show()
