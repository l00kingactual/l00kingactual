import numpy as np
import matplotlib.pyplot as plt

# PSO Classes and Functions

class Particle:
    def __init__(self, dimensions):
        self.position = np.random.rand(dimensions)
        self.velocity = np.random.rand(dimensions)
        self.best_position = self.position.copy()
        self.best_score = float('inf')

class PSO:
    def __init__(self, objective_func, dimensions, num_particles, max_iter):
        self.objective_func = objective_func
        self.dimensions = dimensions
        self.num_particles = num_particles
        self.max_iter = max_iter
        self.swarm = [Particle(dimensions) for _ in range(num_particles)]
        self.global_best_position = np.random.rand(dimensions)
        self.global_best_score = float('inf')

    def optimize(self):
        for iteration in range(self.max_iter):
            for particle in self.swarm:
                score = self.objective_func(particle.position)
                if score < particle.best_score:
                    particle.best_score = score
                    particle.best_position = particle.position.copy()
                if score < self.global_best_score:
                    self.global_best_score = score
                    self.global_best_position = particle.position.copy()

            for particle in self.swarm:
                inertia = 0.5 * particle.velocity
                cognitive = 2.0 * np.random.rand(self.dimensions) * (particle.best_position - particle.position)
                social = 2.0 * np.random.rand(self.dimensions) * (self.global_best_position - particle.position)
                particle.velocity = inertia + cognitive + social
                particle.position += particle.velocity

            print(f"Iteration {iteration+1}/{self.max_iter}, Best Score: {self.global_best_score}")

def objective_function(x):
    return np.sum(x**2)

# PSO Execution
dimensions = 5
num_particles = 30
max_iter = 100

pso = PSO(objective_function, dimensions, num_particles, max_iter)
pso.optimize()

print("Optimized Position:", pso.global_best_position)
print("Optimized Score:", pso.global_best_score)

# Reporting data shapes
print("Swarm Shape:", (num_particles, dimensions))
print("Global Best Position Shape:", pso.global_best_position.shape)
print("Global Best Score Shape:", np.shape(pso.global_best_score))

def plot_line(data, title, ax):
    for i in range(data.shape[0]):
        ax.plot(data[i], label=f'Line {i}')
    ax.set_title(title)
    ax.legend()

def plot_scatter(data, title, ax):
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    scatter = ax.scatter(x, y, c=data.flatten(), cmap='viridis')
    ax.set_title(title)
    plt.colorbar(scatter, ax=ax)

def plot_bar(data, title, ax):
    x = np.arange(data.shape[0])
    for i in range(data.shape[1]):
        ax.bar(x + i * 0.2, data[:, i], width=0.2, label=f'Bar {i}')
    ax.set_title(title)
    ax.legend()

def plot_histogram(data, title, ax):
    ax.hist(data.flatten(), bins=20, color='blue', alpha=0.7)
    ax.set_title(title)

def plot_box(data, title, ax):
    ax.boxplot(data)
    ax.set_title(title)

def plot_heatmap(data, title, ax):
    cax = ax.imshow(data, cmap='viridis', aspect='auto')
    ax.set_title(title)
    plt.colorbar(cax, ax=ax)

def plot_pie(data, title, ax):
    data_sum = data.sum(axis=0)
    ax.pie(data_sum, labels=[f'Pie {i}' for i in range(data.shape[1])], autopct='%1.1f%%')
    ax.set_title(title)

data = np.random.rand(5, 5)

# Plotting the 2D charts
fig1, axs1 = plt.subplots(2, 2, figsize=(10, 8))
plot_line(data, 'Line Plot', axs1[0, 0])
plot_scatter(data, 'Scatter Plot', axs1[0, 1])
plot_bar(data, 'Bar Plot', axs1[1, 0])
plot_histogram(data, 'Histogram', axs1[1, 1])
plt.tight_layout()
plt.show()

fig2, axs2 = plt.subplots(2, 2, figsize=(10, 8))
plot_box(data, 'Box Plot', axs2[0, 0])
plot_heatmap(data, 'Heatmap', axs2[0, 1])
plot_pie(data, 'Pie Chart', axs2[1, 0])
plt.tight_layout()
plt.show()



