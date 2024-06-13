from astropy.io import fits

# Path to your FITS file
fits_file = 'D:\\dads FITS data\\1NGC7023-001B.fit'

# Open the FITS file
with fits.open(fits_file) as hdul:

    # Print information about the FITS file contents
    hdul.info()

    # Access the primary HDU (Header/Data Unit)
    primary_hdu = hdul[0]

    # Access the image data from the primary HDU
    image_data = primary_hdu.data

    # Print the shape of the image data array
    print("Image data shape:", image_data.shape)
