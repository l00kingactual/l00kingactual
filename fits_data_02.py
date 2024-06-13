import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_fits_image(fits_file):
    try:
        # Attempt to open the FITS file
        with fits.open(fits_file) as hdul:
            # Inspect the file to ensure it contains image data
            hdul.info()

            # Extract image data from the primary HDU
            image_data = hdul[0].data
            if image_data is None:
                raise ValueError("Image data is None. Check the FITS file and HDU.")

            # Ensure image data is in a valid numeric format
            if not np.issubdtype(image_data.dtype, np.number):
                raise TypeError("Image data is not a numeric array.")

            # Calculate median and subtract it from the image data
            median_value = np.median(image_data)
            logging.info(f"Median value: {median_value}")

            offset_data = image_data - median_value
            offset_data_clipped = np.clip(offset_data, a_min=1e-10, a_max=None)

            # Apply logarithmic transformation
            processed_data = np.log(offset_data_clipped)

            # Use WCS information for proper coordinate mapping
            wcs = WCS(hdul[0].header)

            # Plotting
            plt.figure(figsize=(10, 10))
            ax = plt.subplot(projection=wcs)
            ax.imshow(processed_data, origin='lower', cmap='gray', aspect='auto')
            ax.set_xlabel('Right Ascension')
            ax.set_ylabel('Declination')
            ax.grid(color='white', ls='solid')

            plt.show()

    except FileNotFoundError:
        logging.error(f"File not found: {fits_file}")
    except OSError as e:
        logging.error(f"Error reading FITS file: {e}")
    except ValueError as ve:
        logging.error(ve)
    except Exception as ex:
        logging.error(f"An unexpected error occurred: {ex}")

# Replace 'path_to_your_fits_file.fits' with the actual path to your FITS file
fits_file_path = 'D:\\dads FITS data\\1NGC7023-001B.fit'
process_fits_image(fits_file_path)
