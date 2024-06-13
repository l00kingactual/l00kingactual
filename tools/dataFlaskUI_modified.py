
from flask import Flask, render_template, jsonify, request, send_file
import MySQLdb
import pandas as pd
import io

# Import database credentials
from mysql_credentials import db_config

# Import Time utility and astro object
import Time_utility
import astro_object

# Existing functions like get_unique_fields() and convert_to_decimal() here

# AI Query Parser function (as implemented before)
def ai_query_parser_extended(user_query, table_names):
    # Implementation here

# Initialize Flask app
app = Flask(__name__)

@app.route('/ai_query', methods=['POST'])
def ai_query():
    user_query = request.form['user_query']
    table_names = ['constellationstarsdata', 'messierObjectsTable', 'constellationsclean00', 'allNGCobjects']  # This can be dynamic
    sql_query = ai_query_parser_extended(user_query, table_names)
    
    if sql_query:
        db = MySQLdb.connect(host=db_config['host'], 
                             user=db_config['user'], 
                             passwd=db_config['password'], 
                             db=db_config['database'])
        cursor = db.cursor()
        cursor.execute(sql_query)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        
        # Convert the fetched data to a pandas DataFrame for easier manipulation
        df = pd.DataFrame(data, columns=['RA', 'Dec'])  # Column names may vary based on your database schema
        
        # Sort the data by RA and Dec
        df_sorted = df.sort_values(by=['RA', 'Dec'])
        
        # Data can be displayed here or returned for the frontend to handle
        return render_template('index.html', table=df_sorted.to_html(classes='data'))
    else:
        return jsonify({'error': 'Invalid query'})

@app.route('/download', methods=['GET'])
def download():
    # Generate a CSV file from the DataFrame (df_sorted)
    buffer = io.StringIO()
    df_sorted.to_csv(buffer, index=False)
    buffer.seek(0)
    
    # Make the CSV file available for download
    return send_file(buffer, as_attachment=True, download_name='sorted_data.csv', mimetype='text/csv')

if __name__ == '__main__':
    app.run(debug=True)
