
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
    file_path = filedialog.askopenfilename(filetypes=[('FITS files', '*.fits')])
    if file_path:
        with fits.open(file_path) as hdul:
            data = hdul[0].data.astype(np.float64)
        channels_data[channel].append(data)
        average_data = average_images(channels_data[channel])
        display_small_preview(average_data, preview_labels[channel])


# Function to display images in the Hubble palette
def display_hubble_palette():
    ha_data = average_images(channels_data['Ha'])
    sii_data = average_images(channels_data['SII'])
    oiii_data = average_images(channels_data['OIII'])
    
    # TODO: Implement the logic to combine these into a Hubble palette image
    # This is a placeholder; the actual logic will depend on the specifics of the Hubble palette representation


# Modified UI Logic
root = Tk()

root.title("Narrowband Image Processor")
root.geometry("800x600")

preview_labels = {
    'Ha': Label(root),
    'SII': Label(root),
    'OIII': Label(root),
    'luminance': Label(root)
}

for channel, label in preview_labels.items():
    label.pack()
    Button(root, text=f"Load {channel} Data", command=lambda channel=channel: load_data(channel)).pack()

Button(root, text="Align & Display", command=None).pack()  # Placeholder for the align and display functionality
Button(root, text="Display in Hubble Palette", command=display_hubble_palette).pack()  # Hubble Palette button

root.mainloop()
