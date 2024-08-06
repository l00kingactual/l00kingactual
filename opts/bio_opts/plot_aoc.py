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
    valid_data = []
    for run_data in data:
        if isinstance(run_data, list) and all(isinstance(entry, dict) and 'avg_cost' in entry for entry in run_data):
            valid_data.append(run_data)
    
    avg_costs = []
    min_costs = []
    max_costs = []
    k_values = []
    q_values = []
    epsilon_values = []
    
    for run_data in valid_data:
        avg_costs.append([entry['avg_cost'] for entry in run_data])
        min_costs.append([entry['min_cost'] for entry in run_data])
        max_costs.append([entry['max_cost'] for entry in run_data])
        if 'k_value' in run_data[0] and 'q_value' in run_data[0] and 'epsilon_value' in run_data[0]:
            k_values.append([entry['k_value'] for entry in run_data])
            q_values.append([entry['q_value'] for entry in run_data])
            epsilon_values.append([entry['epsilon_value'] for entry in run_data])
    
    return avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values

def plot_2d_metrics(avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values, filenames):
    fig, axs = plt.subplots(3, 2, figsize=(15, 15))
    fig.suptitle('2D Metrics Visualization')
    
    # Line Plot with Trend Lines
    for avg, min_c, max_c in zip(avg_costs, min_costs, max_costs):
        iterations = range(len(avg))
        axs[0, 0].plot(iterations, avg, label='Avg Cost')
        axs[0, 0].plot(iterations, min_c, label='Min Cost')
        axs[0, 0].plot(iterations, max_c, label='Max Cost')
    axs[0, 0].set_title('Cost Metrics')
    axs[0, 0].legend()

    # Scatter Plot for k, q, epsilon
    for k, q, epsilon in zip(k_values, q_values, epsilon_values):
        iterations = range(len(k))
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
    sns.boxplot(data=all_costs, ax=axs[1, 0])
    axs[1, 0].set_title('Cost Metrics Box Plot')

    # Box Plot for K, Q, Epsilon Values
    all_values = []
    for k, q, epsilon in zip(k_values, q_values, epsilon_values):
        all_values.extend(k)
        all_values.extend(q)
        all_values.extend(epsilon)
    sns.boxplot(data=all_values, ax=axs[1, 1])
    axs[1, 1].set_title('K, Q, Epsilon Values Box Plot')

    # Line Plot for K, Q, Epsilon
    for k, q, epsilon in zip(k_values, q_values, epsilon_values):
        iterations = range(len(k))
        axs[2, 0].plot(iterations, k, label='k Value')
        axs[2, 0].plot(iterations, q, label='q Value')
        axs[2, 0].plot(iterations, epsilon, label='Epsilon Value')
    axs[2, 0].set_title('K, Q, Epsilon Over Iterations')
    axs[2, 0].legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def plot_3d_metrics(avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values, filenames):
    fig = plt.figure(figsize=(15, 15))
    fig.suptitle('3D Metrics Visualization')

    num_files = len(filenames)
    zs = np.arange(num_files)

    # 3D Line Plot for Cost Metrics
    ax1 = fig.add_subplot(231, projection='3d')
    for i, (avg, min_c, max_c) in enumerate(zip(avg_costs, min_costs, max_costs)):
        iterations = np.arange(len(avg))
        ax1.plot(iterations, avg, zs=zs[i], label=f'Avg Cost Run {i+1}')
        ax1.plot(iterations, min_c, zs=zs[i], label=f'Min Cost Run {i+1}')
        ax1.plot(iterations, max_c, zs=zs[i], label=f'Max Cost Run {i+1}')
    ax1.set_title('3D Line Plot for Cost Metrics')

    # 3D Line Plot for K, Q, Epsilon Values
    ax2 = fig.add_subplot(232, projection='3d')
    for i, (k, q, epsilon) in enumerate(zip(k_values, q_values, epsilon_values)):
        iterations = np.arange(len(k))
        ax2.plot(iterations, k, zs=zs[i], label=f'k Value Run {i+1}')
        ax2.plot(iterations, q, zs=zs[i], label=f'q Value Run {i+1}')
        ax2.plot(iterations, epsilon, zs=zs[i], label=f'Epsilon Value Run {i+1}')
    ax2.set_title('3D Line Plot for K, Q, Epsilon Values')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# Load data
directory = 'analysis/aoc/'
data, filenames = load_json_files(directory)

# Preprocess data
avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values = preprocess_data(data)

# Plot 2D metrics
plot_2d_metrics(avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values, filenames)

# Plot 3D metrics
plot_3d_metrics(avg_costs, min_costs, max_costs, k_values, q_values, epsilon_values, filenames)
