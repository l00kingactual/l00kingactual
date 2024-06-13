import matplotlib.pyplot as plt
from astropy.io import fits

# Load FITS file
fits_file = 'D:\\dads FITS data\\1NGC7023-001B.fit'
with fits.open(fits_file) as hdul:
    image_data = hdul[0].data

# Plot and save the image data
plt.imshow(image_data, cmap='gray')
plt.colorbar()
plt.savefig('converted_image.png')
