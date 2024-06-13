from astropy.io import fits
import numpy as np

fits_file = 'D:\\dads FITS data\\81&82-RGB.fit'
hdul = fits.open(fits_file)

# Ensure the primary HDU contains image data
image_data = hdul[0].data
if image_data is not None:
    # Check if the median calculation is valid
    median_value = np.median(image_data)
    if median_value is not None:
        processed_data = np.log(image_data - median_value)
    else:
        print("Could not calculate the median of the image data.")
else:
    print("No image data found in the primary HDU.")
