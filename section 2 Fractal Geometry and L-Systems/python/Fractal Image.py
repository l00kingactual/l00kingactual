import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize

# Function to apply affine transformations iteratively
def apply_transformations(image, transforms, iterations):
    images = []
    for i in range(1, iterations + 1):
        idx = np.random.choice(len(transforms), p=[t["probability"] for t in transforms])
        matrix = transforms[idx]["matrix"]
        translation = transforms[idx]["translation"]
        # Reshape the image vector to a 2D array before matrix multiplication
        image = np.dot(matrix, image.reshape(2, -1)) + translation.reshape(2, 1)
        images.append(image)
    return images

# Function to reproduce image at a higher resolution
def reproduce_image(image, transforms, target_resolution, iterations, snapshot_iterations):
    # Upscale the random image to target resolution
    upscale_factor = target_resolution / image.shape[0]
    image = resize(image, (target_resolution, target_resolution), anti_aliasing=True)
    
    # Apply affine transformations iteratively
    fractal_images = apply_transformations(image.flatten(), transforms, iterations)
    
    # Reshape the flattened images to 2D arrays
    fractal_images = [img.reshape(target_resolution, target_resolution) for img in fractal_images]
    
    # Select snapshots of iterations for plotting
    snapshot_indices = np.linspace(0, iterations-1, num=snapshot_iterations, dtype=int)
    snapshot_images = [fractal_images[i] for i in snapshot_indices]
    
    return snapshot_images

# Define parameters
random_image_size = 100
target_resolution = 1000
iterations = 10000
snapshot_iterations = 6

# Generate a random image
random_image = np.random.rand(random_image_size, random_image_size)

# Define affine transformations (example transformations)
transforms = [
    {"matrix": np.array([[0.85, 0.04], [-0.04, 0.85]]), "translation": np.array([0, 1.6]), "probability": 0.85},
    {"matrix": np.array([[0.2, -0.26], [0.23, 0.22]]), "translation": np.array([0, 1.6]), "probability": 0.07},
    {"matrix": np.array([[-0.15, 0.28], [0.26, 0.24]]), "translation": np.array([0, 0.44]), "probability": 0.07}
]

# Ensure probabilities sum up to 1
total_prob = sum(t["probability"] for t in transforms)
for t in transforms:
    t["probability"] /= total_prob

# Reproduce image at higher resolution with snapshots of iterations
fractal_images = reproduce_image(random_image, transforms, target_resolution, iterations, snapshot_iterations)

# Plotting snapshots of iterations
plt.figure(figsize=(18, 3))
for i in range(snapshot_iterations):
    plt.subplot(1, snapshot_iterations, i + 1)
    plt.imshow(fractal_images[i], cmap='gray')
    plt.title(f"Iteration {int(iterations * (i+1) / snapshot_iterations)}")
    plt.axis('off')
plt.show()
