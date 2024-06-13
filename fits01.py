from astropy.io import fits
from tkinter import filedialog
import cv2
import numpy as np

# Dictionary to store the data for each channel
channel_data = {
    'RGB': {'R': [], 'G': [], 'B': [], 'L': []},
    'Narrowband': {'Ha': [], 'SII': [], 'OIII': []},
    'JWST': {
        'NIRCam': {'Short_Wavelength': [], 'Long_Wavelength': []},
        'NIRSpec': {'Spectral_Range': []},
        'MIRI': {'Spectral_Range': []},
        'FGS/NIRISS': {'Spectral_Range': []}
    }
}

def open_fits_channel(channel_dict):
    filepaths = filedialog.askopenfilenames(filetypes=[("FITS files", ("*.fit", "*.fits"))])
    if not filepaths:
        return

    for filepath in filepaths:
        data = fits.open(filepath)[0].data
        normalized_data = normalize_data(data)
        
        # Determine which channel to append the data to
        for main_channel, sub_channels in channel_dict.items():
            if isinstance(sub_channels, dict):
                for sub_channel in sub_channels:
                    channel_dict[main_channel][sub_channel].append(normalized_data)
            else:
                channel_dict[main_channel].append(normalized_data)

def normalize_data(data):
    return ((data - np.min(data)) / (np.max(data) - np.min(data)) * 255).astype(np.uint8)

# ... (align_and_stack_images function remains the same)

# Example usage
#open_fits_channel(channel_data['RGB'])  # For RGB+L
#(channel_data['Narrowband'])  # For Ha, SII, OIII
#open_fits_channel(channel_data['JWST'])  # For JWST instrument channels

def align_and_stack_images(channel_dict, channel_name):
    # Initialize an empty list to store the aligned images
    aligned_images = []
    
    # Use the first image from the channel_data as the reference image
    reference_image = channel_dict[channel_name][0]
    
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
    
    # Color mapping (for demonstration, converting grayscale to a colormap; you can replace this with actual color data)
    color_mapped_image = cv2.applyColorMap(stacked_image, cv2.COLORMAP_JET)
    
    # Resize the image to 250x250 using Lanczos interpolation
    preview_image = cv2.resize(color_mapped_image, (250, 250), interpolation=cv2.INTER_LANCZOS4)
    
    # Add the preview image to the channel_data dictionary
    channel_dict[channel_name].append(preview_image)

# Example usage
#align_and_stack_images(channel_data['RGB'], 'R')  # For the Red channel in RGB
#align_and_stack_images(channel_data['Narrowband'], 'Ha')  # For the Ha channel in Narrowband
#align_and_stack_images(channel_data['JWST']['NIRCam'], 'Short_Wavelength')  # For the Short_Wavelength channel in NIRCam

def open_fits_channel(channel_dict, files):
    if not files:
        return

    for file in files:
        data = fits.open(file.stream)[0].data
        normalized_data = normalize_data(data)
        
        # Determine which channel to append the data to
        for main_channel, sub_channels in channel_dict.items():
            if isinstance(sub_channels, dict):
                for sub_channel in sub_channels:
                    channel_dict[main_channel][sub_channel].append(normalized_data)
            else:
                channel_dict[main_channel].append(normalized_data)
                