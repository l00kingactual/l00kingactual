import numpy as np
import random

# Define constants
FISH_SIZE = 5
FISH_COLOR = (0, 0, 255)  # Blue color for fish
FISH_VISUAL_RANGE = 100
FISH_AVOIDANCE_RANGE = 20
MAX_SPEED = 3
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9
EXPLORE_PROB = 0.2  # Probability of exploration

class Agent:
    def __init__(self, position, size, color):
        self.position = np.array(position, dtype=np.float64)
        self.size = size
        self.color = color
        self.velocity = np.array([0.0, 0.0], dtype=np.float64)
        self.pbest_position = np.copy(self.position)
        self.pbest_score = float('inf')

    def move(self):
        self.position += self.velocity
        self.position = np.clip(self.position, 0, 100)  # Ensure position stays within bounds

class Fish(Agent):
    def __init__(self, position, food_sources):
        super().__init__(position, FISH_SIZE, FISH_COLOR)
        self.food_sources = food_sources
        self.q_table = {}

    def get_state(self):
        # Discretize the position to use as state
        state = tuple(self.position.astype(int))
        if state not in self.q_table:
            self.q_table[state] = np.zeros(4)  # Up, down, left, right
        return state

    def choose_action(self, state):
        if random.random() < EXPLORE_PROB:
            return random.choice([0, 1, 2, 3])  # Explore: choose a random action
        return np.argmax(self.q_table[state])  # Exploit: choose the best action

    def update_q_value(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + DISCOUNT_FACTOR * self.q_table[next_state][best_next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += LEARNING_RATE * td_error

    def update(self, fish_school, global_best_position):
        state = self.get_state()
        action = self.choose_action(state)
        reward = -1  # Default reward is negative to encourage exploration

        # Perform the chosen action
        if action == 0:  # Up
            self.velocity = np.array([0, -MAX_SPEED], dtype=np.float64)
        elif action == 1:  # Down
            self.velocity = np.array([0, MAX_SPEED], dtype=np.float64)
        elif action == 2:  # Left
            self.velocity = np.array([-MAX_SPEED, 0], dtype=np.float64)
        elif action == 3:  # Right
            self.velocity = np.array([MAX_SPEED, 0], dtype=np.float64)

        self.move()
        next_state = self.get_state()

        # Calculate reward based on distance to food
        closest_food = None
        min_distance = float('inf')
        for food in self.food_sources:
            distance = np.linalg.norm(food.position - self.position)
            if distance < min_distance:
                min_distance = distance
                closest_food = food

        if closest_food and min_distance < FISH_VISUAL_RANGE:
            reward = 10 - min_distance  # Higher reward for closer food

        self.update_q_value(state, action, reward, next_state)

        # PSO-inspired updates
        if reward > self.pbest_score:
            self.pbest_score = reward
            self.pbest_position = np.copy(self.position)

        self.velocity += LEARNING_RATE * (self.pbest_position - self.position) + \
                         LEARNING_RATE * (global_best_position - self.position)
        if np.linalg.norm(self.velocity) > 0:
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

        self.move()

class FoodSource:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=np.float64)

# Example usage
food_sources = [FoodSource(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]
fish_school = [Fish([random.randint(0, 100), random.randint(0, 100)], food_sources) for _ in range(5)]
global_best_position = np.zeros(2, dtype=np.float64)

for _ in range(100):
    for fish in fish_school:
        fish.update(fish_school, global_best_position)
        print(f"Fish position: {fish.position}")
        if fish.pbest_score > np.linalg.norm(global_best_position):
            global_best_position = fish.pbest_position
