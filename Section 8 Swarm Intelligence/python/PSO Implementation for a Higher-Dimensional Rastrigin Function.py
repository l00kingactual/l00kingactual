import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# PSO Constants
NUM_PARTICLES = 30
NUM_ITERATIONS = 200
DIMENSIONS = 10  # Increased number of dimensions
INERTIA_WEIGHT = 0.5
COGNITIVE_WEIGHT = 1.5
SOCIAL_WEIGHT = 1.5
BOUNDS = [-5.12, 5.12]

# Rastrigin Function
def rastrigin(x):
    return 10 * len(x) + sum(x_i ** 2 - 10 * np.cos(2 * np.pi * x_i) for x_i in x)

# Particle Class
class Particle:
    def __init__(self, bounds):
        self.position = np.random.uniform(bounds[0], bounds[1], DIMENSIONS)
        self.velocity = np.random.uniform(-1, 1, DIMENSIONS)
        self.best_position = self.position.copy()
        self.best_value = rastrigin(self.position)

    def update_velocity(self, global_best_position):
        r1 = np.random.random(DIMENSIONS)
        r2 = np.random.random(DIMENSIONS)
        cognitive_component = COGNITIVE_WEIGHT * r1 * (self.best_position - self.position)
        social_component = SOCIAL_WEIGHT * r2 * (global_best_position - self.position)
        self.velocity = INERTIA_WEIGHT * self.velocity + cognitive_component + social_component

    def update_position(self, bounds):
        self.position += self.velocity
        self.position = np.clip(self.position, bounds[0], bounds[1])
        current_value = rastrigin(self.position)
        if current_value < self.best_value:
            self.best_position = self.position.copy()
            self.best_value = current_value

# PSO Algorithm
def pso():
    particles = [Particle(BOUNDS) for _ in range(NUM_PARTICLES)]
    global_best_position = min(particles, key=lambda p: p.best_value).best_position
    global_best_value = rastrigin(global_best_position)

    best_values = []

    for iteration in range(NUM_ITERATIONS):
        for particle in particles:
            particle.update_velocity(global_best_position)
            particle.update_position(BOUNDS)
            if rastrigin(particle.best_position) < global_best_value:
                global_best_position = particle.best_position
                global_best_value = rastrigin(global_best_position)
        
        best_values.append(global_best_value)
        print(f"Iteration {iteration}: Best Value = {global_best_value}")

    return global_best_position, global_best_value, best_values, particles

# Run PSO
best_position, best_value, best_values, particles = pso()

print(f"Best Position: {best_position}")
print(f"Best Value: {best_value}")

# Plot Convergence and Particle Positions in 3D
fig = plt.figure(figsize=(14, 7))

# 2D Convergence Plot
ax_2d = fig.add_subplot(121)
ax_2d.plot(best_values)
ax_2d.set_title("PSO Convergence")
ax_2d.set_xlabel("Iteration")
ax_2d.set_ylabel("Best Value")

# 3D Particle Positions Plot
ax_3d = fig.add_subplot(122, projection='3d')
positions = np.array([p.position for p in particles])
x_coords = positions[:, 0]
y_coords = positions[:, 1]
z_coords = [rastrigin(pos) for pos in positions]
ax_3d.scatter(x_coords, y_coords, z_coords, color='red')
ax_3d.set_title("Particle Positions in 3D")
ax_3d.set_xlabel("X Coordinates", labelpad=15, fontsize=12)
ax_3d.set_ylabel("Y Coordinates", labelpad=15, fontsize=12)
ax_3d.set_zlabel("Rastrigin Value", labelpad=15, fontsize=12)

# Customize tick labels
ax_3d.tick_params(axis='x', labelsize=8, pad=5)
ax_3d.tick_params(axis='y', labelsize=8, pad=5)
ax_3d.tick_params(axis='z', labelsize=8, pad=5)

# Plot the global best position as a blue point
ax_3d.scatter(best_position[0], best_position[1], rastrigin(best_position), color='blue', marker='x', s=100)
plt.show()
