import numpy as np
import pygame
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Objective function for optimization
def objective_function(x):
    try:
        result = np.sum(x**4)  # Increased complexity to slow convergence
        return result
    except Exception as e:
        logging.error(f"Error in objective_function: {e}")
        return np.inf

# Initialize the population with random values within bounds
def initialize_population(pop_size, dim, bounds):
    try:
        population = np.random.uniform(bounds[0], bounds[1], (pop_size, dim))
        return population
    except Exception as e:
        logging.error(f"Error in initialize_population: {e}")
        return np.empty((pop_size, dim))

# Calculate fitness for the entire population
def calculate_fitness(population):
    try:
        fitness = np.array([objective_function(ind) for ind in population])
        return fitness
    except Exception as e:
        logging.error(f"Error in calculate_fitness: {e}")
        return np.inf * np.ones(len(population))

# Hybrid ABC-Tabu Search Algorithm
def abc_tabu_search(pop_size, dim, bounds, num_iterations, tabu_size):
    try:
        population = initialize_population(pop_size, dim, bounds)
        fitness = calculate_fitness(population)

        tabu_list = []
        best_solution = population[np.argmin(fitness)]
        best_fitness = np.min(fitness)

        history = []

        for iteration in range(num_iterations):
            logging.info(f"Iteration {iteration + 1}/{num_iterations}, Best Fitness: {best_fitness}")

            # Employed bees phase
            for i in range(pop_size):
                new_solution = population[i] + np.random.uniform(-0.1, 0.1, dim)  # Reduced step size
                new_fitness = objective_function(new_solution)
                if new_fitness < fitness[i]:
                    population[i] = new_solution
                    fitness[i] = new_fitness

            # Onlooker bees phase
            for i in range(pop_size):
                selected_bee = population[np.random.choice(pop_size, p=fitness/fitness.sum())]
                new_solution = selected_bee + np.random.uniform(-0.1, 0.1, dim)  # Reduced step size
                new_fitness = objective_function(new_solution)
                if new_fitness < fitness[i]:
                    population[i] = new_solution
                    fitness[i] = new_fitness

            # Scout bees phase
            if np.random.rand() < 0.05:  # Reduced probability
                scout_idx = np.argmax(fitness)
                population[scout_idx] = np.random.uniform(bounds[0], bounds[1], dim)
                fitness[scout_idx] = objective_function(population[scout_idx])

            # Tabu Search
            best_index = np.argmin(fitness)
            candidate_solution = population[best_index].copy()

            if candidate_solution.tolist() not in tabu_list:
                new_solution = candidate_solution + np.random.uniform(-0.05, 0.05, dim)  # Reduced step size
                new_fitness = objective_function(new_solution)
                if new_fitness < fitness[best_index]:
                    population[best_index] = new_solution
                    fitness[best_index] = new_fitness
                    tabu_list.append(candidate_solution.tolist())
                    if len(tabu_list) > tabu_size:
                        tabu_list.pop(0)

            best_solution = population[np.argmin(fitness)]
            best_fitness = np.min(fitness)
            history.append((population.copy(), fitness.copy()))

        return history, best_solution, best_fitness
    except Exception as e:
        logging.error(f"Error in abc_tabu_search: {e}")
        return [], np.empty(dim), np.inf

# Pygame Initialization
pygame.init()

# Screen dimensions
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hybrid ABC-Tabu Search Optimization')

# Color settings
background_color = (0, 0, 0)
bee_color = (0, 255, 0)
best_bee_color = (255, 0, 0)
dim = 2
bounds = [-5, 5]

# Convert coordinates to Pygame's screen coordinates
def to_screen_coords(x, y):
    try:
        screen_x = int((x - bounds[0]) / (bounds[1] - bounds[0]) * width)
        screen_y = int((y - bounds[0]) / (bounds[1] - bounds[0]) * height)
        return screen_x, screen_y
    except Exception as e:
        logging.error(f"Error in to_screen_coords: {e}")
        return 0, 0

# Draw the population of bees
def draw_population(screen, population, best_solution):
    try:
        screen.fill(background_color)
        for bee in population:
            x, y = to_screen_coords(bee[0], bee[1])
            pygame.draw.circle(screen, bee_color, (x, y), 3)
        best_x, best_y = to_screen_coords(best_solution[0], best_solution[1])
        pygame.draw.circle(screen, best_bee_color, (best_x, best_y), 5)
    except Exception as e:
        logging.error(f"Error in draw_population: {e}")

# Parameters
pop_size = 100
num_iterations = 200
tabu_size = 15

# Run the hybrid ABC-Tabu Search
history, best_solution, best_fitness = abc_tabu_search(pop_size, dim, bounds, num_iterations, tabu_size)

# Main loop
running = True
iteration = 0
clock = pygame.time.Clock()

while running and iteration < num_iterations:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw population and best solution
        draw_population(screen, history[iteration][0], best_solution)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(5)  # Adjust to control the speed of the animation, slower than before

        # Move to the next iteration
        iteration += 1
    except Exception as e:
        logging.error(f"Error in main loop: {e}")
        running = False

pygame.quit()
