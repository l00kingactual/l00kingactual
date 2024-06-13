import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest

# Define the scales data
scales = [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Calculate basic statistics
mean = np.mean(scales)
median = np.median(scales)
mode = stats.mode(scales)
std_dev = np.std(scales)
variance = np.var(scales)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode[0][0]} (appears {mode[1][0]} times)")
print(f"Standard Deviation: {std_dev}")
print(f"Variance: {variance}")

# Data Visualization
plt.figure(figsize=(12, 6))

# Histogram
plt.subplot(1, 3, 1)
plt.hist(scales, bins=10, edgecolor='k', alpha=0.7)
plt.title("Histogram of Scales")
plt.xlabel("Scale")
plt.ylabel("Frequency")

# Box Plot
plt.subplot(1, 3, 2)
sns.boxplot(x=scales, orient='vertical')
plt.title("Box Plot of Scales")

# Density Plot
plt.subplot(1, 3, 3)
sns.kdeplot(scales, shade=True)
plt.title("Density Plot of Scales")

plt.tight_layout()
plt.show()

# Correlation Analysis
# If you have additional datasets, you can perform correlation analysis here.

# Feature Scaling
scaler = StandardScaler()
scaled_scales = scaler.fit_transform(np.array(scales).reshape(-1, 1))
# You can use scaled_scales for further analysis

# Dimensionality Reduction
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_scales)
# You can use principal_components for visualization

# Clustering
kmeans = KMeans(n_clusters=3)
cluster_labels = kmeans.fit_predict(np.array(scales).reshape(-1, 1))
# You can use cluster_labels for grouping

# Regression Analysis
# Assuming you have a target variable y, perform regression analysis here.

# Time Series Analysis
# If the scales represent time series data, use time series analysis techniques here.

# Feature Selection (FS)
# You can perform feature selection using RFE or other methods here.

# Machine Learning Models
# You can build and evaluate machine learning models here.

# Anomaly Detection
# Utilize anomaly detection algorithms like Isolation Forest or One-Class SVM here.
