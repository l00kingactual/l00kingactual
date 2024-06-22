import random

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
    sequence = "101"
    fsm.reset()
    state_sequence = []
    for char in sequence:
        state_sequence.append(fsm.step(int(char)))
    if state_sequence == [0, 1, 2]:
        return 1.0
    return 0.0

def crossover(fsm1, fsm2):
    child = FSM(fsm1.num_states)
    for i in range(fsm1.num_states):
        if random.random() < 0.5:
            child.transitions[i] = fsm1.transitions[i]
        else:
            child.transitions[i] = fsm2.transitions[i]
    return child

def mutate(fsm):
    mutated_fsm = FSM(fsm.num_states)
    mutated_fsm.transitions = [list(state) for state in fsm.transitions]
    for i in range(fsm.num_states):
        if random.random() < 0.1:
            mutated_fsm.transitions[i][random.randint(0, 1)] = random.randint(0, fsm.num_states - 1)
    return mutated_fsm

def evolve(num_generations, population_size, num_states):
    population = [FSM(num_states) for _ in range(population_size)]
    for generation in range(num_generations):
        population = sorted(population, key=lambda fsm: -fitness(fsm))
        next_generation = population[:2]
        for _ in range(population_size - 2):
            parent1, parent2 = random.sample(population[:10], 2)
            child = mutate(crossover(parent1, parent2))
            next_generation.append(child)
        population = next_generation
    best_fsm = max(population, key=fitness)
    return best_fsm

if __name__ == "__main__":
    num_generations = 100
    population_size = 50
    num_states = 3
    best_fsm = evolve(num_generations, population_size, num_states)
    print(f"Best FSM transitions: {best_fsm.transitions}, Fitness: {fitness(best_fsm)}")
