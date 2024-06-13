from astropy.io import fits
import pandas as pd
import numpy as np

fits_file = 'D:\\dads FITS data\\1NGC7023-001B.fit'
with fits.open(fits_file) as hdul:
    # Access the primary HDU's image data
    image_data = hdul[0].data

    # Check if image_data is 2D, as we expect for a CSV conversion
    if len(image_data.shape) == 2:
        # Flatten the 2D image data to a 2-column format for CSV
        x_indices, y_indices = np.meshgrid(np.arange(image_data.shape[1]), np.arange(image_data.shape[0]))
        flattened_data = np.column_stack((x_indices.flatten(), y_indices.flatten(), image_data.flatten()))

        # Convert to pandas DataFrame
        df = pd.DataFrame(flattened_data, columns=['X', 'Y', 'Intensity'])

        # Save to CSV
        df.to_csv('converted_image_data.csv', index=False)
    else:
        print("Image data is not 2D and cannot be directly converted to CSV.")
