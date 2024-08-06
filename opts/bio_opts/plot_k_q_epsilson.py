import json
import matplotlib.pyplot as plt

# Load JSON data
file_path = 'analysis/aoc/aoc_results_20240803_025853.json'

# Load the JSON data from the file
with open(file_path) as f:
    data = json.load(f)

# Extract the values of k, q, and epsilon
k_values = data['k_values']
q_values = data['q_values']
epsilon_values = data['epsilon_values']

# Create the plot
plt.figure(figsize=(12, 8))

# Plot k values
plt.subplot(3, 1, 1)
plt.plot(k_values, label='k values')
plt.xlabel('Iteration')
plt.ylabel('k')
plt.legend()

# Plot q values
plt.subplot(3, 1, 2)
plt.plot(q_values, label='q values')
plt.xlabel('Iteration')
plt.ylabel('q')
plt.legend()

# Plot epsilon values
plt.subplot(3, 1, 3)
plt.plot(epsilon_values, label='epsilon values')
plt.xlabel('Iteration')
plt.ylabel('epsilon')
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()


import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.ndimage import gaussian_filter1d

# Load the JSON data
with open('analysis/aoc/aoc_results_20240803_025853.json', 'r') as file:
    data = json.load(file)

# Assuming the correct structure based on the previous script, we might have:
iterations = data.get('iterations', [])

# Extract ks, qs, and epsilons
ks = []
qs = []
epsilons = []

for iteration in iterations:
    ks.append(iteration.get('K', np.nan))
    qs.append(iteration.get('Q', np.nan))
    epsilons.append(iteration.get('epsilon', np.nan))

# Convert to numpy arrays for better handling
ks = np.array(ks, dtype=np.float64)
qs = np.array(qs, dtype=np.float64)
epsilons = np.array(epsilons, dtype=np.float64)

# Remove NaN values for calculations
ks = ks[~np.isnan(ks)]
qs = qs[~np.isnan(qs)]
epsilons = epsilons[~np.isnan(epsilons)]

# Statistical Analysis
k_mean = np.mean(ks)
k_var = np.var(ks)
k_std = np.std(ks)

q_mean = np.mean(qs)
q_var = np.var(qs)
q_std = np.std(qs)

epsilon_mean = np.mean(epsilons)
epsilon_var = np.var(epsilons)
epsilon_std = np.std(epsilons)

statistical_analysis = {
    "k": {"mean": k_mean, "variance": k_var, "std_dev": k_std},
    "q": {"mean": q_mean, "variance": q_var, "std_dev": q_std},
    "epsilon": {"mean": epsilon_mean, "variance": epsilon_var, "std_dev": epsilon_std}
}

# Smoothing
ks_smooth = gaussian_filter1d(ks, sigma=2)
qs_smooth = gaussian_filter1d(qs, sigma=2)
epsilons_smooth = gaussian_filter1d(epsilons, sigma=2)

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(12, 18))

axs[0].plot(ks, label='k values')
axs[0].plot(ks_smooth, label='Smoothed k values')
axs[0].set_title('k values over Iterations')
axs[0].set_xlabel('Iteration')
axs[0].set_ylabel('k')
axs[0].legend()

axs[1].plot(qs, label='q values')
axs[1].plot(qs_smooth, label='Smoothed q values')
axs[1].set_title('q values over Iterations')
axs[1].set_xlabel('Iteration')
axs[1].set_ylabel('q')
axs[1].legend()

axs[2].plot(epsilons, label='epsilon values')
axs[2].plot(epsilons_smooth, label='Smoothed epsilon values')
axs[2].set_title('epsilon values over Iterations')
axs[2].set_xlabel('Iteration')
axs[2].set_ylabel('epsilon')
axs[2].legend()

plt.tight_layout()
plt.show()

# Heatmap or Scatter Plot
data_frame = pd.DataFrame({
    'k': ks,
    'q': qs,
    'epsilon': epsilons
})

pairplot = sns.pairplot(data_frame)
plt.show()

statistical_analysis
