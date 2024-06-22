import random
import matplotlib.pyplot as plt

class FSM:
    def __init__(self, num_states):
        self.num_states = num_states
        self.transitions = [[random.randint(0, num_states - 1) for _ in range(2)] for _ in range(num_states)]
        self.state = 0

    def reset(self):
        self.state = 0

    def step(self, input):
        self.state = self.transitions[self.state][input]
        return self.state

def fitness(fsm):
    sequence = "1010"
    fsm.reset()
    state_sequence = []
    for char in sequence:
        state_sequence.append(fsm.step(int(char)))
    target_sequence = [0, 1, 2, 3]
    matches = sum(1 for actual, target in zip(state_sequence, target_sequence) if actual == target)
    return matches / len(target_sequence)

def crossover(fsm1, fsm2):
    child = FSM(fsm1.num_states)
    for i in range(fsm1.num_states):
        if random.random() < 0.5:
            child.transitions[i] = fsm1.transitions[i]
        else:
            child.transitions[i] = fsm2.transitions[i]
    return child

def mutate(fsm, mutation_rate=0.3):  # Increased mutation rate
    for i in range(fsm.num_states):
        if random.random() < mutation_rate:
            fsm.transitions[i] = [random.randint(0, fsm.num_states - 1) for _ in range(2)]

def evolve(num_states, population_size, generations):
    population = [FSM(num_states) for _ in range(population_size)]
    best_fitness = []

    for gen in range(generations):
        population_fitness = [fitness(fsm) for fsm in population]
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

    best_fsm = max(population, key=fitness)
    return best_fsm, best_fitness

# Parameters
num_states = 4
population_size = 50
generations = 100

# Evolution process
best_fsm, best_fitness = evolve(num_states, population_size, generations)
print(f"Best FSM transitions: {best_fsm.transitions}, Fitness: {fitness(best_fsm)}")

# Plotting fitness over generations
plt.plot(best_fitness, label='Best Fitness')
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.title('Evolution of FSM Fitness Over Generations')
plt.legend()
plt.show()
