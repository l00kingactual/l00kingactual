import numpy as np
import matplotlib.pyplot as plt

# Original 1D array
scales = [  
    0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 15, 16, 19, 22, 24, 25,
    28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64,
    94, 128, 171, 196, 206, 345, 360, 512, 720, 845, 1080, 4096, 4394, 5239, 5261
]

# Determine the length of the array for padding
length = len(scales)

# Find the next perfect square greater than length for 2D reshaping, and a cube for 3D
next_square = np.ceil(np.sqrt(length))**2
next_cube = np.ceil(length ** (1/3))**3

# Pad scales to match the next perfect square and cube sizes
padded_scales_2d = np.pad(scales, (0, int(next_square - length)), constant_values=-1)
padded_scales_3d = np.pad(scales, (0, int(next_cube - length)), constant_values=-1)

# Reshape to 2D array
scales_2d = padded_scales_2d.reshape(int(np.sqrt(next_square)), int(np.sqrt(next_square)))

# Reshape to 3D array
scales_3d = padded_scales_3d.reshape(int(np.cbrt(next_cube)), int(np.cbrt(next_cube)), int(np.cbrt(next_cube)))

print("2D Array:")
print(scales_2d)
print("\n3D Array:")
print(scales_3d)

# Plotting
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot the original 1D array
axs[0].plot(scales, 'o-')
axs[0].set_title('Original 1D Array')
axs[0].set_xlabel('Index')
axs[0].set_ylabel('Value')

# Plot the 2D array as a heatmap
c = axs[1].matshow(scales_2d, cmap='viridis')
fig.colorbar(c, ax=axs[1])
axs[1].set_title('2D Array Heatmap')

# Plot the first layer of the 3D array as a heatmap
c = axs[2].matshow(scales_3d[0], cmap='viridis')
fig.colorbar(c, ax=axs[2])
axs[2].set_title('3D Array First Layer Heatmap')

plt.tight_layout()
plt.show()