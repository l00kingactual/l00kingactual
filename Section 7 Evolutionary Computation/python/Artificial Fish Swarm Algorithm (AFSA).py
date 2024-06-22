import numpy as np
import pygame
import sys

# Define the complex function to be minimized
def complex_function(x, y):
    return np.sin(np.sqrt(x**2 + y**2)) + 0.1 * (x**2 + y**2)

# AFSA Parameters
POP_SIZE = 30
DIM = 2
MAX_ITER = 100
VISUAL = 0.1
STEP = 0.1
TRY_NUMBER = 5
WIDTH, HEIGHT = 800, 800
SCALE = 80
OFFSET = WIDTH // 2

# Initialize the fish population
np.random.seed(42)
population = np.random.rand(POP_SIZE, DIM) * 10 - 5  # Range [-5, 5]

# Evaluate the fitness of each fish
def evaluate(pop):
    return np.array([complex_function(ind[0], ind[1]) for ind in pop])

# Define the behaviors
def prey(fish, population):
    best_fish = fish
    best_fitness = complex_function(fish[0], fish[1])
    for _ in range(TRY_NUMBER):
        candidate = fish + np.random.uniform(-1, 1, DIM) * VISUAL
        candidate_fitness = complex_function(candidate[0], candidate[1])
        if candidate_fitness < best_fitness:
            best_fish = candidate
            best_fitness = candidate_fitness
    return best_fish

def swarm(fish, population):
    center = np.mean(population, axis=0)
    center_fitness = complex_function(center[0], center[1])
    if center_fitness < complex_function(fish[0], fish[1]):
        return fish + STEP * (center - fish) / np.linalg.norm(center - fish)
    return fish

def follow(fish, population):
    best_fish = fish
    best_fitness = complex_function(fish[0], fish[1])
    for other_fish in population:
        if np.linalg.norm(fish - other_fish) < VISUAL:
            other_fitness = complex_function(other_fish[0], other_fish[1])
            if other_fitness < best_fitness:
                best_fish = other_fish
                best_fitness = other_fitness
    if best_fish is not fish:
        return fish + STEP * (best_fish - fish) / np.linalg.norm(best_fish - fish)
    return fish

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Artificial Fish Swarm Algorithm Visualization")

# Colors
BACKGROUND_COLOR = (0, 0, 0)
FISH_COLOR = (0, 255, 255)
TEXT_COLOR = (255, 255, 255)
GEN_COLORS = [(int(255 * i / MAX_ITER), 0, 255 - int(255 * i / MAX_ITER)) for i in range(MAX_ITER)]

# Draw Function Landscape
def draw_landscape():
    for x in range(WIDTH):
        for y in range(HEIGHT):
            fx = (x - OFFSET) / SCALE
            fy = (y - OFFSET) / SCALE
            fz = complex_function(fx, fy)
            color = (0, int(255 * fz / 10), int(255 * fz / 10))
            screen.set_at((x, y), color)

# AFSA Algorithm
best_solution = None
best_fitness = float('inf')

for iteration in range(MAX_ITER):
    screen.fill(BACKGROUND_COLOR)
    draw_landscape()
    new_population = np.zeros_like(population)
    for i in range(POP_SIZE):
        fish = population[i]
        if np.random.rand() < 0.3:
            new_population[i] = prey(fish, population)
        elif np.random.rand() < 0.6:
            new_population[i] = swarm(fish, population)
        else:
            new_population[i] = follow(fish, population)
    population = new_population
    current_fitness = evaluate(population)
    min_fitness_idx = np.argmin(current_fitness)
    if current_fitness[min_fitness_idx] < best_fitness:
        best_fitness = current_fitness[min_fitness_idx]
        best_solution = population[min_fitness_idx]
    
    for fish in population:
        fx = int(fish[0] * SCALE + OFFSET)
        fy = int(fish[1] * SCALE + OFFSET)
        pygame.draw.circle(screen, GEN_COLORS[iteration], (fx, fy), 5)
    
    pygame.display.flip()
    pygame.time.delay(100)

    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

print(f"Best solution: {best_solution}")
print(f"Best fitness: {best_fitness}")
pygame.quit()
