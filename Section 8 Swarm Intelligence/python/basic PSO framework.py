import numpy as np

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
print("Swarm Shape:", (num_particles, dimensions))
print("Global Best Position Shape:", pso.global_best_position.shape)
print("Global Best Score Shape:", np.shape(pso.global_best_score))
