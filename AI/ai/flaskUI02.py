from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Read metadata from tables_list.csv using a raw string for the file path
    metadata_df = pd.read_csv(r"C:\Users\andy\OneDrive\Documents\AstroAI\ouchAstronomy\AI\ai\csv_data\tables_list.csv")

    # Read all CSV files from directory, again using a raw string for the directory path
    csv_files = []
    csv_dir = r"C:\Users\andy\OneDrive\Documents\AstroAI\ouchAstronomy\AI\ai\csv_data"
    for filename in os.listdir(csv_dir):
        if filename.endswith('.csv'):
            csv_files.append(filename)

    # Generate MySQL queries (assuming a MySQL connection object 'conn')
    mysql_queries = []
    for filename in csv_files:
        table_name = filename.replace('.csv', '')
        df = pd.read_csv(os.path.join(csv_dir, filename))
        columns = ", ".join([f"`{col}`" for col in df.columns])  # Backticks for MySQL column names
        values = ", ".join(["%s"] * len(df.columns))
        query = f"INSERT INTO `{table_name}` ({columns}) VALUES ({values});"  # Backticks for MySQL table name
        mysql_queries.append(query)

    # You can return these queries or use them further
    return render_template('index.html', queries=mysql_queries)

if __name__ == '__main__':
    app.run(debug=True)
