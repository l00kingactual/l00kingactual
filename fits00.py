# Here's an extended version of your code to handle multiple files per channel and to create previews.
# Note: I can't run this code here due to library restrictions, but you should be able to run it in your environment.

import numpy as np
from astropy.io import fits
from scipy.ndimage import shift
import matplotlib.pyplot as plt
from tkinter import filedialog

# Dictionary to store the data for each channel
channel_data = {
    'blue': [],
    'green': [],
    'red': [],
    'luminance': [],
    'Ha': [],
    'SII': [],
    'OIII': [],
    'JWST': {
        'NIRCam': {
            'Short_Wavelength': [],  # 0.6 to 2.3 micrometers
            'Long_Wavelength': []   # 2.4 to 5.0 micrometers
        },
        'NIRSpec': {
            'Spectral_Range': []  # 0.6 to 5.0 micrometers
        },
        'MIRI': {
            'Spectral_Range': []  # 5 to 28 micrometers
        },
        'FGS/NIRISS': {
            'Spectral_Range': []  # 0.8 to 5.0 micrometers
        }
    }
}

# Example of appending data to a specific instrument and frequency range
channel_data['JWST']['NIRCam']['Short_Wavelength'].append('your_data_here')

def open_fits_channel(channel):
    filepaths = filedialog.askopenfilenames(filetypes=[("FITS files", ("*.fit", "*.fits"))])
    if not filepaths:
        return

    for filepath in filepaths:
        data = fits.open(filepath)[0].data
        channel_data[channel].append(data)

def normalize_data(data):
    return ((data - np.min(data)) / (np.max(data) - np.min(data)) * 255).astype(np.uint8)

import cv2
import numpy as np

def align_and_stack_images(image_paths, channel):
    # Initialize an empty list to store the aligned images
    aligned_images = []
    
    # Read the first image from the list to serve as the reference image
    reference_image = cv2.imread(image_paths[0], cv2.IMREAD_GRAYSCALE)
    
    # Initialize the ORB detector for feature matching
    orb = cv2.ORB_create()
    
    # Detect keypoints and descriptors in the reference image
    kp1, des1 = orb.detectAndCompute(reference_image, None)
    
    # Initialize the BFMatcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
    for path in image_paths:
        # Read each image
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        
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
    channel_data[channel].append(stacked_image)

# Example usage
image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']
channel = 'NIRCam_Short_Wavelength'
align_and_stack_images(image_paths, channel)

def combine_channels(channels):
    # Assuming all channels have the same dimensions, you can sum the data arrays.
    combined_data = np.zeros_like(channel_data[channels[0]][0], dtype=np.float32)
    for channel in channels:
        for data in channel_data[channel]:
            combined_data += data
    return normalize_data(combined_data)

def preview_image(data, size=(250, 250)):
    plt.imshow(data, cmap='gray')
    plt.axis('off')
    plt.show()

def save_image(data, filename, size=(1920, 1080)):
    plt.imshow(data, cmap='gray')
    plt.axis('off')
    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close()

