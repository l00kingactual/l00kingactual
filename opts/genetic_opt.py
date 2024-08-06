import random
from deap import base, creator, tools, algorithms
from neural_network import build_enhanced_nn
import numpy as np

from k_value_space import k_value_space
from q_value_space import q_value_space
from epsilon_value_space import epsilon_value_space

def genetic_algorithm_optimization(input_shape, num_classes, x_train, y_train, build_fn, logger, ngen=12):
    def evaluate(individual):
        num_layers, units_0, dropout_0, units_1, dropout_1, learning_rate, k, q, epsilon = individual
        model = build_fn(
            input_shape=(input_shape,),
            num_classes=num_classes,
            num_layers=int(num_layers),
            units_0=int(units_0),
            dropout_0=dropout_0,
            units_1=int(units_1),
            dropout_1=dropout_1,
            learning_rate=learning_rate,
            k=k,
            q=q,
            epsilon=epsilon
        )
        history = model.fit(x_train, y_train, epochs=10, validation_split=0.2, verbose=0)
        accuracy = history.history['val_accuracy'][-1]
        return accuracy,

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_int", random.randint, 6, 10)
    toolbox.register("attr_units", random.randint, 16, 1024)
    toolbox.register("attr_float", random.uniform, 0.0, 0.75)
    toolbox.register("attr_units_1", random.randint, 32, 512)
    toolbox.register("attr_dropout_1", random.uniform, 0.0, 0.25)
    toolbox.register("attr_lr", random.uniform, 1e-6, 1e-1)
    toolbox.register("attr_k", random.choice, k_value_space)
    toolbox.register("attr_q", random.choice, q_value_space)
    toolbox.register("attr_epsilon", random.choice, epsilon_value_space)

    toolbox.register("individual", tools.initCycle, creator.Individual,
                     (toolbox.attr_int, toolbox.attr_units, toolbox.attr_float,
                      toolbox.attr_units_1, toolbox.attr_dropout_1, toolbox.attr_lr,
                      toolbox.attr_k, toolbox.attr_q, toolbox.attr_epsilon), n=1)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", evaluate)

    population = toolbox.population(n=10)
    cxpb = 0.5
    mutpb = 0.2

    # Logging statistics
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    
    logbook = tools.Logbook()
    logbook.header = ["gen", "nevals"] + stats.fields

    try:
        logger.debug("Starting Genetic Algorithm Optimization")
        print("Starting Genetic Algorithm Optimization...")
        for gen in range(ngen):
            population, log = algorithms.eaSimple(population, toolbox, cxpb, mutpb, 1, stats=stats, verbose=False)
            record = stats.compile(population)
            logbook.record(gen=gen, nevals=len(population), **record)
            logger.debug(f"Generation {gen}")
            logger.debug(logbook.stream)
            print(f"Generation {gen}")
            print(logbook.stream)
            
        top_individuals = tools.selBest(population, k=1)
        logger.debug(f"Genetic Algorithm Optimization Completed: {top_individuals}")
        print(f"Genetic Algorithm Optimization Completed: {top_individuals}")
        return top_individuals[0]
    except Exception as e:
        logger.error(f"Error during Genetic Algorithm Optimization: {str(e)}", exc_info=True)
        print(f"Error during Genetic Algorithm Optimization: {str(e)}")
        raise
