import tkinter as tk
from tkinter import filedialog, messagebox
from astropy.io import fits
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

def open_fits():
    filepath = filedialog.askopenfilename(filetypes=[("FITS files", ("*.fit", "*.fits"))])
    if not filepath:
        return

    # Read the FITS file
    hdulist = fits.open(filepath)
    data = hdulist[0].data

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

app = tk.Tk()
app.title("FITS Viewer")

# Button to open FITS file
btn_open = tk.Button(app, text="Open FITS File", command=open_fits)
btn_open.pack(pady=20)

# Label to display the image
label_img = tk.Label(app)
label_img.pack(pady=20)

app.mainloop()