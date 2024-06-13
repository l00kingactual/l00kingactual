import pygame
import numpy as np

# Pygame setup
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define parameters
grid_size = 100
num_ants = 50
evaporation_rate = 0.01
deposit_amount = 1
pheromone_grid = np.zeros((grid_size, grid_size))
ants = np.random.randint(0, grid_size, (num_ants, 2))

# Define movement function
def move_ant(ant, pheromone_grid):
    x, y = ant
    moves = [((x-1)%grid_size, y), ((x+1)%grid_size, y), (x, (y-1)%grid_size), (x, (y+1)%grid_size)]
    move_pheromones = [pheromone_grid[m] for m in moves]
    total_pheromone = sum(move_pheromones)
    if total_pheromone == 0:
        return moves[np.random.randint(4)]
    probabilities = [p / total_pheromone for p in move_pheromones]
    return moves[np.random.choice(4, p=probabilities)]

# Simulation loop
running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_pheromone_grid = pheromone_grid * (1 - evaporation_rate)
    for i in range(num_ants):
        ants[i] = move_ant(ants[i], pheromone_grid)
        new_pheromone_grid[ants[i][0], ants[i][1]] += deposit_amount
        pygame.draw.circle(screen, (255, 0, 0), (ants[i][1] * (width // grid_size), ants[i][0] * (height // grid_size)), 3)

    pheromone_grid = new_pheromone_grid
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
