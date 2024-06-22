import random
import logging
import numpy as np
import json
from datetime import datetime, timezone
import matplotlib.pyplot as plt

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Constants
ROWS, COLS = 10, 10  # Maze dimensions
POPULATION_SIZE = 50  # Number of paths in the population
GENERATIONS = 100  # Number of generations for the GA to run
INITIAL_MUTATION_RATE = 0.1  # Initial probability of mutation occurring in a path
PHEROMONE_DECAY = 0.9
PHEROMONE_BOOST = 100
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# Maze and Genetic Algorithm configurations
maze = np.zeros((ROWS, COLS))  # A 10x10 maze for simplicity
start = (0, 0)
end = (9, 9)
pheromone = np.ones((ROWS, COLS))

def log_to_json(level, message, **kwargs):
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "message": message,
        "extra": kwargs
    }
    logger.log(level, json.dumps(log_entry))

class Path:
    def __init__(self, moves=None):
        self.moves = moves or self.generate_random_moves()
        self.fitness = 0

    def generate_random_moves(self):
        moves = []
        x, y = start
        for _ in range(ROWS * COLS):
            move = random.choice(DIRECTIONS)
            new_x, new_y = x + move[0], y + move[1]
            if 0 <= new_x < ROWS and 0 <= new_y < COLS:
                moves.append(move)
                x, y = new_x, new_y
        return moves

    def calculate_fitness(self):
        x, y = start
        steps_taken = 0
        for move in self.moves:
            x, y = x + move[0], y + move[1]
            steps_taken += 1
            if not (0 <= x < ROWS and 0 <= y < COLS) or maze[x][y] == 1:
                self.fitness = -float('inf')
                return
            if (x, y) == end:
                self.fitness = 1 / steps_taken
                self.update_pheromones()
                return
        self.fitness = -((abs(x - end[0]) + abs(y - end[1])))

    def update_pheromones(self):
        x, y = start
        for move in self.moves:
            x, y = x + move[0], y + move[1]
            if not (0 <= x < ROWS and 0 <= y < COLS) or maze[x][y] == 1:
                return
            pheromone[x][y] += PHEROMONE_BOOST

    @staticmethod
    def crossover(path1, path2):
        split = random.randint(0, min(len(path1.moves), len(path2.moves)) - 1)
        new_moves = path1.moves[:split] + path2.moves[split:]
        return Path(new_moves)

    def mutate(self, mutation_rate):
        if random.random() < mutation_rate:
            idx = random.randint(0, len(self.moves) - 1)
            self.moves[idx] = random.choice(DIRECTIONS)

def decay_pheromones():
    for i in range(ROWS):
        for j in range(COLS):
            pheromone[i][j] *= PHEROMONE_DECAY

def genetic_algorithm():
    population = [Path() for _ in range(POPULATION_SIZE)]
    mutation_rate = INITIAL_MUTATION_RATE
    for generation in range(GENERATIONS):
        log_to_json(logging.INFO, "Generation", generation=generation)
        for path in population:
            path.calculate_fitness()
        population.sort(key=lambda p: p.fitness, reverse=True)
        next_generation = population[:POPULATION_SIZE // 10]

        fitness_values = [path.fitness for path in population]
        if max(fitness_values) - min(fitness_values) < 0.01:
            mutation_rate = min(1.0, mutation_rate * 1.1)
        else:
            mutation_rate = max(0.01, mutation_rate * 0.9)

        while len(next_generation) < POPULATION_SIZE:
            parents = random.sample(population[:POPULATION_SIZE // 2], 2)
            child = Path.crossover(parents[0], parents[1])
            child.mutate(mutation_rate)
            next_generation.append(child)

        population = next_generation
        decay_pheromones()

    best_path = max(population, key=lambda p: p.fitness)
    log_to_json(logging.INFO, "Best Path", moves=best_path.moves, fitness=best_path.fitness)
    return best_path

def visualize_path(path):
    x, y = start
    path_x, path_y = [x], [y]
    for move in path.moves:
        x += move[0]
        y += move[1]
        if 0 <= x < ROWS and 0 <= y < COLS:
            path_x.append(x)
            path_y.append(y)

    plt.figure(figsize=(8, 8))
    plt.imshow(maze, cmap='gray_r')
    plt.plot(path_y, path_x, marker='o', color='blue')
    plt.scatter(start[1], start[0], color='green', s=100, label='Start')
    plt.scatter(end[1], end[0], color='red', s=100, label='End')
    plt.legend()
    plt.title('Path Visualization')
    plt.show()

if __name__ == "__main__":
    best_path = genetic_algorithm()
    visualize_path(best_path)
