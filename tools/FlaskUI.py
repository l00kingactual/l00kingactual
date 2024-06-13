from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
conn = sqlite3.connect('langchaiModel.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS documents (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, metadata TEXT)''')
conn.commit()

table_names = [
    'constellationstarsdata',
    'messierObjectsTable',
    'constellationsclean00',
    'allNGCobjects',
    'exoplanets',
    'largetsgalaxies'
]

# Function to convert RA and Dec strings to numerical values
def convert_ra(ra_str):
    h, m, s = map(float, ra_str.split('h|m|s'))
    return h + m/60 + s/3600

def convert_dec(dec_str):
    d, m, s = map(float, dec_str.split('°|′|″'))
    sign = -1 if "−" in dec_str else 1
    return sign * (d + m/60 + s/3600)

# Connect to SQLite database
conn = sqlite3.connect('langchaiModel.db')
c = conn.cursor()

for table in table_names:
    # Fetch RA and Dec strings from the database
    c.execute(f"SELECT ra_str, dec_str FROM {table} WHERE some_condition")
    rows = c.fetchall()

    # Loop through each row to convert RA and Dec to numerical values
    for row in rows:
        ra_str, dec_str = row
        ra_num = convert_ra(ra_str)
        dec_num = convert_dec(dec_str)
        
        # Optionally, update the database with the numerical values
        c.execute(f"UPDATE {table} SET ra_num = ?, dec_num = ? WHERE ra_str = ? AND dec_str = ?", (ra_num, dec_num, ra_str, dec_str))

# Commit changes to the database
conn.commit()


def create_table_from_rows(rows):
    table = '<table border="1">'
    for row in rows:
        table += '<tr>'
        for cell in row:
            table += f'<td>{cell}</td>'
        table += '</tr>'
    table += '</table>'
    return table



def create_table_from_rows(rows):
    table = '<table border="1">'
    for row in rows:
        table += '<tr>'
        for cell in row:
            table += f'<td>{cell}</td>'
        table += '</tr>'
    table += '</table>'
    return table

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_ra = request.form.get('ra')
        selected_dec = request.form.get('dec')
        
        c.execute(f"SELECT * FROM documents WHERE ra = ? AND dec = ?", (selected_ra, selected_dec))
        rows = c.fetchall()
        table = create_table_from_rows(rows)
    else:
        table = "Select RA and Dec to display data."
    
    return render_template('index.html', table=table)


'''
@app.route('/langchai')
def langchai():
    return render_template('langchainFlakUI.html')

@app.route('/archaeological_sites')
def archaeological_sites():
    # Your logic for archaeological sites
    archaeological_sites = {"sites": [{"Continent": "Asia", "Age": "Bronze", "Site": "Mohenjo-Daro", "Location": "Pakistan", "Year_Discovered": 1922}]}
    return render_template('archaeological_sites_template.html', archaeological_sites=archaeological_sites)

@app.route('/generate_text', methods=['POST'])
def generate_text():
    content = request.form['content']
    # Your logic for text generation
    generated_text = "Generated Text Here"

    # Save to SQLite database
    c.execute("INSERT INTO documents (content, metadata) VALUES (?, ?)", (content, generated_text))
    conn.commit()

    return render_template('langchainFlakUI.html', generated_text=generated_text)
'''




if __name__ == '__main__':
    app.run(debug=True)
