import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Generate synthetic data (features of images)
def generate_synthetic_data(n_samples, n_features):
    np.random.seed(0)
    data = np.random.rand(n_samples, n_features)
    return data

# Apply K-means clustering
def kmeans_clustering(data, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(data)
    return kmeans

# Generate synthetic data
n_samples = 300
n_features = 2  # For simplicity, use 2 features to allow 2D visualization
data = generate_synthetic_data(n_samples, n_features)

# Apply K-means clustering
n_clusters = 3
kmeans = kmeans_clustering(data, n_clusters)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Visualize the clusters
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', marker='o', alpha=0.5)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
plt.title("K-means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Log information about the clustering
logging.info(f"Cluster Centers: {centers}")
for i in range(n_clusters):
    logging.info(f"Cluster {i}: {np.sum(labels == i)} points")
