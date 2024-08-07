import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Generate synthetic economic data
np.random.seed(42)
years = np.linspace(2000, 2020, 100)
gdp = 0.03 * years**3 - 1.5 * years**2 + 10 * years + np.random.randn(100) * 500

# Create a spline model
spline = make_interp_spline(years, gdp, k=3)  # k=3 for cubic spline

# Predict using the model
years_fit = np.linspace(2000, 2020, 300)
gdp_fit = spline(years_fit)

# Plot the results
plt.scatter(years, gdp, color='blue', label='Original Data')
plt.plot(years_fit, gdp_fit, color='red', label='Spline Approximation')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.title('Spline Approximation of GDP over Years')
plt.legend()
plt.show()
