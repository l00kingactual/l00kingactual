import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the Schwefel function
def schwefel_function(X):
    return 418.9829 * len(X) - np.sum(X * np.sin(np.sqrt(np.abs(X))))

# PSO parameters
population_size = 50
dimensions = 2
bounds = [-500, 500]
generations = 200  # Increased number of generations
w = 0.9  # Increased inertia weight to slow down convergence
c1 = 0.5  # Reduced cognitive (particle) coefficient
c2 = 0.5  # Reduced social (swarm) coefficient

# Initialize population
population = np.random.uniform(bounds[0], bounds[1], (population_size, dimensions))
velocity = np.random.uniform(-1, 1, (population_size, dimensions))
personal_best = np.copy(population)
personal_best_scores = np.array([schwefel_function(p) for p in population])
global_best = personal_best[np.argmin(personal_best_scores)]
global_best_score = np.min(personal_best_scores)

# For visualization purposes
fig, ax = plt.subplots()
scat = ax.scatter(population[:, 0], population[:, 1], c='blue', marker='o')
plt.xlim(bounds[0], bounds[1])
plt.ylim(bounds[0], bounds[1])
plt.title('Particle Swarm Optimization - Schwefel Function')
plt.xlabel('x1')
plt.ylabel('x2')

def animate(i):
    global population, velocity, personal_best, personal_best_scores, global_best, global_best_score
    r1, r2 = np.random.rand(2)
    velocity = w * velocity + c1 * r1 * (personal_best - population) + c2 * r2 * (global_best - population)
    population += velocity
    population = np.clip(population, bounds[0], bounds[1])

    # Update personal best
    for j in range(population_size):
        score = schwefel_function(population[j])
        if score < personal_best_scores[j]:
            personal_best[j] = population[j]
            personal_best_scores[j] = score

    # Update global best
    best_particle = np.argmin(personal_best_scores)
    if personal_best_scores[best_particle] < global_best_score:
        global_best = personal_best[best_particle]
        global_best_score = personal_best_scores[best_particle]

    # Update scatter plot
    scat.set_offsets(population)
    ax.set_title(f'Generation {i + 1}, Best Score: {global_best_score:.6f}')

# Create animation
ani = FuncAnimation(fig, animate, frames=generations, interval=200, repeat=False)
plt.show()

print(f'Best Solution: {global_best}, Best Score: {global_best_score:.6f}')
