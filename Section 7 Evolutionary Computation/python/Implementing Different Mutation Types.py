import random
import matplotlib.pyplot as plt

class FSM:
    def __init__(self, num_states, num_symbols):
        self.num_states = num_states
        self.num_symbols = num_symbols
        self.transitions = [[random.randint(0, num_states - 1) for _ in range(num_symbols)] for _ in range(num_states)]
        self.state = 0

    def reset(self):
        self.state = 0

    def step(self, input_symbol):
        if 0 <= input_symbol < self.num_symbols:
            self.state = self.transitions[self.state][input_symbol]
        return self.state

    def predict(self, input_symbol):
        if 0 <= input_symbol < self.num_symbols:
            return self.transitions[self.state][input_symbol]
        return None

def fitness(fsm, sequence):
    fsm.reset()
    correct_predictions = 0
    for i in range(len(sequence) - 1):
        predicted_symbol = fsm.predict(sequence[i])
        if predicted_symbol == sequence[i + 1]:
            correct_predictions += 1
        fsm.step(sequence[i])
    return correct_predictions / (len(sequence) - 1)

def crossover(fsm1, fsm2):
    child = FSM(fsm1.num_states, fsm1.num_symbols)
    for i in range(fsm1.num_states):
        if random.random() < 0.5:
            child.transitions[i] = fsm1.transitions[i]
        else:
            child.transitions[i] = fsm2.transitions[i]
    return child

def mutate(fsm, mutation_rate=0.1):
    for i in range(fsm.num_states):
        if random.random() < mutation_rate:
            fsm.transitions[i] = [random.randint(0, fsm.num_states - 1) for _ in range(fsm.num_symbols)]

def evolve(num_states, num_symbols, population_size, generations, sequence):
    population = [FSM(num_states, num_symbols) for _ in range(population_size)]
    best_fitness = []

    for gen in range(generations):
        population_fitness = [fitness(fsm, sequence) for fsm in population]
        best_fitness.append(max(population_fitness))

        next_generation = []
        for _ in range(population_size // 2):
            parents = random.choices(population, weights=population_fitness, k=2)
            child1 = crossover(parents[0], parents[1])
            child2 = crossover(parents[0], parents[1])
            mutate(child1)
            mutate(child2)
            next_generation.extend([child1, child2])

        population = next_generation

    best_fsm = max(population, key=lambda fsm: fitness(fsm, sequence))
    return best_fsm, best_fitness

# Parameters
num_states = 5
num_symbols = 3
population_size = 50
generations = 100
sequence = [random.randint(0, num_symbols - 1) for _ in range(100)]  # More complex random sequence

# Evolution process
best_fsm, best_fitness = evolve(num_states, num_symbols, population_size, generations, sequence)
print(f"Best FSM transitions: {best_fsm.transitions}, Fitness: {fitness(best_fsm, sequence)}")

# Plotting fitness over generations
plt.plot(best_fitness, label='Best Fitness')
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.title('Evolution of FSM Fitness Over Generations')
plt.legend()
plt.show()
