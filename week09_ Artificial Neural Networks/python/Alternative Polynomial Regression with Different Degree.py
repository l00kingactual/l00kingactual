import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# Generate synthetic economic data
np.random.seed(42)
years = np.linspace(2000, 2020, 100)
gdp = 0.03 * years**3 - 1.5 * years**2 + 10 * years + np.random.randn(100) * 500

# Try a higher degree polynomial regression model
degree = 10
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model.fit(years[:, np.newaxis], gdp)

# Predict using the model
years_fit = np.linspace(2000, 2020, 100)
gdp_fit = model.predict(years_fit[:, np.newaxis])

# Plot the results
plt.scatter(years, gdp, color='blue', label='Original Data')
plt.plot(years_fit, gdp_fit, color='red', label=f'Polynomial Approximation (degree {degree})')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.title('Polynomial Approximation of GDP over Years')
plt.legend()
plt.show()
