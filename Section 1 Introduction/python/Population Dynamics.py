import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Parameters
r = np.linspace(2.5, 4.0, 100)
x = np.linspace(0, 1, 100)

R, X = np.meshgrid(r, x)
Z = logistic_map(R, X)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(R, X, Z, cmap='viridis')

ax.set_title('3D Population Dynamics (Logistic Map)')
ax.set_xlabel('Growth rate (r)')
ax.set_ylabel('Population (x)')
ax.set_zlabel('Next Population')
plt.show()
