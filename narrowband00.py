import numpy as np
from astropy.io import fits
from tkinter import filedialog, Label, Button, Tk
from PIL import Image, ImageTk

# Initialize global dictionaries to hold multiple datasets per channel
channels_data = {'Ha': [], 'SII': [], 'OIII': [], 'luminance': []}

# Function to average multiple images
def average_images(data_list):
    return np.mean(data_list, axis=0)

# Function to display a small preview of the image
def display_small_preview(data, label_widget):
    norm_data = ((data - np.min(data)) / (np.max(data) - np.min(data)) * 255).astype(np.uint8)
    pil_img = Image.fromarray(norm_data, 'L').resize((250, 250), Image.LANCZOS)
    img = ImageTk.PhotoImage(pil_img)
    label_widget.config(image=img)
    label_widget.image = img

# Updated function to open and store multiple FITS files per channel
def open_fits_channel(channel, label_widget):
    filepaths = filedialog.askopenfilenames(filetypes=[("FITS files", ("*.fit", "*.fits"))])
    if not filepaths:
        return

    channel_data = []
    for filepath in filepaths:
        data = fits.open(filepath)[0].data
        channel_data.append(data)

    # Average the images and store in global channels_data dictionary
    channels_data[channel] = average_images(channel_data)

    # Display a small preview of the combined channel data
    display_small_preview(channels_data[channel], label_widget)

from astroalign import register

# Aligns source_data with target_data using the astroalign library
def align_with_astroalign(source_data, target_data):
    aligned_data, _ = register(source_data, target_data)
    return aligned_data

# Function to combine channels into a single colour image
def combine_channels_into_colour(Ha_data, SII_data, OIII_data):
    return np.stack((Ha_data, SII_data, OIII_data), axis=2).astype(np.uint8)


# Your align_with_astroalign and save_image functions go here

# Function to align and display channels
def align_and_display():
    global combined_image, label_natural_colour_img
    # Initialize variables
    Ha_data = channels_data.get('Ha', None)
    SII_data = channels_data.get('SII', None)
    OIII_data = channels_data.get('OIII', None)

    if Ha_data is None or SII_data is None or OIII_data is None:
        print("All channels must be loaded before alignment.")
        return

    # Alignment
    aligned_SII = align_with_astroalign(SII_data, Ha_data)
    aligned_OIII = align_with_astroalign(OIII_data, Ha_data)

    # Create natural colour image
    natural_colour_data = combine_channels_into_colour(Ha_data, aligned_SII, aligned_OIII)
    combined_image = natural_colour_data  # Update the global variable
    
    # Display a small preview (assuming function handles resizing)
    display_small_preview(natural_colour_data, label_natural_colour_img)


def resize_image(image, base_width=250):
    w_percent = (base_width / float(image.size[0]))
    h_size = int((float(image.size[1]) * float(w_percent)))
    return image.resize((base_width, h_size), Image.LANCZOS)


def save_colour_image():
    global combined_image  # Declare the global variable
    
    # Check if combined_image is defined
    if 'combined_image' not in globals():
        print("Error: 'combined_image' is not defined.")
        return

    try:
        # Convert the combined_image numpy array to a PIL Image
        img_to_save = Image.fromarray((combined_image * 255).astype('uint8'))
    except Exception as e:
        print(f"Error in PIL Image creation: {e}")
        return

    # Resize the image while maintaining aspect ratio
    resized_img = resize_image(img_to_save, base_width=1920)

    # Define the file types for the save dialog
    filetypes = [
        ("PNG files", "*.png"),
        ("JPEG files", "*.jpg"),
        ("BMP files", "*.bmp"),
        ("TIFF files", "*.tif"),
        ("All files", "*.*")
    ]

    # Invoke the save dialog
    filename = filedialog.asksaveasfilename(filetypes=filetypes)
    
    if not filename:
        return
    
    # Saving the image
    try:
        resized_img.save(filename)
    except Exception as e:
        print(f"Failed to save image: {e}")
    
from PIL import Image, ImageTk
import numpy as np

def display_small_preview(data, label_widget):
    print(f"Data Shape: {data.shape}, Data Type: {data.dtype}")

    # Check if data is 2D or 3D and normalize it
    if len(data.shape) == 2:
        print("Warning: Data is not 3D. Converting to 3D.")
        data = np.stack([data]*3, axis=2)
    elif len(data.shape) != 3:
        print("Error: Data is neither 2D nor 3D.")
        return

    norm_data = ((data - np.min(data)) / (np.max(data) - np.min(data)) * 255).astype('uint8')

    try:
        pil_img = Image.fromarray(norm_data, 'RGB').resize((250, 250), Image.LANCZOS)
    except Exception as e:
        print(f"Error in PIL Image creation: {e}")
        return
    
    try:
        tk_img = ImageTk.PhotoImage(image=pil_img)
        label_widget.config(image=tk_img)
        label_widget.image = tk_img  # keep a reference to prevent GC from deleting the image
    except Exception as e:
        print(f"Error in Tkinter Image update: {e}")

# ... (Tkinter setup)
# Function to save the natural colour image as a popular image format
# Tkinter GUI components
from tkinter import Label, Tk, Button, Frame, Canvas, filedialog
from tkinter import StringVar

# Initialize Tkinter root window once
root = Tk()
root.geometry('1300x1200')  # Set the window size

# Text labels for buttons
load_text = StringVar()
load_text.set("Load")

# Create Frames
frame_top = Frame(root)
frame_top.grid(row=0, column=0, columnspan=3)

frame_middle = Frame(root)
frame_middle.grid(row=1, column=0, columnspan=3)

frame_bottom = Frame(root)
frame_bottom.grid(row=2, column=0, columnspan=3)

# Create Labels for 250 placeholders
label_ha_img = Label(frame_top, width=25, height=25, bg="grey")
label_ha_img.grid(row=0, column=0)

label_sii_img = Label(frame_top, width=25, height=25, bg="grey")
label_sii_img.grid(row=0, column=1)

label_oiii_img = Label(frame_top, width=25, height=25, bg="grey")
label_oiii_img.grid(row=0, column=2)

label_natural_colour_img = Label(frame_bottom, width=100, height=100, bg="grey")
label_natural_colour_img.grid(row=1, column=0, columnspan=3)

# Create Load File Buttons
Button(frame_middle, text="Load Ha", command=lambda: open_fits_channel('Ha', label_ha_img)).grid(row=0, column=0)
Button(frame_middle, text="Load SII", command=lambda: open_fits_channel('SII', label_sii_img)).grid(row=0, column=1)
Button(frame_middle, text="Load OIII", command=lambda: open_fits_channel('OIII', label_oiii_img)).grid(row=0, column=2)

# Create Align & Save Buttons
Button(frame_bottom, text="Align and Display Channels", command=align_and_display).grid(row=0, column=0)
Button(frame_bottom, text="Save Natural Colour Image", command=save_colour_image).grid(row=0, column=1)

# Create Label for 1000px placeholder
label_natural_colour_img = Label(frame_bottom, width=100, height=40, bg="grey")
label_natural_colour_img.grid(row=1, column=0, columnspan=3)

root.mainloop()


