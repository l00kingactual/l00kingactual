from astropy.io import fits

# Open the FITS file
hdulist = fits.open('path_to_fits_file.fits')

# Extract header data
header = hdulist[0].header

# Print some specific header information
print(header['OBJECT'])  # Name of the object observed
print(header['DATE-OBS'])  # Date of observation

# Extract image data
image_data = hdulist[0].data

# Close the FITS file
hdulist.close()
