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

def preprocess_data(run_data):
    avg_costs = []
    min_costs = []
    max_costs = []
    k_values = []
    q_values = []
    epsilon_values = []
    
    iterations = range(len(run_data['best_solutions']))
    
    for entry in run_data['best_solutions']:
        avg_costs.append(entry['cost'])
        min_costs.append(entry['cost'])
        max_costs.append(entry['cost'])
        
    if 'k' in run_data and 'q' in run_data and 'epsilon' in run_data:
        k_values = run_data['k']
        q_values = run_data['q']
        epsilon_values = run_data['epsilon']
    
    return iterations, avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values

def plot_2d_metrics(iterations, avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values, filename):
    fig, axs = plt.subplots(3, 2, figsize=(15, 15))
    fig.suptitle(f'2D Metrics Visualization for {filename}')
    
    # Line Plot with Trend Lines
    axs[0, 0].plot(iterations, avg_costs, label='Avg Cost')
    axs[0, 0].plot(iterations, min_costs, label='Min Cost')
    axs[0, 0].plot(iterations, max_costs, label='Max Cost')
    axs[0, 0].set_title('Cost Metrics')
    axs[0, 0].legend()

    # Scatter Plot for k, q, epsilon
    if k_values and q_values and epsilon_values:
        axs[0, 1].scatter(iterations, k_values, label='k Value', alpha=0.6)
        axs[0, 1].scatter(iterations, q_values, label='q Value', alpha=0.6)
        axs[0, 1].scatter(iterations, epsilon_values, label='Epsilon Value', alpha=0.6)
    axs[0, 1].set_title('K, Q, Epsilon Values')
    axs[0, 1].legend()

    # Box Plot for Cost Metrics
    all_costs = avg_costs + min_costs + max_costs
    if all_costs:
        sns.boxplot(data=all_costs, ax=axs[1, 0])
    axs[1, 0].set_title('Cost Metrics Box Plot')

    # Box Plot for K, Q, Epsilon Values
    all_values = k_values + q_values + epsilon_values
    if all_values:
        sns.boxplot(data=all_values, ax=axs[1, 1])
    axs[1, 1].set_title('K, Q, Epsilon Values Box Plot')

    # Line Plot for K, Q, Epsilon
    if k_values and q_values and epsilon_values:
        axs[2, 0].plot(iterations, k_values, label='k Value')
        axs[2, 0].plot(iterations, q_values, label='q Value')
        axs[2, 0].plot(iterations, epsilon_values, label='Epsilon Value')
    axs[2, 0].set_title('K, Q, Epsilon Over Iterations')
    axs[2, 0].legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def plot_3d_metrics(avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values, filename):
    fig = plt.figure(figsize=(15, 15))
    fig.suptitle(f'3D Metrics Visualization for {filename}')

    # 3D Line Plot for Cost Metrics
    ax1 = fig.add_subplot(231, projection='3d')
    ax1.plot(np.arange(len(avg_costs)), avg_costs, label='Avg Cost')
    ax1.plot(np.arange(len(min_costs)), min_costs, label='Min Cost')
    ax1.plot(np.arange(len(max_costs)), max_costs, label='Max Cost')
    ax1.set_title('3D Line Plot for Cost Metrics')

    # 3D Line Plot for K, Q, Epsilon Values
    ax2 = fig.add_subplot(232, projection='3d')
    if k_values and q_values and epsilon_values:
        ax2.plot(np.arange(len(k_values)), k_values, label='k Value')
        ax2.plot(np.arange(len(q_values)), q_values, label='q Value')
        ax2.plot(np.arange(len(epsilon_values)), epsilon_values, label='Epsilon Value')
    ax2.set_title('3D Line Plot for K, Q, Epsilon Values')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# Load data
directory = 'analysis/aoc/'
data, filenames = load_json_files(directory)

# Plot metrics for each file
for run_data, filename in zip(data, filenames):
    iterations, avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values = preprocess_data(run_data)
    plot_2d_metrics(iterations, avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values, filename)
    plot_3d_metrics(avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values, filename)
