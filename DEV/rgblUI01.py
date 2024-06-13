import tkinter as tk
from tkinter import filedialog
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import shift
from PIL import Image, ImageTk

# Global variables to store the data for each channel
blue_data = None
green_data = None
red_data = None
luminance_data = None

def open_fits_blue():
    global blue_data
    blue_data = open_fits_channel()
    
def open_fits_green():
    global green_data
    green_data = open_fits_channel()

def open_fits_red():
    global red_data
    red_data = open_fits_channel()

def open_fits_luminance():
    global luminance_data
    luminance_data = open_fits_channel()

def open_fits_channel():
    filepath = filedialog.askopenfilename(filetypes=[("FITS files", ("*.fit", "*.fits"))])
    if not filepath:
        return None
    return fits.open(filepath)[0].data

def align_stars():
    global blue_data, green_data, red_data, luminance_data

    # Define a function to get the shift values based on the brightest pixel
    def get_shift(data):
        return np.unravel_index(np.argmax(data), data.shape)

    # Align the stars using the brightest pixel
    reference_shift = get_shift(blue_data)
    green_shift = np.array(get_shift(green_data)) - np.array(reference_shift)
    red_shift = np.array(get_shift(red_data)) - np.array(reference_shift)
    luminance_shift = np.array(get_shift(luminance_data)) - np.array(reference_shift)

    green_data = shift(green_data, shift=green_shift)
    red_data = shift(red_data, shift=red_shift)
    luminance_data = shift(luminance_data, shift=luminance_shift)

    display()

def display():
    # Combine channels to produce a color image
    color_image = np.stack((red_data, green_data, blue_data), axis=-1)
    color_image = (color_image - np.min(color_image)) / (np.max(color_image) - np.min(color_image))
    color_image = (color_image * 255).astype(np.uint8)

    # Convert to PIL Image and display in the UI
    img = Image.fromarray(color_image)
    img = ImageTk.PhotoImage(img)
    label_img.config(image=img)
    label_img.image = img

app = tk.Tk()
app.title("FITS Viewer Enhanced")

# Buttons to open FITS files for each channel
btn_open_blue = tk.Button(app, text="Open Blue Channel", command=open_fits_blue)
btn_open_blue.pack(pady=10)

btn_open_green = tk.Button(app, text="Open Green Channel", command=open_fits_green)
btn_open_green.pack(pady=10)

btn_open_red = tk.Button(app, text="Open Red Channel", command=open_fits_red)
btn_open_red.pack(pady=10)

btn_open_luminance = tk.Button(app, text="Open Luminance Channel", command=open_fits_luminance)
btn_open_luminance.pack(pady=10)

# Button to align stars and display color image
btn_align = tk.Button(app, text="Align Stars & Display", command=align_stars)
btn_align.pack(pady=20)

# Label to display the image
label_img = tk.Label(app)
label_img.pack(pady=20)

app.mainloop()
