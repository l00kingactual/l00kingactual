import numpy as np
import matplotlib.pyplot as plt

# Grid generation
x, y, z = np.meshgrid(np.linspace(-1, 1, 10), 
                      np.linspace(-1, 1, 10), 
                      np.linspace(-1, 1, 10))

# Vector field (simple example)
u = -y
v = x
w = np.zeros_like(x)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True, color='blue')

ax.set_title('3D Ocean Currents and Tides')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
plt.show()
