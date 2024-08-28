import tensorflow as tf
import numpy as np
import pandas as pd
import time
import os
import json
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from compute_metrics_clustering import save_metrics_with_timestamp, prepare_data_for_clustering
from compute_metrics import compute_metrics, save_metrics_to_json
from data_return_real_data_df import combined_df as real_data
from data_return_df import combined_df as synthetic_data
from enhanced_nn import build_enhanced_nn

# Combine real and synthetic data
combined_df = pd.concat([real_data, synthetic_data], ignore_index=True)

from k_value_space import k_value_space
from q_value_space import q_value_space
from epsilon_value_space import epsilon_value_space
from epsilon_greedy_vaule_space import epsilon_greedy_space
from quantum.quantum_layer import QuantumCircuitLayer

# Function to calculate statistics for a value space
def calculate_statistics(values):
    return {
        "min": np.min(values),
        "max": np.max(values),
        "mean": np.mean(values),
        "stddev": np.std(values)
    }

# Calculate statistics for each value space
k_stats = calculate_statistics(k_value_space)
q_stats = calculate_statistics(q_value_space)
epsilon_stats = calculate_statistics(epsilon_value_space)
epsilon_greedy_stats = calculate_statistics(epsilon_greedy_space)

# Optional: Further abstract these statistics into a higher-level representation
abstracted_space_stats = {
    "mean": np.mean([k_stats["mean"], q_stats["mean"], epsilon_stats["mean"], epsilon_greedy_stats["mean"]]),
    "stddev": np.mean([k_stats["stddev"], q_stats["stddev"], epsilon_stats["stddev"], epsilon_greedy_stats["stddev"]]),
    "max": np.mean([k_stats["max"], q_stats["max"], epsilon_stats["max"], epsilon_greedy_stats["max"]])
}

# Data and Model Preparation
x_train = np.random.rand(250, 25)
y_train = np.random.randint(0, 3, 250)
x_test = np.random.rand(25, 25)
y_test = np.random.randint(0, 3, 25)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

total_samples = len(x_train) + len(x_test)
k_values = np.array(k_value_space)[:total_samples]
q_values = np.array(q_value_space)[:total_samples]
epsilon_values = np.array(epsilon_value_space)[:total_samples]

if len(k_values) < total_samples:
    k_values = np.pad(k_values, (0, total_samples - len(k_values)), 'constant')
if len(q_values) < total_samples:
    q_values = np.pad(q_values, (0, total_samples - len(q_values)), 'constant')
if len(epsilon_values) < total_samples:
    epsilon_values = np.pad(epsilon_values, (0, total_samples - len(epsilon_values)), 'constant')

# Combine input features with value spaces, now abstracted
x_train_combined = np.hstack((
    x_train, 
    k_values[:len(x_train)].reshape(-1, 1), 
    q_values[:len(x_train)].reshape(-1, 1), 
    epsilon_values[:len(x_train)].reshape(-1, 1)
))

x_test_combined = np.hstack((
    x_test, 
    k_values[len(x_train):].reshape(-1, 1), 
    q_values[len(x_train):].reshape(-1, 1), 
    epsilon_values[len(x_train):].reshape(-1, 1)
))

input_shape = (x_train_combined.shape[1],)
num_classes = len(np.unique(y_train))


def train_neural_network(model, x_train, y_train, x_val, y_val, epochs=50, batch_size=32):
    epoch_times = []
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    lr_scheduler = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6)
    for epoch in range(epochs):
        start_time = time.time()
        model.fit(x_train, y_train, epochs=1, batch_size=batch_size, validation_data=(x_val, y_val), callbacks=[early_stopping, lr_scheduler])
        epoch_time = time.time() - start_time
        epoch_times.append(epoch_time)
    return model, epoch_times

def metrics(metrics):
    inverted_metrics = {}
    for key, value in metrics.items():
        if isinstance(value, (int, float)):
            # Invert metric if it's a performance metric like accuracy, precision, etc.
            if key in ['accuracy', 'precision', 'recall', 'f1', 'balanced_acc', 'jaccard']:
                inverted_metrics[key] = 1 - value
            else:
                inverted_metrics[key] = value
        elif isinstance(value, list):
            inverted_metrics[key] = [1 - v if isinstance(v, (int, float)) and key in ['accuracy', 'precision', 'recall', 'f1', 'balanced_acc', 'jaccard'] else v for v in value]
        else:
            inverted_metrics[key] = value
    return inverted_metrics

model, epoch_times = train_neural_network(model, x_train_combined, y_train, x_test_combined, y_test, epochs=10)

y_pred = model.predict(x_test_combined).argmax(axis=1)
y_proba = model.predict(x_test_combined)

# Compute the metrics and then invert them
metrics = compute_metrics(y_test, y_pred, y_proba, epoch_times, k_values[len(x_train):], q_values[len(x_train):], epsilon_values[len(x_train):])
inverted_metrics = metrics(metrics)
save_metrics_to_json(inverted_metrics, 'analysis/clustering/inverted_metrics')

# Clustering on Collected Metrics
data = prepare_data_for_clustering([inverted_metrics])

# Ensure data has more than one sample for clustering
if data.shape[0] > 2:  # Ensure at least 3 samples for 3 clusters
    # Apply K-Means Clustering
    kmeans = KMeans(n_clusters=3, random_state=0)
    labels_kmeans = kmeans.fit_predict(data)
    silhouette_kmeans = silhouette_score(data, labels_kmeans)
    save_metrics_with_timestamp({"clustering_method": "KMeans", "silhouette_score": silhouette_kmeans}, 'analysis/clustering', 'kmeans_metrics')

    # Apply DBSCAN Clustering
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    labels_dbscan = dbscan.fit_predict(data)
    silhouette_dbscan = silhouette_score(data, labels_dbscan) if len(set(labels_dbscan)) > 1 else -1
    save_metrics_with_timestamp({"clustering_method": "DBSCAN", "silhouette_score": silhouette_dbscan}, 'analysis/clustering', 'dbscan_metrics')

    # Apply Gaussian Mixture Model Clustering
    gmm = GaussianMixture(n_components=3, random_state=0)
    labels_gmm = gmm.fit_predict(data)
    silhouette_gmm = silhouette_score(data, labels_gmm)
    save_metrics_with_timestamp({"clustering_method": "GMM", "silhouette_score": silhouette_gmm}, 'analysis/clustering', 'gmm_metrics')
else:
    print("Not enough samples for clustering. Skipping clustering step.")

print("Clustering analysis completed and saved.")
