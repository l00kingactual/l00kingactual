from flask import Flask, render_template, request, jsonify
from astropy.io import fits
import numpy as np
from fits02 import open_fits_channel, align_and_stack_images, channel_data, normalize_data, numpy_array_to_base64
import cv2
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import logging
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # 1. Data Structures: Consistent channel_data dictionary
    channel_data = {
    'RGB': {'Red': [], 'Green': [], 'Blue': [], 'Luminance': []},
    'Narrowband': {'Ha': [], 'SII': [], 'OIII': []},
    'JWST': {
        'NIRCam': {'Short_Wavelength': [], 'Long_Wavelength': []},
        'NIRSpec': {'Spectral_Range': []},
        'MIRI': {'Spectral_Range': []},
        'FGS/NIRISS': {'Spectral_Range': []}
    }
}
    return render_template('index.html', channel_data=channel_data)

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        files = request.files.getlist('fitsFile')
        channel = request.form['channel']
        frequency = request.form['frequency']

        # Open and normalize the FITS files
        open_fits_channel(channel_data[channel], files, frequency)

        # Create a Matplotlib figure from the last uploaded FITS file
        last_uploaded_data = channel_data[channel][frequency][-1]
        img_base64 = numpy_array_to_base64(last_uploaded_data)

        # Stack and align images if all frequencies are uploaded
        if all(len(channel_data[channel][f]) > 0 for f in channel_data[channel]):
            align_and_stack_images(channel_data, channel)

            # Convert the stacked image to base64
            stacked_img_base64 = numpy_array_to_base64(channel_data[channel][-1])
            return jsonify({'status': 'success', 'img_base64': stacked_img_base64})

        return jsonify({'status': 'success', 'img_base64': img_base64})

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/stack_and_align', methods=['POST'])
def stack_and_align():
    try:
        channel = request.form['channel']
        align_and_stack_images(channel_data, channel)
        stacked_img_base64 = numpy_array_to_base64(channel_data[channel][-1])
        return jsonify({'status': 'success', 'img_base64': stacked_img_base64})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/save_image', methods=['POST'])
def save_image():
    try:
        channel = request.form['channel']
        file_format = request.form.get('format', 'png')  # Default to PNG if not provided

        # Validate the format
        if file_format not in ['png', 'jpg', 'jpeg', 'bmp', 'tif', 'tiff', 'gif']:
            return jsonify({'status': 'error', 'message': 'Invalid file format'}), 400

        # Assuming channel_data[channel][-1] contains the image data as a NumPy array
        image_data = np.array(channel_data[channel][-1])

        # Convert the image to a format that OpenCV can save
        image_data = cv2.normalize(image_data, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        # Save the image
        file_path = f"saved_images/image.{file_format}"
        cv2.imwrite(file_path, image_data)

        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
