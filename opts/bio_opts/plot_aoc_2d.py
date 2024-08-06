import os
import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

def load_json_files(directory):
    data = []
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                try:
                    data.append(json.load(file))
                    filenames.append(filename)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from {filepath}: {e}")
    return data, filenames

def preprocess_data(data):
    avg_costs = []
    min_costs = []
    max_costs = []
    k_values = []
    q_values = []
    epsilon_values = []
    
    iterations = None
    
    for run_data in data:
        if 'best_solutions' in run_data:
            if iterations is None:
                iterations = range(len(run_data['best_solutions']))
            avg_costs.append([entry['cost'] for entry in run_data['best_solutions']])
            min_costs.append([entry['cost'] for entry in run_data['best_solutions']])
            max_costs.append([entry['cost'] for entry in run_data['best_solutions']])
        if 'k' in run_data and 'q' in run_data and 'epsilon' in run_data:
            k_values.append(run_data['k'])
            q_values.append(run_data['q'])
            epsilon_values.append(run_data['epsilon'])
    
    return iterations, avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values

def plot_2d_metrics(iterations, avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values, filenames):
    fig, axs = plt.subplots(3, 2, figsize=(15, 15))
    fig.suptitle('2D Metrics Visualization')
    
    # Line Plot with Trend Lines
    for avg, min_c, max_c in zip(avg_costs, min_costs, max_costs):
        axs[0, 0].plot(iterations, avg, label='Avg Cost')
        axs[0, 0].plot(iterations, min_c, label='Min Cost')
        axs[0, 0].plot(iterations, max_c, label='Max Cost')
    axs[0, 0].set_title('Cost Metrics')
    axs[0, 0].legend()

    # Scatter Plot for k, q, epsilon
    if k_values and q_values and epsilon_values:
        for k, q, epsilon in zip(k_values, q_values, epsilon_values):
            axs[0, 1].scatter(iterations, k, label='k Value', alpha=0.6)
            axs[0, 1].scatter(iterations, q, label='q Value', alpha=0.6)
            axs[0, 1].scatter(iterations, epsilon, label='Epsilon Value', alpha=0.6)
        axs[0, 1].set_title('K, Q, Epsilon Values')
        axs[0, 1].legend()

    # Box Plot for Cost Metrics
    all_costs = []
    for avg, min_c, max_c in zip(avg_costs, min_costs, max_costs):
        all_costs.extend(avg)
        all_costs.extend(min_c)
        all_costs.extend(max_c)
    if all_costs:
        sns.boxplot(data=all_costs, ax=axs[1, 0])
    axs[1, 0].set_title('Cost Metrics Box Plot')

    # Box Plot for K, Q, Epsilon Values
    all_values = []
    for k, q, epsilon in zip(k_values, q_values, epsilon_values):
        all_values.extend(k)
        all_values.extend(q)
        all_values.extend(epsilon)
    if all_values:
        sns.boxplot(data=all_values, ax=axs[1, 1])
    axs[1, 1].set_title('K, Q, Epsilon Values Box Plot')

    # Line Plot for K, Q, Epsilon
    if k_values and q_values and epsilon_values:
        for k, q, epsilon in zip(k_values, q_values, epsilon_values):
            axs[2, 0].plot(iterations, k, label='k Value')
            axs[2, 0].plot(iterations, q, label='q Value')
            axs[2, 0].plot(iterations, epsilon, label='Epsilon Value')
        axs[2, 0].set_title('K, Q, Epsilon Over Iterations')
        axs[2, 0].legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# Load data
directory = '/mnt/data'
data, filenames = load_json_files(directory)

# Preprocess data
iterations, avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values = preprocess_data(data)

# Plot 2D metrics
plot_2d_metrics(iterations, avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values, filenames)
