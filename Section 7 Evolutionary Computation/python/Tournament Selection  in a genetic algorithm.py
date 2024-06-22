import logging
import json
import random
import numpy as np
from datetime import datetime, timezone
from PIL import Image
import matplotlib.pyplot as plt

# Constants
INITIAL_POPULATION_SIZE = 100
GENERATIONS = 500  # Increased number of generations for better convergence
INITIAL_MUTATION_RATE = 0.1
FINAL_MUTATION_RATE = 0.01
ROWS, COLS = 128, 128

# Set up logging
logger = logging.getLogger('genetic_algorithm_logger')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log_to_json(level, message, **kwargs):
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "message": message,
        "extra": kwargs
    }
    logger.log(level, json.dumps(log_entry))

class IndividualImage:
    def __init__(self):
        try:
            self.pixels = np.random.randint(0, 256, (ROWS, COLS, 3), dtype=np.uint8)
            self.fitness = 0
        except Exception as e:
            log_to_json(logging.ERROR, f"Error in IndividualImage __init__: {e}")
            raise

    def calculate_fitness(self, target_image):
        try:
            self.fitness = -np.mean((self.pixels - target_image) ** 2)
        except Exception as e:
            log_to_json(logging.ERROR, f"Error in calculate_fitness: {e}")
            raise

    def mutate(self, mutation_rate):
        try:
            for _ in range(int(mutation_rate * ROWS * COLS)):
                i, j = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
                self.pixels[i, j] = np.random.randint(0, 256, 3)
        except Exception as e:
            log_to_json(logging.ERROR, f"Error in mutate: {e}")
            raise

    @staticmethod
    def crossover(parent1, parent2):
        try:
            child = IndividualImage()
            mask = np.random.randint(0, 2, (ROWS, COLS, 1), dtype=bool)
            child.pixels = np.where(mask, parent1.pixels, parent2.pixels)
            return child
        except Exception as e:
            log_to_json(logging.ERROR, f"Error in crossover: {e}")
            raise

def tournament_selection(population, tournament_size):
    try:
        tournament = random.sample(population, tournament_size)
        tournament.sort(key=lambda ind: ind.fitness, reverse=True)
        return tournament[0]
    except Exception as e:
        log_to_json(logging.ERROR, f"Error in tournament_selection: {e}")
        raise

def genetic_algorithm_image(target_image):
    try:
        population_size = INITIAL_POPULATION_SIZE
        mutation_rate = INITIAL_MUTATION_RATE
        population = [IndividualImage() for _ in range(population_size)]
        best_fitness_values = []
        tournament_size = 5  # Adjust as needed

        for generation in range(GENERATIONS):
            log_to_json(logging.INFO, "Generation", generation=generation)
            for ind in population:
                ind.calculate_fitness(target_image)
            population.sort(key=lambda ind: ind.fitness, reverse=True)

            best_fitness_values.append(population[0].fitness)
            
            if generation % 50 == 0 and generation != 0:
                mutation_rate = max(FINAL_MUTATION_RATE, mutation_rate * 0.9)
                population_size = max(10, int(population_size * 0.9))
                population = population[:population_size]

            next_generation = population[:population_size // 2]
            while len(next_generation) < population_size:
                parent1 = tournament_selection(population, tournament_size)
                parent2 = tournament_selection(population, tournament_size)
                child = IndividualImage.crossover(parent1, parent2)
                child.mutate(mutation_rate)
                next_generation.append(child)
            population = next_generation

        best_individual = min(population, key=lambda ind: ind.fitness)
        log_to_json(logging.INFO, "Best Image", fitness=best_individual.fitness)
        return best_individual, best_fitness_values
    except Exception as e:
        log_to_json(logging.ERROR, f"Error in genetic_algorithm_image: {e}")
        raise

def visualize_image_reconstruction(best_individual, best_fitness_values, target_image):
    try:
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 3, 1)
        plt.imshow(best_individual.pixels)
        plt.title('Reconstructed Image')

        plt.subplot(1, 3, 2)
        plt.imshow(target_image)
        plt.title('Target Image')

        plt.subplot(1, 3, 3)
        plt.plot(best_fitness_values)
        plt.title('Fitness Over Generations')
        plt.xlabel('Generation')
        plt.ylabel('Fitness')

        plt.tight_layout()
        plt.show()
    except Exception as e:
        log_to_json(logging.ERROR, f"Error in visualize_image_reconstruction: {e}")
        raise

if __name__ == "__main__":
    try:
        TARGET_IMAGE_PATH = 'images/001.jpg'
        target_image = np.array(Image.open(TARGET_IMAGE_PATH).resize((ROWS, COLS)))
        best_individual, best_fitness_values = genetic_algorithm_image(target_image)
        visualize_image_reconstruction(best_individual, best_fitness_values, target_image)
    except Exception as e:
        log_to_json(logging.ERROR, f"Error in main execution: {e}")
        raise
