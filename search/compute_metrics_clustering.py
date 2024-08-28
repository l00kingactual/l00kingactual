import os
import json
import numpy as np
from datetime import datetime
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
from sklearn.metrics import silhouette_score
from compute_metrics import compute_metrics, save_metrics_to_json

def save_metrics_with_timestamp(metrics, directory, prefix):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'{prefix}_{current_time}.json'
    save_path = os.path.join(directory, filename)
    save_metrics_to_json(metrics, save_path)

def read_all_metrics_files(directory):
    metrics_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    metrics_list.append(json.load(f))
    return metrics_list

def prepare_data_for_clustering(metrics_list):
    required_keys = ['accuracy', 'precision', 'recall', 'f1', 'logloss', 'mse', 'mae', 'mcc', 'kappa', 'balanced_acc', 'jaccard', 'r2']
    data = []
    for metrics in metrics_list:
        row = []
        for key in required_keys:
            row.append(metrics.get(key, 0))  # Use 0 as default if key is missing
        data.append(row)
    data = np.array(data)
    # Handle NaN values
    imputer = SimpleImputer(strategy='mean')
    data = imputer.fit_transform(data)
    return data

def perform_clustering(data, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
    return kmeans.cluster_centers_, kmeans.labels_

def main():
    results_directory = 'analysis'
    analysis_directory = 'analysis/compute_metrics_clustering'

    # Step 1: Read all metrics files
    metrics_list = read_all_metrics_files(results_directory)
    if not metrics_list:
        print("No metrics files found.")
        return

    # Step 2: Prepare data for clustering
    data = prepare_data_for_clustering(metrics_list)
    if data.size == 0:
        print("No data available for clustering.")
        return

    # Step 3: Perform clustering
    cluster_centers, labels = perform_clustering(data)

    # Step 4: Compute enhanced metrics for each cluster
    enhanced_metrics = []
    for i, center in enumerate(cluster_centers):
        cluster_data = data[labels == i]
        y_true = cluster_data[:, 0]  # Assuming the first column is y_true
        y_pred = cluster_data[:, 1]  # Assuming the second column is y_pred
        y_proba = cluster_data[:, 2:]  # Assuming the rest are probabilities
        epoch_times = [0.1] * len(y_true)  # Example epoch times
        metrics = compute_metrics(y_true, y_pred, y_proba, epoch_times)
        enhanced_metrics.append(metrics)
        save_metrics_with_timestamp(metrics, analysis_directory, f'enhanced_metrics_cluster_{i}')

    print("Enhanced metrics computed and saved.")

if __name__ == "__main__":
    main()
