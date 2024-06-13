from flask import Flask, render_template, request
from astropy.io import fits
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Read the FITS file
            hdulist = fits.open(file)
            data = hdulist[0].data

            # Plot the data
            plt.figure()
            plt.imshow(data, cmap='gray')
            plt.colorbar()
            plt.axis('off')

            # Convert the plot to PNG and then to base64 to display in HTML
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            img_base64 = base64.b64encode(img.getvalue()).decode('utf-8').replace('\n', '')
            img.close()

            return render_template('index.html', img_data=img_base64)

    return render_template('index.html', img_data=None)

if __name__ == '__main__':
    app.run(debug=True)
