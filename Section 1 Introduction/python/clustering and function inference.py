import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Generate synthetic data
np.random.seed(42)
x1 = np.random.rand(50, 1) * 10
y1 = 2 * x1 + 1 + np.random.randn(50, 1)

x2 = np.random.rand(50, 1) * 10
y2 = -3 * x2 + 10 + np.random.randn(50, 1)

x3 = np.random.rand(50, 1) * 10
y3 = 0.5 * x3 ** 2 - 2 * x3 + 5 + np.random.randn(50, 1)

X = np.vstack((x1, x2, x3))
y = np.vstack((y1, y2, y3))

data = np.hstack((X, y))

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
plt.figure(figsize=(10, 8))
colors = ['r', 'g', 'b', 'y', 'c', 'm']

for i in range(k):
    points = data[labels == i]
    plt.scatter(points[:, 0], points[:, 1], s=50, c=colors[i], label=f'Cluster {i+1}')
    plt.scatter(centroids[i, 0], centroids[i, 1], s=200, c='black', marker='x')  # Centroid
    
    # Fit a function to each cluster
    if i == 2:  # Polynomial regression for the third cluster
        poly_features = np.polyfit(points[:, 0], points[:, 1], 2)
        poly = np.poly1d(poly_features)
        x_poly = np.linspace(min(points[:, 0]), max(points[:, 0]), 100)
        plt.plot(x_poly, poly(x_poly), color=colors[i])
    else:  # Linear regression for the other clusters
        lin_reg = LinearRegression()
        lin_reg.fit(points[:, 0].reshape(-1, 1), points[:, 1])
        x_lin = np.linspace(min(points[:, 0]), max(points[:, 0]), 100)
        y_lin = lin_reg.predict(x_lin.reshape(-1, 1))
        plt.plot(x_lin, y_lin, color=colors[i])

plt.title('K-Means Clustering and Function Inference')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
