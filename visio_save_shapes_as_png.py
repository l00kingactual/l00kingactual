import os
import comtypes.client
import tkinter as tk
from tkinter import filedialog

def save_shapes_as_png(visio_path, output_dir):
    # Create Visio application instance
    visio = comtypes.client.CreateObject("Visio.Application")
    visio.Visible = False

    # Open the Visio document
    doc = visio.Documents.Open(visio_path)

    # Loop through each page in the document
    for page in doc.Pages:
        # Loop through each shape in the page
        for shape in page.Shapes:
            if shape.Type == 1:  # Shape.Type 1 indicates a group or shape
                shape_name = shape.Name.replace(" ", "_")
                # Save each shape as PNG
                png_path = os.path.join(output_dir, f"{shape_name}.png")
                shape.Export(png_path)

    # Close the document and quit Visio application
    doc.Close()
    visio.Quit()

    print(f"Shapes from {visio_path} have been saved to {output_dir}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        visio_files = filedialog.askopenfilenames(filetypes=[("Visio files", "*.vsd *.vsdx")])
        if visio_files:
            for visio_path in visio_files:
                output_dir = os.path.join(directory, 'shapes')
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                save_shapes_as_png(visio_path, output_dir)

# Initialize main window
root = tk.Tk()
root.title("Visio Shapes to PNG Converter")

tk.Label(root, text="Select Directory to Save PNG Files").pack(pady=10)
select_button = tk.Button(root, text="Select Directory", command=select_directory)
select_button.pack(pady=10)

root.mainloop()
