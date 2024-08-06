import numpy as np
import json

class Particle:
    def __init__(self, dimensions):
        self.position = np.random.rand(dimensions) * 10 - 5  # Initialize within a wider range
        self.velocity = np.random.rand(dimensions) - 0.5
        self.best_position = self.position.copy()
        self.best_value = float('inf')

    def update_velocity(self, global_best_position, inertia, cognitive, social):
        r1 = np.random.rand(len(self.position))
        r2 = np.random.rand(len(self.position))
        cognitive_velocity = cognitive * r1 * (self.best_position - self.position)
        social_velocity = social * r2 * (global_best_position - self.position)
        self.velocity = inertia * self.velocity + cognitive_velocity + social_velocity

    def update_position(self):
        self.position += self.velocity
        self.position = np.clip(self.position, -10, 10)  # Assuming the position should stay within [-10, 10]

class Swarm:
    def __init__(self, num_particles, dimensions, inertia=0.7, cognitive=1.4, social=1.4, patience=100):
        self.num_particles = num_particles
        self.dimensions = dimensions
        self.particles = [Particle(dimensions) for _ in range(num_particles)]
        self.global_best_position = np.random.rand(dimensions) * 10 - 5
        self.global_best_value = float('inf')
        self.inertia = inertia
        self.cognitive = cognitive
        self.social = social
        self.patience = patience
        self.stagnation_count = 0

    def optimize(self, function, iterations):
        improvements = []
        previous_best_value = self.global_best_value

        for iteration in range(iterations):
            if self.stagnation_count > self.patience:
                self._reinitialize_particles()
                self.stagnation_count = 0
                previous_best_value = float('inf')

            for particle in self.particles:
                value = function(particle.position)
                if value < particle.best_value:
                    particle.best_value = value
                    particle.best_position = particle.position.copy()

                if value < self.global_best_value:
                    self.global_best_value = value
                    self.global_best_position = particle.position.copy()
                    self.stagnation_count = 0
                else:
                    self.stagnation_count += 1

            for particle in self.particles:
                particle.update_velocity(self.global_best_position, self.inertia, self.cognitive, self.social)
                particle.update_position()

            self._adapt_parameters()

            if iteration > 0 and previous_best_value != self.global_best_value:
                improvement = ((previous_best_value - self.global_best_value) / abs(previous_best_value)) * 100
                improvements.append(improvement)
                previous_best_value = self.global_best_value

            print(f'Iteration {iteration}: Global Best Value = {self.global_best_value}')

        greatest_improvement = max(improvements) if improvements else 0
        mean_improvement = np.mean(improvements) if improvements else 0
        print(f'Greatest Percentage Improvement: {greatest_improvement:.2f}%')
        print(f'Mean Percentage Improvement: {mean_improvement:.2f}%')

        results = {
            "greatest_improvement": greatest_improvement,
            "mean_improvement": mean_improvement,
            "global_best_value": self.global_best_value,
            "global_best_position": self.global_best_position.tolist()
        }

        return results

    def _reinitialize_particles(self):
        print("Reinitializing particles to increase diversity.")
        self.particles = [Particle(self.dimensions) for _ in range(self.num_particles)]
        self.global_best_position = np.random.rand(self.dimensions) * 10 - 5
        self.global_best_value = float('inf')

    def _adapt_parameters(self):
        self.inertia = max(0.4, self.inertia * 0.99)
        self.cognitive = min(2.0, self.cognitive * 1.01)
        self.social = min(2.0, self.social * 1.01)

def objective_function(x):
    # More complex function to avoid easy minimization
    return np.sum(x**2 + 10 * np.cos(2 * np.pi * x))

if __name__ == "__main__":
    # Reduced parameters for demonstration
    num_particles = 5000
    dimensions = 13
    iterations = 4096
    patience = 100  # Early stopping if no improvement for 100 iterations

    swarm = Swarm(num_particles, dimensions, patience=patience)
    results = swarm.optimize(objective_function, iterations)

    print(f'Best Position: {results["global_best_position"]}')
    print(f'Best Value: {results["global_best_value"]}')

    # Save results to JSON
    output_file = 'results/swarm_intelligence.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

    print(f"Results saved to {output_file}")
