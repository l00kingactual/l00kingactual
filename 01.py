import numpy as np
from astropy.io import fits
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Global variables to store the data for each channel
Ha_data, SII_data, OIII_data, luminance_data = None, None, None, None
combined_image = None

def open_fits_channel(channel):
    filepath = filedialog.askopenfilename(filetypes=[("FITS files", ("*.fit", "*.fits"))])
    if not filepath:
        return

    data = fits.open(filepath)[0].data
    norm_data = ((data - np.min(data)) / (np.max(data) - np.min(data)) * 255).astype(np.uint8)

    global Ha_data, SII_data, OIII_data, luminance_data
    if channel == 'Ha':
        Ha_data = data
    elif channel == 'SII':
        SII_data = data
    elif channel == 'OIII':
        OIII_data = data
    elif channel == 'luminance':
        luminance_data = data

    # Generate the PIL Image object from the normalized NumPy array
    pil_img = Image.fromarray(norm_data, 'L')  # 'L' mode for greyscale
    img = ImageTk.PhotoImage(pil_img)  # Convert to Tkinter-compatible image

    # Utilize the 'img' object for label configuration
    if channel == 'Ha':
        label_ha_img.config(image=img)
        label_ha_img.image = img
    elif channel == 'SII':
        label_sii_img.config(image=img)
        label_sii_img.image = img
    elif channel == 'OIII':
        label_oiii_img.config(image=img)
        label_oiii_img.image = img
    elif channel == 'luminance':
        label_luminance_img.config(image=img)
        label_luminance_img.image = img

# Hypothetical function to align two datasets using astroalign
def align_with_astroalign(source_data, target_data):
    aligned_data, footprint = fits.register(source_data, target_data)
    return aligned_data

# Function to save aligned image
def save_image(data, filepath):
    # Save the image to a FITS file
    fits.writeto(filepath, data, overwrite=True)

def align_stars():
    global Ha_data, SII_data, OIII_data

    if Ha_data is None or SII_data is None or OIII_data is None:
        print("All channels must be loaded before alignment.")
        return

    # Align SII and OIII to Ha
    aligned_SII = align_with_astroalign(SII_data, Ha_data)
    aligned_OIII = align_with_astroalign(OIII_data, Ha_data)

    # Replace original data with aligned data
    SII_data = aligned_SII
    OIII_data = aligned_OIII

    # Additional processing, for example, to combine the channels or to enhance nebula features
    # can go here.

    # Save the aligned images
    save_image(Ha_data, 'aligned_Ha.fits')
    save_image(SII_data, 'aligned_SII.fits')
    save_image(OIII_data, 'aligned_OIII.fits')

    def display():
    # Combine the channels into a final image and display it.
        global combined_image, Ha_data, SII_data, OIII_data, luminance_data

    # Here you should combine Ha, SII, OIII, and luminance to generate the final image
    # For example, to generate a natural color image, you might use:
    # combined_image = np.stack((SII_data, Ha_data, OIII_data), axis=-1)
    
    combined_image = np.stack((SII_data, Ha_data, OIII_data), axis=-1)
    combined_image = (combined_image - np.min(combined_image)) / (np.max(combined_image) - np.min(combined_image))
    combined_image = (combined_image * 255).astype(np.uint8)

    # Convert to PIL Image and display in the UI
    img = Image.fromarray(combined_image)
    img = img.resize((640, 480), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    label_combined_img.config(image=img)
    label_combined_img.image = img

# ... The rest of your code for Tkinter widgets and other functionalities remains largely the same
# Declare Tkinter objects globally, ensuring their existence prior to manipulation.
app = tk.Tk()
app.title("FITS Viewer Enhanced")

# Declare Labels globally to avoid 'Undefined' errors
label_combined_img = tk.Label(app)
label_ha_img = tk.Label(app)
label_sii_img = tk.Label(app)
label_oiii_img = tk.Label(app)
label_luminance_img = tk.Label(app)



# Buttons for opening Ha, SII, OIII, and Luminance channels
btn_open_ha = tk.Button(app, text="Open Ha Channel", command=lambda: open_fits_channel('Ha'))
btn_open_ha.grid(row=0, column=0)
btn_open_sii = tk.Button(app, text="Open SII Channel", command=lambda: open_fits_channel('SII'))
btn_open_sii.grid(row=0, column=1)
btn_open_oiii = tk.Button(app, text="Open OIII Channel", command=lambda: open_fits_channel('OIII'))
btn_open_oiii.grid(row=0, column=2)
btn_open_luminance = tk.Button(app, text="Open Luminance Channel", command=lambda: open_fits_channel('luminance'))
btn_open_luminance.grid(row=0, column=3)

# ... Rest of the code remains unchanged

# Final line to run the Tkinter event loop
app.mainloop()
