import numpy as np
import logging
import matplotlib.pyplot as plt
import seaborn as sns
from deap import base, creator, tools, algorithms

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define the problem
def evaluate(individual):
    f1 = np.sum(np.square(individual))
    f2 = np.sum(np.abs(individual))
    return f1, f2

# Constraint function
def constraint(individual):
    return np.sum(individual) - 10  # Example constraint: sum of variables should be <= 10

# Penalty function
def penalty(individual):
    constraint_violation = max(0, constraint(individual))  # Constraint violation if positive
    penalty_factor = 1000  # Penalty factor
    return penalty_factor * constraint_violation

# Define constants
POP_SIZE = 100
NGEN = 200
DIMENSIONS = 2
BOUNDS = [-10, 10]

# Setup DEAP
creator.create("FitnessMulti", base.Fitness, weights=(-1.0, -1.0))  # Minimization problem
creator.create("Individual", list, fitness=creator.FitnessMulti)

toolbox = base.Toolbox()
toolbox.register("attr_float", np.random.uniform, BOUNDS[0], BOUNDS[1])
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, DIMENSIONS)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=BOUNDS[0], up=BOUNDS[1], eta=20.0)
toolbox.register("mutate", tools.mutPolynomialBounded, low=BOUNDS[0], up=BOUNDS[1], eta=20.0, indpb=1.0/DIMENSIONS)
toolbox.register("select", tools.selNSGA2)
toolbox.register("evaluate", evaluate)

# Initialize population
try:
    population = toolbox.population(n=POP_SIZE)
    logger.info("Initial population generated with shape: %s", np.shape(population))
except Exception as e:
    logger.error("Error initializing population: %s", e)
    raise

# Log initial population data
for i, individual in enumerate(population):
    logger.info("Initial individual %d: %s", i, individual)

# Run the algorithm and log fitness values
fitness_data = []

for gen in range(NGEN):
    try:
        # Evaluate the population
        fitnesses = list(map(toolbox.evaluate, population))
        for ind, fit in zip(population, fitnesses):
            penalty_value = penalty(ind)
            ind.fitness.values = (fit[0] + penalty_value, fit[1] + penalty_value)
        
        # Verify fitness values
        for i, ind in enumerate(population):
            if not hasattr(ind.fitness, 'values') or len(ind.fitness.values) != 2:
                logger.error("Invalid fitness values for individual %d in generation %d: %s", i, gen, ind.fitness.values)
        
        # Log fitness values
        fitness_data.append([ind.fitness.values for ind in population])
        logger.info("Generation %d, fitness values: %s", gen, fitness_data[-1])

        # Apply selection
        population = toolbox.select(population, len(population))
        
        # Apply crossover and mutation
        offspring = list(map(toolbox.clone, population))
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if np.random.rand() < 0.9:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
        for mutant in offspring:
            if np.random.rand() < 0.1:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Update population with offspring
        population[:] = offspring
        
        # Log population data
        for i, individual in enumerate(population):
            logger.info("Generation %d, individual %d: %s", gen, i, individual)
    
    except Exception as e:
        logger.error("Error in generation %d: %s", gen, e)
        raise

# Extract the Pareto front and log it
try:
    pareto_front = tools.sortNondominated(population, len(population), first_front_only=True)[0]
    valid_pareto_front = [ind for ind in pareto_front if hasattr(ind.fitness, 'values') and len(ind.fitness.values) == 2]
    logger.info("Pareto front extracted with %d solutions", len(valid_pareto_front))
    
    # Verify fitness values in Pareto front
    for i, ind in enumerate(valid_pareto_front):
        if not hasattr(ind.fitness, 'values') or len(ind.fitness.values) != 2:
            logger.error("Invalid fitness values for Pareto front individual %d: %s", i, ind.fitness.values)
    
    # Collect valid Pareto front fitness values
    pareto_f1 = [ind.fitness.values[0] for ind in valid_pareto_front]
    pareto_f2 = [ind.fitness.values[1] for ind in valid_pareto_front]

    logger.info("Pareto front solutions: %s", valid_pareto_front)
    logger.info("Pareto front f1 values: %s", pareto_f1)
    logger.info("Pareto front f2 values: %s", pareto_f2)
except Exception as e:
    logger.error("Error extracting Pareto front: %s", e)
    raise

# Prepare data for plotting
pareto_data = np.array([[ind.fitness.values[0], ind.fitness.values[1]] for ind in valid_pareto_front if len(ind.fitness.values) == 2])
logger.info("Pareto data shape: %s", pareto_data.shape)
logger.info("Pareto data: %s", pareto_data)

# Plotting function
def plot_evolution(fitness_data):
    sns.set(style="whitegrid")
    palette = sns.color_palette("viridis", NGEN)
    
    plt.figure(figsize=(10, 6))
    for gen, fitness_gen in enumerate(fitness_data):
        f1 = [fit[0] for fit in fitness_gen if len(fit) == 2]
        f2 = [fit[1] for fit in fitness_gen if len(fit) == 2]
        plt.scatter(f1, f2, color=palette[gen], label=f'Generation {gen}' if gen % 10 == 0 else "", alpha=0.5, edgecolors='w', s=30)
    
    plt.xlabel('Objective 1')
    plt.ylabel('Objective 2')
    plt.title('Evolution of Population Over Generations')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Call the plotting function
plot_evolution(fitness_data)

# Ensure to close all DEAP loggers
for handler in logger.handlers:
    handler.close()
    logger.removeHandler(handler)
