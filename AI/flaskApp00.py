from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Logic to read failed_urls.txt and wikiURLSearch.txt
    # ...
    return render_template('index.html', failed_urls=failed_urls)

@app.route('/update', methods=['POST'])
def update():
    # Logic to update wikiURLSearch.txt
    # ...
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
