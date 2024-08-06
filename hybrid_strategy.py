import numpy as np
import matplotlib.pyplot as plt
import os
import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Define all strategies
def epsilon_greedy(q_table, state, epsilon=0.1):
    if np.random.rand() < epsilon:
        action = np.random.choice(q_table.shape[1])
    else:
        action = np.argmax(q_table[state])
    return action

def ucb1(q_table, state, counts, total_counts):
    ucb_values = q_table[state] + np.sqrt(2 * np.log(total_counts) / (counts + 1))
    return np.argmax(ucb_values)

def thompson_sampling(q_table, state):
    sampled_values = np.random.beta(q_table[state] + 1, 1)
    return np.argmax(sampled_values)

def softmax(q_table, state, tau=1.0):
    exp_values = np.exp(q_table[state] / tau)
    probabilities = exp_values / np.sum(exp_values)
    return np.random.choice(len(probabilities), p=probabilities)

def bayesian_ucb(q_table, state, total_counts, alpha=1.0):
    sampled_values = q_table[state] + alpha * np.sqrt(np.log(total_counts + 1) / (total_counts + 1))
    return np.argmax(sampled_values)

def exp3(q_table, state, gamma=0.1):
    exp_values = np.exp(gamma * q_table[state])
    probabilities = exp_values / np.sum(exp_values)
    return np.random.choice(len(probabilities), p=probabilities)

def greedy(q_table, state):
    return np.argmax(q_table[state])

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
    elif strategy == 'bayesian_ucb':
        return bayesian_ucb(q_table, state, total_counts)
    elif strategy == 'exp3':
        return exp3(q_table, state)
    elif strategy == 'greedy':
        return greedy(q_table, state)
    elif strategy == 'random_selection':
        return random_selection(q_table, state)

# Compute metrics
def compute_metrics(y_true, y_pred, y_proba):
    y_proba_normalized = y_proba / y_proba.sum(axis=1, keepdims=True)
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, average='weighted'),
        "recall": recall_score(y_true, y_pred, average='weighted'),
        "f1_score": f1_score(y_true, y_pred, average='weighted'),
        "auc": roc_auc_score(y_true, y_proba_normalized, multi_class='ovr')
    }

# Save metrics to JSON
def save_metrics_to_json(metrics, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(metrics, f, indent=4)

# Plot results in 2D
def plot_results_2d(epsilon_values, actions, save_path):
    plt.figure()
    plt.plot(epsilon_values, actions, marker='o')
    plt.title('Epsilon-Greedy Results')
    plt.xlabel('Epsilon Value')
    plt.ylabel('Selected Action')
    plt.grid(True)
    plt.savefig(save_path)
    plt.show()

# Plot results in 3D
def plot_results_3d(epsilon_values, actions, save_path):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(epsilon_values, actions, c='r', marker='o')
    ax.set_title('3D Scatter plot with Predicted Clusters')
    ax.set_xlabel('Epsilon Values')
    ax.set_ylabel('Selected Actions')
    ax.set_zlabel('Probabilities')
    plt.savefig(save_path)
    plt.show()

# Main Function
if __name__ == "__main__":
    # Example Q-table and state initialization
    q_table = np.random.rand(10, 3)  # 10 states, 3 actions
    state = 0  # initial state
    counts = np.zeros(3)  # count of actions taken
    total_counts = 1
    # New list of epsilon values to test, including mathematical and physical constants
    epsilon_values = [
        0.1,  # A commonly used value
        0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001,
        np.pi / 10, np.pi / 100, np.pi / 1000,  # Values based on pi
        (np.pi**2) / 10, (np.pi**2) / 100, (np.pi**2) / 1000,  # Pi squared
        (np.pi**3) / 10, (np.pi**3) / 100, (np.pi**3) / 1000,  # Pi cubed
        299792458 / 10**9, 299792458 / 10**10, 299792458 / 10**11  # Speed of light in m/s in various scales
    ]

    strategies = ['epsilon_greedy', 'ucb1', 'thompson_sampling', 'softmax', 'bayesian_ucb', 'exp3', 'greedy', 'random_selection']
    results = {}

    for strategy in strategies:
        actions = []
        for epsilon in epsilon_values:
            action = hybrid_strategy(q_table, state, counts, total_counts, epsilon, strategy)
            actions.append(action)
            counts[action] += 1
            total_counts += 1
        results[strategy] = {str(epsilon): f'action{action}' for epsilon, action in zip(epsilon_values, actions)}

    # Save results
    from datetime import datetime

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    save_metrics_to_json(results, 'analysis/hybrid_strategy/hybrid_strategy_{current_time}.json')

    # Plot results
    plot_results_2d(epsilon_values, actions, 'analysis/hybrid_strategy/charts/hybrid_stragy_2d_results_{current_time}.png')
    plot_results_3d(epsilon_values, actions, 'analysis/hybrid_strategy/charts/hybrid_stragy_3d_results_{current_time}.png')

    # Example metrics computation (dummy values for y_true, y_pred, y_proba)
    y_true = np.random.randint(0, 3, 100)
    y_pred = np.random.randint(0, 3, 100)
    y_proba = np.random.rand(100, 3)
    metrics = compute_metrics(y_true, y_pred, y_proba)
    save_metrics_to_json(metrics, 'analysis/epsilon_greedy/epsilon_greedy_metrics_current_time.json')
