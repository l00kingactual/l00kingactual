
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
def display_small_preview(data, label_widget, size=(250, 250)):
    norm_data = ((data - np.min(data)) / (np.max(data) - np.min(data)) * 255).astype(np.uint8)
    img = Image.fromarray(norm_data, 'L')
    img = img.resize(size, Image.ANTIALIAS)  # Resizing the image
    img = ImageTk.PhotoImage(img)
    label_widget.config(image=img)
    label_widget.image = img


# Function to load FITS data
def load_data(channel):
    file_path = filedialog.askopenfilename(filetypes=[('FITS files', '*.fit, *.fits')])
    if file_path:
        with fits.open(file_path) as hdul:
            data = hdul[0].data.astype(np.float64)
        channels_data[channel].append(data)
        average_data = average_images(channels_data[channel])
        display_small_preview(average_data, preview_labels[channel])


# Function to align images
# This is a placeholder for actual image alignment logic
def align_images(images_dict):
    # Assuming the first image in each channel is the reference image
    ref_image = images_dict['Ha'][0]
    aligned_images = {}
    for channel, images in images_dict.items():
        # Placeholder for alignment logic; currently, just using the reference image
        aligned_images[channel] = ref_image
    return aligned_images


# Function to display aligned image
def display_aligned_image():
    aligned_images = align_images(channels_data)
    # Combine the aligned images from each channel to create an RGB image
    # Placeholder for the actual logic of combining images
    combined_image = np.stack([aligned_images['Ha'], aligned_images['SII'], aligned_images['OIII']], axis=2)
    
    # Display the aligned and combined image at 1000x1000 pixels
    display_small_preview(combined_image, preview_labels['aligned'], size=(1000, 1000))


# Function to display images in the Hubble palette
def display_hubble_palette():
    ha_data = average_images(channels_data['Ha'])
    sii_data = average_images(channels_data['SII'])
    oiii_data = average_images(channels_data['OIII'])
    
    # Create an RGB image based on the Hubble palette
    rgb_image = np.stack([sii_data, ha_data, oiii_data], axis=2)
    
    # Display the Hubble palette image at 1000x1000 pixels
    display_small_preview(rgb_image, preview_labels['hubble'], size=(1000, 1000))


# Modified UI Logic
root = Tk()

root.title("Narrowband Image Processor")
root.geometry("800x600")

preview_labels = {
    'Ha': Label(root),
    'SII': Label(root),
    'OIII': Label(root),
    'luminance': Label(root),
    'aligned': Label(root),  # Label for displaying the aligned image
    'hubble': Label(root)    # Label for displaying the Hubble palette image
}

for channel, label in preview_labels.items():
    label.pack()
    if channel in ['Ha', 'SII', 'OIII', 'luminance']:
        Button(root, text=f"Load {channel} Data", command=lambda channel=channel: load_data(channel)).pack()

Button(root, text="Align & Display", command=display_aligned_image).pack()  # Updated align and display functionality
Button(root, text="Display in Hubble Palette", command=display_hubble_palette).pack()  # Hubble Palette button

root.mainloop()
