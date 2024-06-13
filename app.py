from flask import Flask, render_template, request, send_file, jsonify
import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import base64
from astropy.io import fits

# Import functions from fits01.py
from fits01 import open_fits_channel, align_and_stack_images, channel_data, normalize_data

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('fitsFile')
    channel = request.form['channel']
    
    # Process the FITS files using open_fits_channel function
    open_fits_channel(channel_data[channel], files)
    
    # Align and stack images
    align_and_stack_images(channel_data[channel], channel)
    
    # Create a Matplotlib plot
    plt.figure(figsize=(6, 6))
    plt.imshow(channel_data[channel][-1], cmap='gray')  # Display the last image (stacked and aligned)
    plt.axis('off')
    
    # Save the plot to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode()
    
    # Return the base64 encoded image
    return jsonify({'img_base64': img_base64})

@app.route('/preview/<channel>/<frequency>', methods=['GET'])
def preview(channel, frequency):
    print(f"Received request for channel: {channel}, frequency: {frequency}")  # Debugging line

    # Replace this with the actual path to your FITS file
    fits_file_path = f"{channel}_{frequency}.fits"

    # Open the FITS file and read the data
    with fits.open(fits_file_path) as hdul:
        data = hdul[0].data

    # Normalize the data to 8-bit
    normalized_data = ((data - np.min(data)) / (np.max(data) - np.min(data)) * 255).astype(np.uint8)

    # Convert to a color image for demonstration (replace this with your actual color mapping)
    color_mapped_image = cv2.applyColorMap(normalized_data, cv2.COLORMAP_JET)

    # Resize the image to 250x250 using Lanczos interpolation
    resized_image = cv2.resize(color_mapped_image, (250, 250), interpolation=cv2.INTER_LANCZOS4)

    # Convert to PIL Image
    pil_img = Image.fromarray(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))

    # Save to a BytesIO object
    byte_io = BytesIO()
    pil_img.save(byte_io, 'PNG')
    byte_io.seek(0)

    return send_file(byte_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
