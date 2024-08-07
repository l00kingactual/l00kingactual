from PIL import Image
import numpy as np

def grayscale_to_binary(image_path, threshold=128):
    """
    Function to convert a grayscale image to a binary (black and white) image.
    
    Parameters:
    image_path (str): Path to the input grayscale image.
    threshold (int): Threshold value to determine black or white (default is 128).
    
    Returns:
    np.array: Binary image represented as a numpy array.
    """
    # Load the image
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    image_array = np.array(image)
    
    # Apply threshold to convert to binary
    binary_image = (image_array > threshold) * 255
    return binary_image

# Example usage
binary_image = grayscale_to_binary('path_to_grayscale_image.png')
output_image = Image.fromarray(binary_image.astype(np.uint8))
output_image.save('path_to_output_binary_image.png')
