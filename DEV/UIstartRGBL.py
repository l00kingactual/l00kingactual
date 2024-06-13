import tkinter as tk
from tkinter import filedialog, messagebox
from astropy.io import fits
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import numpy as np
from scipy.ndimage import shift


# Global variables to store the data for each channel
blue_data = None
green_data = None
red_data = None
luminance_data = None

def open_fits_blue():
    global blue_data
    filepath = filedialog.askopenfilename(filetypes=[("FITS files", ("*.fit", "*.fits"))])
    if not filepath:
        return
    blue_data = fits.open(filepath)[0].data
    display_temp_image(blue_data)

def open_fits_green():
    global green_data
    filepath = filedialog.askopenfilename(filetypes=[("FITS files", ("*.fit", "*.fits"))])
    if not filepath:
        return
    green_data = fits.open(filepath)[0].data
    display_temp_image(green_data)

def open_fits_red():
    global red_data
    filepath = filedialog.askopenfilename(filetypes=[("FITS files", ("*.fit", "*.fits"))])
    if not filepath:
        return
    red_data = fits.open(filepath)[0].data
    display_temp_image(red_data)

def open_fits_luminance():
    global luminance_data
    filepath = filedialog.askopenfilename(filetypes=[("FITS files", ("*.fit", "*.fits"))])
    if not filepath:
        return
    luminance_data = fits.open(filepath)[0].data
    display_temp_image(luminance_data)

def display_temp_image(data):
    # Plot the data and save as PNG
    plt.figure()
    plt.imshow(data, cmap='gray')
    plt.colorbar()
    plt.axis('off')
    plt.savefig("temp.png")
    plt.close()

    # Load the PNG and display in the UI
    img = Image.open("temp.png")
    img = img.resize((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label_img.config(image=img)
    label_img.image = img


def align_stars():
    global blue_data, green_data, red_data, luminance_data

    # Read the FITS files
    blue_data = fits.open('path_to_blue_channel.fits')[0].data
    green_data = fits.open('path_to_green_channel.fits')[0].data
    red_data = fits.open('path_to_red_channel.fits')[0].data
    luminance_data = fits.open('path_to_luminance_channel.fits')[0].data

    # Define a function to get the shift values
    def get_shift(data):
        max_val = np.max(data)
        location_max = np.argwhere(data == max_val)[0]
        return location_max

    # Align the stars using the first change in value from 0 to maximum value
    reference_shift = get_shift(blue_data)
    green_shift = get_shift(green_data) - reference_shift
    red_shift = get_shift(red_data) - reference_shift
    luminance_shift = get_shift(luminance_data) - reference_shift

    green_data = shift(green_data, shift=green_shift)
    red_data = shift(red_data, shift=red_shift)
    luminance_data = shift(luminance_data, shift=luminance_shift)

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

# ... (rest of the tkinter UI code)


app = tk.Tk()
app.title("FITS Viewer Enhanced")

# Button to open FITS file
btn_open = tk.Button(app, text="Open FITS File", command=open_fits)
btn_open.pack(pady=20)

btn_open_blue = tk.Button(app, text="Open Blue Channel", command=open_fits_blue)
btn_open_blue.pack(pady=10)

btn_open_green = tk.Button(app, text="Open Green Channel", command=open_fits_green)
btn_open_green.pack(pady=10)

btn_open_red = tk.Button(app, text="Open Red Channel", command=open_fits_red)
btn_open_red.pack(pady=10)

btn_open_luminance = tk.Button(app, text="Open Luminance Channel", command=open_fits_luminance)
btn_open_luminance.pack(pady=10)

# Button to align stars and display color image
btn_align = tk.Button(app, text="Align Stars & Display", command=align_stars_and_display)
btn_align.pack(pady=20)

# Label to display the image
label_img = tk.Label(app)
label_img.pack(pady=20)

app.mainloop()
