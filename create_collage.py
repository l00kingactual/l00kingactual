from PIL import Image
import numpy as np
import os

def create_collage(image_dir, output_path, collage_size):
    # Get list of image files in the directory
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.png')]
    
    # Open all images and resize them to fit into the collage
    images = []
    for file in image_files:
        image = Image.open(os.path.join(image_dir, file))
        image = image.resize(collage_size, Image.ANTIALIAS)  # Resize image to fit into collage
        images.append(image)
    
    # Calculate the dimensions of the collage
    cols = int(np.ceil(np.sqrt(len(images))))
    rows = int(np.ceil(len(images) / cols))
    
    # Create a blank canvas for the collage
    collage = Image.new('RGB', (cols * collage_size[0], rows * collage_size[1]))
    
    # Paste each image onto the collage
    for i, img in enumerate(images):
        x = (i % cols) * collage_size[0]
        y = (i // cols) * collage_size[1]
        collage.paste(img, (x, y))
    
    # Save the collage
    collage.save(output_path)

# Example usage
image_dir = 'path/to/your/images'
output_path = 'path/to/save/collage.jpg'
collage_size = (200, 200)  # Size of each image in the collage
create_collage(image_dir, output_path, collage_size)
