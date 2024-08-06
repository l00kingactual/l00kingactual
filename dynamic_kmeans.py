import os
import json
import numpy as np
from datetime import datetime
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from compute_metrics_clustering import perform_clustering, prepare_data_for_clustering, read_all_metrics_files
from skopt import BayesSearchCV
from skopt.space import Real, Integer
from sklearn.model_selection import RandomizedSearchCV

def load_previous_results(directory):
    results = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as file:
                try:
                    data = json.load(file)
                    if 'feedback_data' in data:
                        results.extend(data['feedback_data'])
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from {filename}, skipping this file.")
    return results

def extract_best_combination(data, previous_results):
    best_combination = None
    best_score = float('-inf')
    
    for result in previous_results:
        try:
            k, q, epsilon, metrics = result
            if metrics['silhouette'] is not None and metrics['silhouette'] > best_score:
                best_score = metrics['silhouette']
                best_combination = (k, q, epsilon)
        except ValueError:
            print(f"Skipping invalid result: {result}")
    
    return best_combination

def kmeans_clustering(data, n_clusters, tol):
    kmeans = KMeans(n_clusters=n_clusters, tol=tol)
    kmeans.fit(data)
    return kmeans.labels_, kmeans.cluster_centers_

def dynamic_kmeans(data, k_values, q_values, epsilon_values):
    feedback_data = []
    total_combinations = len(k_values) * len(q_values) * len(epsilon_values)
    print(f"Total combinations to try: {total_combinations}")

    for q in q_values:
        for epsilon in epsilon_values:
            for k in k_values:
                try:
                    labels, cluster_centers = kmeans_clustering(data, k, epsilon)
                    metrics = perform_clustering(data, labels)
                    feedback_data.append((k, q, epsilon, metrics))
                    print(f"Calculated for k={k}, q={q}, epsilon={epsilon}: {metrics}")
                except Exception as e:
                    print(f"An error occurred for k={k}, q={q}, epsilon={epsilon}: {e}")
    return feedback_data

def main():
    from sklearn.datasets import make_blobs

    # Load synthetic dataset for testing
    X, _ = make_blobs(n_samples=1000, centers=5, cluster_std=0.60, random_state=0)

    # Load previous results
    previous_results = load_previous_results('analysis/k-means') + load_previous_results('analysis/dynamic-k-means')
    best_combination = extract_best_combination(X, previous_results)

    if best_combination:
        k, q, epsilon = best_combination
    else:
        k, q, epsilon = 10, 0.1, 0.0001  # Default values

    k_values = list(range(1, 21))  # Example k value range
    q_values = [0.1, 0.01, 0.001, 0.0001]
    epsilon_values = [0.1, 0.01, 0.001, 0.0001]

    feedback_data = dynamic_kmeans(X, k_values, q_values, epsilon_values)

    # Save results to JSON
    results = {
        "best_combination": {"k": k, "q": q, "epsilon": epsilon},
        "feedback_data": previous_results + feedback_data
    }

    os.makedirs('analysis/dynamic-k-means', exist_ok=True)
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f'analysis/dynamic-k-means/dynamic_k_means_results_{current_time}.json', 'w') as file:
        json.dump(results, file, indent=4)
    print(f"Results written to analysis/dynamic-k-means/dynamic_k_means_results_{current_time}.json for further analysis.")

if __name__ == "__main__":
    main()
