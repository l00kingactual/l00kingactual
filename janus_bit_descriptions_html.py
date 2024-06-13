from flask import Flask, render_template_string

app = Flask(__name__)

# Function to generate binary table for a given number of bits
def generate_binary_table(bits):
    table = []
    for i in range(2 ** bits):
        binary = bin(i)[2:].zfill(bits)
        table.append(binary)
    return table

# Define Janus bit descriptions
janus_bit_descriptions = [
    {"description": 2, "table": generate_binary_table(2)},
    {"description": 5, "table": generate_binary_table(5)},
    {"description": 8, "table": generate_binary_table(8)},
    {"description": 13, "table": generate_binary_table(13)},
]

# Define the HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Janus Bit Descriptions</title>
</head>
<body>
    <h1>Janus Bit Descriptions</h1>
    {% for item in janus_bit_descriptions %}
    <h2>Binary table for {{ item.description }} bits:</h2>
    <table border="1">
        <tr>
            <th>Decimal</th>
            <th>Binary</th>
        </tr>
        {% for row in item.table %}
        <tr>
            <td>{{ loop.index0 }}</td>
            <td>{{ row }}</td>
        </tr>
        {% endfor %}
    </table>
    <br>
    {% endfor %}
</body>
</html>
"""

# Define a route to render the HTML template
@app.route('/')
def index():
    return render_template_string(html_template, janus_bit_descriptions=janus_bit_descriptions)

if __name__ == '__main__':
    app.run(debug=True)
