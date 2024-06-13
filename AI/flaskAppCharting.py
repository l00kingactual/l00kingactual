from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    # Your data preparation logic here
    data = {'Toppings': ['Mushrooms', 'Onions', 'Peppers'], 'Counts': [5, 7, 2]}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
