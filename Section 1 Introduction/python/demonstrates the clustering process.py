import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Generate synthetic data (for example, we use 2D points for simplicity)
np.random.seed(42)
data = np.random.rand(100, 2) * 100  # 100 points in 2D

# Number of clusters
k = 3

# Apply K-Means clustering
kmeans = KMeans(n_clusters=k, random_state=0)
labels = kmeans.fit_predict(data)
centroids = kmeans.cluster_centers_

# Log the clustering process
logging.info(f"Data points clustered into {k} groups.")
logging.info(f"Cluster centroids: {centroids}")

# Plot the clusters
plt.figure(figsize=(8, 6))
colors = ['r', 'g', 'b', 'y', 'c', 'm']

for i in range(k):
    points = data[labels == i]
    plt.scatter(points[:, 0], points[:, 1], s=50, c=colors[i], label=f'Cluster {i+1}')
    plt.scatter(centroids[i, 0], centroids[i, 1], s=200, c='black', marker='x')  # Centroid

plt.title('K-Means Clustering')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
