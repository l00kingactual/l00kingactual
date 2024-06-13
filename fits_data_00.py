from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.wcs import WCS
import numpy as np

# Step 1: Load the FITS file
fits_file = 'D:\\FITS\\CartwheelGalaxy.fits'
hdul = fits.open(fits_file)

# Step 2: Extract the image data from the primary HDU
image_data = hdul[0].data

# Optional: Process the image data (e.g., normalization, background subtraction)
# This step is highly specific to your data and goals
processed_data = np.log(image_data - np.median(image_data))

# Step 3: Use the WCS (World Coordinate System) information from the FITS header
wcs = WCS(hdul[0].header)

# Step 4: Plotting the image with celestial coordinates
plt.figure(figsize=(10, 10))
ax = plt.subplot(projection=wcs)
ax.imshow(processed_data, origin='lower', cmap='gray')
ax.grid(color='white', ls='solid')
ax.set_xlabel('Right Ascension')
ax.set_ylabel('Declination')

# Overlaying a coordinate grid
overlay = ax.get_coords_overlay('fk5')
overlay.grid(color='white', ls='dotted')
overlay[0].set_axislabel('Right Ascension (J2000)')
overlay[1].set_axislabel('Declination (J2000)')

# Show the plot
plt.show()

# Don't forget to close the FITS file when you're done
hdul.close()
