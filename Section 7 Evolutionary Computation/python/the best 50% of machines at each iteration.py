import random
import numpy as np
import matplotlib.pyplot as plt
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FSM:
    def __init__(self, num_states):
        self.num_states = num_states
        self.transitions = np.random.randint(0, num_states, size=(num_states, 2))

    def predict(self, inputs):
        state = 0
        for inp in inputs:
            state = self.transitions[state, inp]
        return state

def generate_sequence(length=50):
    return np.random.randint(0, 2, length)

def evaluate_fsm(fsm, sequence):
    correct_predictions = 0
    for i in range(len(sequence) - 1):
        prediction = fsm.predict(sequence[:i+1])
        if prediction == sequence[i+1]:
            correct_predictions += 1
    return correct_predictions / (len(sequence) - 1)

def crossover(fsm1, fsm2):
    child = FSM(fsm1.num_states)
    for i in range(fsm1.num_states):
        if random.random() < 0.5:
            child.transitions[i] = fsm1.transitions[i]
        else:
            child.transitions[i] = fsm2.transitions[i]
    return child

def mutate(fsm, mutation_rate=0.1):
    for i in range(fsm.num_states):
        if random.random() < mutation_rate:
            fsm.transitions[i] = np.random.randint(0, fsm.num_states, 2)

def evolve_population(population, sequence, retain_rate=0.5, mutation_rate=0.1, generations=100):
    fitness_history = []

    for generation in range(generations):
        fitness_scores = [(evaluate_fsm(fsm, sequence), fsm) for fsm in population]
        fitness_scores.sort(key=lambda x: x[0], reverse=True)
        
        retain_length = int(len(fitness_scores) * retain_rate)
        next_generation = [fsm for _, fsm in fitness_scores[:retain_length]]

        while len(next_generation) < len(population):
            parent1, parent2 = random.sample(next_generation, 2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            next_generation.append(child)

        population = next_generation
        best_fitness = fitness_scores[0][0]
        fitness_history.append(best_fitness)
        logging.info(f"Generation {generation+1}: Best fitness = {best_fitness}")

    return population, fitness_history

# Example usage
if __name__ == "__main__":
    num_states = 5
    population_size = 50
    sequence = generate_sequence(length=100)
    population = [FSM(num_states) for _ in range(population_size)]
    generations = 100

    population, fitness_history = evolve_population(population, sequence, generations=generations)
    best_fsm = population[0]
    best_fitness = evaluate_fsm(best_fsm, sequence)
    print(f"Best FSM transitions: {best_fsm.transitions}, Fitness: {best_fitness}")

    # Plotting the fitness over generations
    plt.plot(range(generations), fitness_history, label='Best Fitness')
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.title('Evolution of FSM Fitness Over Generations')
    plt.legend()
    plt.show()
