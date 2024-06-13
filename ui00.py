import numpy as np
from astropy.io import fits
from tkinter import filedialog
import tkinter as tk
import cv2

# Global variables to store the data for each channel
blue_data, green_data, red_data, luminance_data, ha_data, sii_data, oiii_data = None, None, None, None, None, None, None

def open_fits_channel(channel):
    filepaths = filedialog.askopenfilenames(filetypes=[("FITS files", ("*.fit", "*.fits"))])
    
    if not filepaths or not all(filepaths):
        return None  # If no file is selected, return None
    
    data_list = []

    for filepath in filepaths:
        data = fits.open(filepath)[0].data
        data_list.append(data)

    # Combine the data arrays from multiple files, if applicable
    combined_data = np.mean(data_list, axis=0)

    # Normalize the data to 0-255 for display
    norm_data = ((combined_data - np.min(combined_data)) / (np.max(combined_data) - np.min(combined_data)) * 255).astype(np.uint8)

    # Assign data to the appropriate global variable
    global blue_data, green_data, red_data, luminance_data, ha_data, sii_data, oiii_data
    if channel == 'blue':
        blue_data = combined_data
    elif channel == 'green':
        green_data = combined_data
    elif channel == 'red':
        red_data = combined_data
    elif channel == 'luminance':
        luminance_data = combined_data
    elif channel == 'ha':
        ha_data = combined_data
    elif channel == 'sii':
        sii_data = combined_data
    elif channel == 'oiii':
        oiii_data = combined_data

# Example usage:
# open_fits_channel('blue')

from PIL import Image

def create_preview():
    global blue_data, green_data, red_data, luminance_data, ha_data, sii_data, oiii_data
    channels = [blue_data, green_data, red_data]
    
    # Create a blank (black) RGB image
    preview_img = Image.new('RGB', (250, 250), color='black')
    
    for i, data in enumerate(channels):
        if data is not None:
            # Rescale the data to 250x250
            resized_data = cv2.resize(data, (250, 250))
            # Normalize to 0-255
            norm_data = ((resized_data - np.min(resized_data)) / (np.max(resized_data) - np.min(resized_data)) * 255).astype(np.uint8)
            preview_img.putchannel(norm_data, i)
    
    preview_img.show()

def create_final_image():
    global blue_data, green_data, red_data, luminance_data, ha_data, sii_data, oiii_data
    channels = [blue_data, green_data, red_data]

    # Create a blank (black) RGB image
    final_img = Image.new('RGB', (1920, 1080), color='black')

    for i, data in enumerate(channels):
        if data is not None:
            # Rescale the data to 1920x1080
            resized_data = cv2.resize(data, (1920, 1080))
            # Normalize to 0-255
            norm_data = ((resized_data - np.min(resized_data)) / (np.max(resized_data) - np.min(resized_data)) * 255).astype(np.uint8)
            final_img.putchannel(norm_data, i)

    # Show a 1000x1000 preview of the final image
    preview_final_img = final_img.resize((1000, 1000), Image.LANCZOS)
    preview_final_img.show()

    # Save the 1920x1080 image
    final_img.save('final_image.png')
