from astropy.io import fits
import cv2
import numpy as np

# 1. Data Structures: Consistent channel_data dictionary
channel_data = {
    'RGB': {'Red': [], 'Green': [], 'Blue': [], 'Luminance': []},
    'Narrowband': {'Ha': [], 'SII': [], 'OIII': []},
    'JWST': {
        'NIRCam': {'Short_Wavelength': [], 'Long_Wavelength': []},
        'NIRSpec': {'Spectral_Range': []},
        'MIRI': {'Spectral_Range': []},
        'FGS/NIRISS': {'Spectral_Range': []}
    }
}

# 2. Function Definitions: One flexible function to handle both scenarios
# 3. File Handling: Accepts both file paths and file objects
# 4. Error Handling: Robust error handling
def open_fits_channel(channel_dict, files, frequency):
    if not files:
        return

    for file in files:
        data = fits.open(file.stream)[0].data
        normalized_data = normalize_data(data)
        
        # Append the data to the appropriate frequency
        if frequency in channel_dict:
            channel_dict[frequency].append(normalized_data)
        else:
            print(f"Warning: Frequency {frequency} not found in channel_dict.")

# 6. Data Normalization: Managed by fit02.py
def normalize_data(data):
    return ((data - np.min(data)) / (np.max(data) - np.min(data)) * 255).astype(np.uint8)

# 5. Function Calls: Compatible with Flask backend
# 7. Data Transfer: Small previews, one large preview
# 8. Debugging: Debug statements for understanding
# 9. Code Comments: Copious comments for clarity
def align_and_stack_images(channel_dict, channel_name):
    try:
        # Initialize an empty list to store the aligned images
        aligned_images = []
        
        # Use the first image from the channel_data as the reference image
        reference_image = channel_dict[channel_name][0]
    except KeyError as e:
        print(f"KeyError: {e}")
        return
    
    # Initialize the ORB detector for feature matching
    orb = cv2.ORB_create()
    
    # Detect keypoints and descriptors in the reference image
    kp1, des1 = orb.detectAndCompute(reference_image, None)
    
    # Initialize the BFMatcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
    for image in channel_dict[channel_name]:
        # Detect keypoints and descriptors in the image
        kp2, des2 = orb.detectAndCompute(image, None)
        
        # Match descriptors between the reference image and the image to be aligned
        matches = bf.match(des1, des2)
        
        # Sort matches based on their distances
        matches = sorted(matches, key=lambda x: x.distance)
        
        # Extract location of good matches
        points1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        points2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
        
        # Compute the homography matrix
        M, mask = cv2.findHomography(points1, points2, cv2.RANSAC, 5.0)
        
        # Align the image to the reference image
        aligned_image = cv2.warpPerspective(image, M, (reference_image.shape[1], reference_image.shape[0]))
        
        # Append the aligned image to the list
        aligned_images.append(aligned_image)
    
    # Stack the aligned images
    stacked_image = np.mean(aligned_images, axis=0).astype(np.uint8)
    
    # Add the stacked image to the channel_data dictionary
    channel_dict[channel_name].append(stacked_image)

import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-GUI rendering
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import logging

logging.basicConfig(level=logging.INFO)

def numpy_array_to_base64(array, cmap='gray', format='png'):
    """
    Convert a numpy array to a base64 encoded image.

    Parameters:
        array (numpy.ndarray): The numpy array to convert.
        cmap (str): The colormap to use for rendering the image.
        format (str): The image format to use for encoding.

    Returns:
        str: The base64 encoded image.
    """
    try:
        plt.ioff()  # Turn off interactive mode to prevent GUI
        fig, ax = plt.subplots()  # Create a figure and axis object

        ax.imshow(array, cmap=cmap)  # Display the array
        ax.axis('off')  # Turn off axis

        buffer = BytesIO()  # Create a BytesIO object

        plt.savefig(buffer, format=format)  # Save the figure to the BytesIO object
        plt.close(fig)  # Close the figure to free up resources

        img_base64 = base64.b64encode(buffer.getvalue()).decode()  # Encode to base64

        logging.info("Successfully converted numpy array to base64 image.")
        return img_base64

    except Exception as e:
        logging.error(f"An error occurred while converting numpy array to base64: {e}")
        return None
