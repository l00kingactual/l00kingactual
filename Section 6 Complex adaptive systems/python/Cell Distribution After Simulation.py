import numpy as np
import matplotlib.pyplot as plt

# Parameters
size = 100  # Grid size
time_steps = 100  # Number of time steps
D_n = 0.1  # Diffusion rate of cells
D_c = 0.1  # Diffusion rate of chemoattractant
chi = 1.0  # Chemotactic sensitivity
alpha = 0.01  # Production rate of chemoattractant
beta = 0.05  # Decay rate of chemoattractant

# Initialize cell and chemoattractant concentrations
cells = np.zeros((size, size))
chemoattractant = np.zeros((size, size))

# Random initial distribution of cells
np.random.seed(42)
cells[np.random.randint(0, size, 50), np.random.randint(0, size, 50)] = 1

# Function to update cell and chemoattractant concentrations
def update(cells, chemoattractant, D_n, D_c, chi, alpha, beta):
    # Diffusion of chemoattractant
    laplacian_c = (
        np.roll(chemoattractant, 1, axis=0) + np.roll(chemoattractant, -1, axis=0) +
        np.roll(chemoattractant, 1, axis=1) + np.roll(chemoattractant, -1, axis=1) - 4 * chemoattractant
    )
    chemoattractant += D_c * laplacian_c

    # Production and decay of chemoattractant
    chemoattractant += alpha * cells
    chemoattractant -= beta * chemoattractant

    # Chemotaxis and diffusion of cells
    grad_x, grad_y = np.gradient(chemoattractant)
    movement_x = -chi * grad_x
    movement_y = -chi * grad_y

    new_cells = np.zeros_like(cells)
    for x in range(size):
        for y in range(size):
            if cells[x, y] > 0:
                new_x = (x + int(movement_x[x, y])) % size
                new_y = (y + int(movement_y[x, y])) % size
                new_cells[new_x, new_y] = 1

    return new_cells, chemoattractant

# Simulation loop
for t in range(time_steps):
    cells, chemoattractant = update(cells, chemoattractant, D_n, D_c, chi, alpha, beta)

# Visualization
plt.imshow(cells, cmap='Greens')
plt.title('Cell Distribution After Simulation')
plt.show()
