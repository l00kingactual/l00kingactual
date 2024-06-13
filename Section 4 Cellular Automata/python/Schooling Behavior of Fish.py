import numpy as np
import matplotlib.pyplot as plt

# Define the Boid class for fish
class Fish:
    def __init__(self, position, velocity):
        self.position = np.array(position)
        self.velocity = np.array(velocity)

    def update(self, fishes, perception_radius, max_speed, max_force):
        steering = np.array([0.0, 0.0])
        total = 0

        for fish in fishes:
            distance = np.linalg.norm(self.position - fish.position)
            if fish != self and distance < perception_radius:
                steering += fish.velocity
                total += 1

        if total > 0:
            steering /= total
            steering = (steering / np.linalg.norm(steering)) * max_speed
            steering -= self.velocity
            steering = (steering / np.linalg.norm(steering)) * max_force

        self.velocity += steering
        self.velocity = (self.velocity / np.linalg.norm(self.velocity)) * max_speed
        self.position += self.velocity

# Initialize parameters
num_fish = 50
perception_radius = 50
max_speed = 2
max_force = 0.05
width, height = 800, 600

# Create fish
fishes = [Fish([np.random.rand() * width, np.random.rand() * height], [np.random.rand() * 2 - 1, np.random.rand() * 2 - 1]) for _ in range(num_fish)]

# Simulation loop
def simulate():
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 6))
    while True:
        ax.clear()
        for fish in fishes:
            fish.update(fishes, perception_radius, max_speed, max_force)
            ax.plot(fish.position[0], fish.position[1], 'bo')
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
        plt.pause(0.01)

simulate()
