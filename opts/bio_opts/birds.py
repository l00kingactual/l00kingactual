import numpy as np
import random

# Define constants
BIRD_SIZE = 5
BIRD_COLOR = (0, 0, 255)  # Blue color for birds
BIRD_VISUAL_RANGE = 100
BIRD_AVOIDANCE_RANGE = 20
MAX_SPEED = 3

class Agent:
    def __init__(self, position, size, color):
        self.position = np.array(position, dtype=np.float64)
        self.size = size
        self.color = color
        self.velocity = np.array([0.0, 0.0], dtype=np.float64)

    def move(self):
        self.position += self.velocity

class Bird(Agent):
    def __init__(self, position, food_sources):
        super().__init__(position, BIRD_SIZE, BIRD_COLOR)
        self.food_sources = food_sources

    def update(self, bird_flock):
        center_of_mass = np.array([0.0, 0.0])
        alignment = np.array([0.0, 0.0])
        avoidance = np.array([0.0, 0.0])
        num_neighbors = 0

        for bird in bird_flock:
            if bird != self:
                distance = np.linalg.norm(bird.position - self.position)
                if distance < BIRD_VISUAL_RANGE:
                    center_of_mass += bird.position
                    alignment += bird.velocity
                    if distance < BIRD_AVOIDANCE_RANGE:
                        avoidance -= (bird.position - self.position)
                    num_neighbors += 1

        if num_neighbors > 0:
            center_of_mass /= num_neighbors
            alignment /= num_neighbors
            direction_to_com = center_of_mass - self.position
            direction_to_com = direction_to_com / np.linalg.norm(direction_to_com) * MAX_SPEED
            alignment = alignment / np.linalg.norm(alignment) * MAX_SPEED
            avoidance = avoidance / np.linalg.norm(avoidance) * MAX_SPEED

            self.velocity = (direction_to_com + alignment + avoidance) / 3
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

        closest_food = None
        min_distance = float('inf')
        for food in self.food_sources:
            distance = np.linalg.norm(food.position - self.position)
            if distance < min_distance:
                min_distance = distance
                closest_food = food

        if closest_food and min_distance < BIRD_VISUAL_RANGE:
            direction_to_food = closest_food.position - self.position
            direction_to_food = direction_to_food / np.linalg.norm(direction_to_food) * MAX_SPEED
            self.velocity = (self.velocity + direction_to_food) / 2
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

        self.move()

class FoodSource:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=np.float64)

# Example usage
food_sources = [FoodSource(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]
birds = [Bird([random.randint(0, 100), random.randint(0, 100)], food_sources) for _ in range(5)]
for _ in range(100):
    for bird in birds:
        bird.update(birds)
        print(f"Bird position: {bird.position}")
