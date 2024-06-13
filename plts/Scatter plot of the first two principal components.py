import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load dataset
data = load_iris()
X = data.data
y = data.target

# PCA transformation
pca = PCA(n_components=2)
X_r = pca.fit_transform(X)

# Scatter plot of the first two principal components
plt.figure()
for color, i, target_name in zip(['red', 'green', 'blue'], [0, 1, 2], data.target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=2, label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA of IRIS dataset')
plt.show()
