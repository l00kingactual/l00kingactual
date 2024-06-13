import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
import logging
import warnings
from astropy.utils.exceptions import AstropyWarning

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Suppress specific AstroPy warnings
warnings.filterwarnings('ignore', category=AstropyWarning, message='.*datfix.*')

def calculate_fov(wcs, shape):
    # Calculate the degrees per pixel along each axis
    cdelt1 = np.abs(wcs.wcs.cdelt[0])  # Scale along x-axis
    cdelt2 = np.abs(wcs.wcs.cdelt[1])  # Scale along y-axis
    
    # Calculate the FoV
    fov_x = shape[0] * cdelt1  # FoV along the x-axis
    fov_y = shape[1] * cdelt2  # FoV along the y-axis
    
    return fov_x, fov_y

def process_fits_image(fits_file):
    try:
        with fits.open(fits_file) as hdul:
            hdul.info()
            image_data = hdul[0].data
            if image_data is None:
                raise ValueError("Image data is None. Check the FITS file and HDU.")
            if not np.issubdtype(image_data.dtype, np.number):
                raise TypeError("Image data is not a numeric array.")

            single_channel_data = image_data[:, :, 0]
            median_value = np.median(single_channel_data)
            logging.info(f"Median value: {median_value}")

            offset_data = single_channel_data - median_value
            offset_data_clipped = np.clip(offset_data, a_min=1e-10, a_max=None)
            processed_data = np.log(offset_data_clipped)

            wcs = WCS(hdul[0].header, naxis=2)
            fov_x, fov_y = calculate_fov(wcs, single_channel_data.shape)
            logging.info(f"Field of View: {fov_x}° x {fov_y}°")

            plt.figure(figsize=(10, 10))
            ax = plt.subplot(projection=wcs)
            ax.imshow(processed_data, origin='lower', cmap='gray', aspect='auto')
            ax.set_xlabel('Right Ascension')
            ax.set_ylabel('Declination')
            ax.grid(color='white', ls='solid')
            plt.title(f"Field of View: {fov_x:.2f}° x {fov_y:.2f}°")
            plt.show()

    except FileNotFoundError:
        logging.error(f"File not found: {fits_file}")
    except OSError as e:
        logging.error(f"Error reading FITS file: {e}")
    except ValueError as ve:
        logging.error(ve)
    except Exception as ex:
        logging.error(f"An unexpected error occurred: {ex}")

fits_file_path = 'D:\\dads FITS data\\1NGC7023-001B.fit'
process_fits_image(fits_file_path)
