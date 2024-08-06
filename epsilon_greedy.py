import numpy as np
import pandas as pd
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from compute_metrics import compute_metrics, save_metrics_to_json

# Define all strategies
def epsilon_greedy(q_table, state, epsilon=0.1):
    if np.random.rand() < epsilon:
        action = np.random.choice(q_table.shape[1])
    else:
        action = np.argmax(q_table.loc[state])
    return action

def ucb1(q_table, state, counts, total_counts):
    ucb_values = q_table.loc[state] + np.sqrt(2 * np.log(total_counts) / (counts + 1))
    return np.argmax(ucb_values)

def thompson_sampling(q_table, state):
    sampled_values = np.random.beta(q_table.loc[state] + 1, 1)
    return np.argmax(sampled_values)

def softmax(q_table, state, tau=1.0):
    exp_values = np.exp(q_table.loc[state] / tau)
    probabilities = exp_values / np.sum(exp_values)
    return np.random.choice(len(probabilities), p=probabilities)

def exp3(q_table, state, gamma=0.1):
    exp_values = np.exp(gamma * q_table.loc[state])
    probabilities = exp_values / np.sum(exp_values)
    return np.random.choice(len(probabilities), p=probabilities)

def bayesian_ucb(q_table, state, total_counts, alpha=1.0):
    sampled_values = q_table.loc[state] + alpha * np.sqrt(np.log(total_counts + 1) / (total_counts + 1))
    return np.argmax(sampled_values)

def greedy(q_table, state):
    return np.argmax(q_table.loc[state])

def random_selection(q_table, state):
    return np.random.choice(q_table.shape[1])

# Hybrid strategy to select the best action based on a given strategy
def hybrid_strategy(q_table, state, counts, total_counts, epsilon=0.1, strategy='epsilon_greedy'):
    if strategy == 'epsilon_greedy':
        return epsilon_greedy(q_table, state, epsilon)
    elif strategy == 'ucb1':
        return ucb1(q_table, state, counts, total_counts)
    elif strategy == 'thompson_sampling':
        return thompson_sampling(q_table, state)
    elif strategy == 'softmax':
        return softmax(q_table, state)
    elif strategy == 'exp3':
        return exp3(q_table, state)
    elif strategy == 'bayesian_ucb':
        return bayesian_ucb(q_table, state, total_counts)
    elif strategy == 'greedy':
        return greedy(q_table, state)
    elif strategy == 'random_selection':
        return random_selection(q_table, state)
    else:
        return epsilon_greedy(q_table, state, epsilon)

# Save metrics to JSON
def save_metrics_to_json(metrics, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(metrics, f, indent=4, default=lambda x: x.tolist() if isinstance(x, np.ndarray) else x)

def compute_clustering_metrics(data, labels):
    metrics = {
        'silhouette': silhouette_score(data, labels)
    }
    return metrics

def kmeans_clustering(data, n_clusters, tol):
    kmeans = KMeans(n_clusters=n_clusters, tol=tol)
    kmeans.fit(data)
    return kmeans.labels_, kmeans.cluster_centers_

def dynamic_kmeans(data, k_values, q_values, epsilon_values, q_table):
    feedback_data = []
    total_combinations = len(k_values) * len(q_values) * len(epsilon_values)
    print(f"Total combinations to try: {total_combinations}")

    state = 'state1'  # For simplicity, we use a single state
    counts = np.zeros(len(k_values) * len(q_values) * len(epsilon_values))
    total_counts = 1

    for q in q_values:
        for epsilon in epsilon_values:
            for k in k_values:
                try:
                    action = epsilon_greedy(q_table, state, epsilon)
                    labels, cluster_centers = kmeans_clustering(data, k, epsilon)
                    metrics = compute_clustering_metrics(data, labels)
                    feedback_data.append((k, q, epsilon, metrics))
                    print(f"Calculated for k={k}, q={q}, epsilon={epsilon}: {metrics}")
                except Exception as e:
                    print(f"An error occurred for k={k}, q={q}, epsilon={epsilon}: {e}")
    return feedback_data

def main():
    # Load synthetic dataset for testing
    X, _ = make_blobs(n_samples=1000, centers=5, cluster_std=0.60, random_state=0)

    # Define Q-table
    q_table = pd.DataFrame(
        np.random.rand(13, 13),  # 13 states, 13 actions
        columns=[f'action{i}' for i in range(1, 14)],
        index=[f'state{i}' for i in range(1, 14)]
    )
    # Define epsilon values
    epsilon_values = [0.1, 0.01, 0.001, 0.0001]

    # Define K, Q, and epsilon ranges
    k_values = list(range(1, 21))
    q_values = [0.1, 0.01, 0.001, 0.0001]

    feedback_data = dynamic_kmeans(X, k_values, q_values, epsilon_values, q_table)

    # Save results to JSON
    results = {
        "feedback_data": feedback_data
    }

    os.makedirs('analysis/dynamic-k-means', exist_ok=True)
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f'analysis/dynamic-k-means/dynamic_k_means_results_{current_time}.json', 'w') as file:
        json.dump(results, file, indent=4)
    print(f"Results written to analysis/dynamic-k-means/dynamic_k_means_results_{current_time}.json for further analysis.")

    # Example metrics computation (dummy values for y_true, y_pred, y_proba)
    y_true = np.random.randint(0, 3, 100)
    y_pred = np.random.randint(0, 3, 100)
    y_proba = np.random.rand(100, 3)
    y_proba /= y_proba.sum(axis=1, keepdims=True)  # Normalize probabilities
    metrics = compute_metrics(y_true, y_pred, y_proba, [0.1] * 100)
    save_metrics_to_json(metrics, f'analysis/epsilon_greedy/epsilon_greedy_metrics_{current_time}.json')

    # Plot results
    def plot_results_2d(epsilon_values, actions, save_path):
        plt.figure()
        plt.plot(epsilon_values, actions, marker='o')
        plt.title('Hybrid Strategy Results (2D)')
        plt.xlabel('Epsilon Value')
        plt.ylabel('Selected Action')
        plt.grid(True)
        plt.savefig(save_path)
        plt.show()

    def plot_results_3d(epsilon_values, actions, save_path):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(epsilon_values, range(len(actions)), actions, c='r', marker='o')
        ax.set_title('Hybrid Strategy Results (3D)')
        ax.set_xlabel('Epsilon Values')
        ax.set_ylabel('Iteration')
        ax.set_zlabel('Selected Actions')
        plt.savefig(save_path)
        plt.show()

    # Assuming `actions` is a list of selected actions for plotting
    plot_results_2d(epsilon_values, [0] * len(epsilon_values), f'analysis/epsilon_greedy/charts/epsilon_greedy_2d_results_{current_time}.png')
    plot_results_3d(epsilon_values, [0] * len(epsilon_values), f'analysis/epsilon_greedy/charts/epsilon_greedy_3d_results_{current_time}.png')

if __name__ == "__main__":
    main()
