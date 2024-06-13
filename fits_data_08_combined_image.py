import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS

# Define the directory path
directory_path = 'D:\\temp\\'

# Initialize empty lists for each color group
blue_data = []
red_data = []
green_data = []
lum_data = []

# Initialize variables for combined plots
combined_rgb = None
combined_rgbl = None

# Iterate through files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.fit') or filename.endswith('.fits'):
        # Read FITS file
        file_path = os.path.join(directory_path, filename)
        hdul = fits.open(file_path)
        data = hdul[0].data
        wcs = WCS(hdul[0].header)
        
        # Determine the color group based on filename
        color_group = None
        if 'B' in filename:
            color_group = 'Blue'
            blue_data.append({'Filename': filename, 'Data': data})
        elif 'R' in filename:
            color_group = 'Red'
            red_data.append({'Filename': filename, 'Data': data})
        elif 'G' in filename:
            color_group = 'Green'
            green_data.append({'Filename': filename, 'Data': data})
        elif 'L' in filename:
            color_group = 'Luminance'
            lum_data.append({'Filename': filename, 'Data': data})
        
        # Create individual color plots
        plt.figure(figsize=(8, 8))
        plt.imshow(data, cmap='gray', origin='lower')
        plt.title(f'{color_group} - {filename}')
        plt.colorbar()
        plt.savefig(f'{color_group}_{filename}.png')
        plt.close()
        
        # Combine RGB and RGBl images
        if color_group in ['Red', 'Green', 'Blue']:
            if combined_rgb is None:
                combined_rgb = np.zeros_like(data, dtype=np.float64)
            combined_rgb += data.astype(np.float64)
        
        if color_group in ['Red', 'Green', 'Blue', 'Luminance']:
            if combined_rgbl is None:
                combined_rgbl = np.zeros_like(data, dtype=np.float64)
            combined_rgbl += data.astype(np.float64)

# Create overall combined RGB plot
plt.figure(figsize=(8, 8))
plt.imshow(combined_rgb, cmap='gray', origin='lower')
plt.title('Combined RGB')
plt.colorbar()
plt.savefig('Combined_RGB.png')
plt.close()

# Create overall combined RGBl plot
plt.figure(figsize=(8, 8))
plt.imshow(combined_rgbl, cmap='gray', origin='lower')
plt.title('Combined RGBl')
plt.colorbar()
plt.savefig('Combined_RGBl.png')
plt.close()

# Create DataFrames from the lists
df_blue = pd.DataFrame(blue_data)
df_red = pd.DataFrame(red_data)
df_green = pd.DataFrame(green_data)
df_lum = pd.DataFrame(lum_data)

# Save DataFrames to CSV
#df_blue.to_csv('blue_files.csv', index=False)
#df_red.to_csv('red_files.csv', index=False)
#df_green.to_csv('green_files.csv', index=False)
#df_lum.to_csv('luminance_files.csv', index=False)
