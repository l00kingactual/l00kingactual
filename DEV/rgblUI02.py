import numpy as np
from astropy.io import fits
from scipy.ndimage import shift
import tkinter as tk
from tkinter import filedialog, Button
from PIL import Image, ImageTk, ImageFilter
import matplotlib.pyplot as plt
import astroalign as aa


# Global variables to store the data for each channel
blue_data, green_data, red_data, luminance_data = None, None, None, None

def open_fits_channel(channel):
    filepath = filedialog.askopenfilename(filetypes=[("FITS files", ("*.fit", "*.fits"))])
    if not filepath:
        return

    data = fits.open(filepath)[0].data

    # Normalize the data to 0-255 for display
    norm_data = ((data - np.min(data)) / (np.max(data) - np.min(data)) * 255).astype(np.uint8)

    # Assign data to the appropriate global variable
    if channel == 'blue':
        global blue_data
        blue_data = data
    elif channel == 'green':
        global green_data
        green_data = data
    elif channel == 'red':
        global red_data
        red_data = data
    elif channel == 'luminance':
        global luminance_data
        luminance_data = data

    # Display the normalized channel data in the UI
    img = Image.fromarray(norm_data)
    img = img.resize((250, 250), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)

    if channel == 'blue':
        label_blue_img.config(image=img)
        label_blue_img.image = img
    elif channel == 'green':
        label_green_img.config(image=img)
        label_green_img.image = img
    elif channel == 'red':
        label_red_img.config(image=img)
        label_red_img.image = img
    elif channel == 'luminance':
        label_luminance_img.config(image=img)
        label_luminance_img.image = img

def align_stars():
    global blue_data, green_data, red_data, luminance_data

    # Convert data to little-endian format
    def to_little_endian(data):
        if data.dtype.byteorder == '>':  # Check if data is big-endian
            return data.byteswap().newbyteorder()
        return data

    # Define a function to align images using AstroAlign
    def align_with_astroalign(source, reference):
        # Convert to little-endian
        source = to_little_endian(source)
        reference = to_little_endian(reference)
        
        aligned_source, footprint = aa.register(source, reference)
        return aligned_source

    # Use blue_data as the reference image
    reference_image = blue_data

    # Align other channels to the reference image
    green_data = align_with_astroalign(green_data, reference_image)
    red_data = align_with_astroalign(red_data, reference_image)
    luminance_data = align_with_astroalign(luminance_data, reference_image)

    display()



def display():
    # Combine channels to produce a color image
    color_image = np.stack((red_data, green_data, blue_data), axis=-1)
    color_image = (color_image - np.min(color_image)) / (np.max(color_image) - np.min(color_image))
    color_image = (color_image * 255).astype(np.uint8)

    # Convert to PIL Image and display in the UI
    img = Image.fromarray(color_image)
    img = img.resize((640, 480), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    label_combined_img.config(image=img)
    label_combined_img.image = img

def save_image():
    global img  # Assuming img is the image object you're working with
    resized_img = img.resize((1920, 1080), Image.LANCZOS)
    resized_img.save("saved_image.png", "PNG")

app = tk.Tk()
app.title("FITS Viewer Enhanced")

# Buttons to open FITS files for each channel
btn_open_blue = tk.Button(app, text="Open Blue Channel", command=lambda: open_fits_channel('blue'))
btn_open_blue.grid(row=0, column=0)

btn_open_green = tk.Button(app, text="Open Green Channel", command=lambda: open_fits_channel('green'))
btn_open_green.grid(row=0, column=1)

btn_open_red = tk.Button(app, text="Open Red Channel", command=lambda: open_fits_channel('red'))
btn_open_red.grid(row=0, column=2)

btn_open_luminance = tk.Button(app, text="Open Luminance Channel", command=lambda: open_fits_channel('luminance'))
btn_open_luminance.grid(row=0, column=3)

# Labels to display the images for each channel
label_blue_img = tk.Label(app)
label_blue_img.grid(row=1, column=0)

label_green_img = tk.Label(app)
label_green_img.grid(row=1, column=1)

label_red_img = tk.Label(app)
label_red_img.grid(row=1, column=2)

label_luminance_img = tk.Label(app)
label_luminance_img.grid(row=1, column=3)

# Button to align stars and display color image
btn_align = tk.Button(app, text="Align Stars & Display", command=align_stars)
btn_align.grid(row=2, column=0, columnspan=4)

save_button = tk.Button(app, text="Save Image", command=save_image)
save_button.grid(row=4, column=0, columnspan=4)

# Label to display the combined color image
label_combined_img = tk.Label(app)
label_combined_img.grid(row=3, column=0, columnspan=4)

app.mainloop()
