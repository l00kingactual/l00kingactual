import numpy as np
import matplotlib.pyplot as plt

# Define parameters
alpha = 0.1  # Prey birth rate
beta = 0.02  # Predation rate
gamma = 0.1  # Predator death rate
delta = 0.01 # Predator reproduction rate

# Initialize populations
prey = 40
predators = 9
timesteps = 200

# Lists to store population sizes
prey_population = []
predator_population = []

# Simulation loop
for t in range(timesteps):
    prey_population.append(prey)
    predator_population.append(predators)
    
    # Update populations based on Lotka-Volterra equations
    prey = prey + alpha * prey - beta * prey * predators
    predators = predators + delta * prey * predators - gamma * predators

# Plot the results
plt.plot(prey_population, label='Prey')
plt.plot(predator_population, label='Predators')
plt.legend()
plt.title("Predator-Prey Dynamics")
plt.xlabel("Time")
plt.ylabel("Population Size")
plt.show()
