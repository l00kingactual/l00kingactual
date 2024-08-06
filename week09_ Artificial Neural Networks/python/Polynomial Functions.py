import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + 1.5 * X**2 + np.random.randn(100, 1)

# Polynomial regression model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)

# Plot
plt.scatter(X, y, label='Data points')
X_fit = np.linspace(0, 2, 100).reshape(100, 1)
X_fit_poly = poly_features.transform(X_fit)
y_fit = lin_reg.predict(X_fit_poly)
plt.plot(X_fit, y_fit, color='red', label='Polynomial fit')
plt.legend()
plt.show()
