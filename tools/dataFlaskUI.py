from flask import Flask, render_template, jsonify
import MySQLdb
import pandas as pd

# Import database credentials
from mysql_credentials import db_config

# import Time
import Time_utility
import astro_object



def get_unique_fields(table_names):
    db = MySQLdb.connect(host=db_config['host'], 
                         user=db_config['user'], 
                         passwd=db_config['password'], 
                         db=db_config['database'])
    cursor = db.cursor()
    unique_fields = set()
    
    for table in table_names:
        query = f"SHOW COLUMNS FROM {table}"
        cursor.execute(query)
        fields = cursor.fetchall()
        for field in fields:
            unique_fields.add(field[0])
            
    cursor.close()
    db.close()
    
    return list(unique_fields)

def convert_to_decimal(coord, coord_type):
    """
    Converts DMS (Degrees, Minutes, Seconds) or HMS (Hours, Minutes, Seconds) to decimal.
    
    Parameters:
        coord (str): The coordinate in DMS or HMS format.
        coord_type (str): Either 'Dec' for Declination or 'RA' for Right Ascension.
        
    Returns:
        float: The coordinate in decimal format.
    """
    elements = coord.split()
    
    if coord_type == 'Dec':
        degrees = float(elements[0])
        minutes = float(elements[1])
        seconds = float(elements[2])
        milliseconds = float(elements[3])
        decimal_value = degrees + (minutes / 60) + (seconds / 3600) + (milliseconds / 3600000)
        
    elif coord_type == 'RA':
        hours = float(elements[0][:-1])  # Remove 'h'
        minutes = float(elements[1][:-1])  # Remove 'm'
        seconds = float(elements[2])
        milliseconds = float(elements[3][:-1])  # Remove 's'
        decimal_value = 15 * (hours + (minutes / 60) + (seconds / 3600) + (milliseconds / 3600000))
        
    else:
        raise ValueError("Invalid coordinate type. Use 'Dec' for Declination or 'RA' for Right Ascension.")
        
    return decimal_value

def convert_to_dms_hms(decimal_value, coord_type):
    """
    Converts a decimal coordinate to DMS (Degrees, Minutes, Seconds) or HMS (Hours, Minutes, Seconds) format.
    
    Parameters:
        decimal_value (float): The coordinate in decimal format.
        coord_type (str): Either 'Dec' for Declination or 'RA' for Right Ascension.
        
    Returns:
        str: The coordinate in DMS or HMS format.
    """
    if coord_type == 'Dec':
        degrees = int(decimal_value)
        minutes = int((decimal_value - degrees) * 60)
        seconds = int((decimal_value - degrees - minutes / 60) * 3600)
        milliseconds = int((decimal_value - degrees - minutes / 60 - seconds / 3600) * 3600000)
        return f"{degrees} {minutes} {seconds} {milliseconds}"
        
    elif coord_type == 'RA':
        decimal_value /= 15  # Convert back to hours
        hours = int(decimal_value)
        minutes = int((decimal_value - hours) * 60)
        seconds = int((decimal_value - hours - minutes / 60) * 3600)
        milliseconds = int((decimal_value - hours - minutes / 60 - seconds / 3600) * 3600000)
        return f"{hours}h {minutes}m {seconds} {milliseconds}s"
        
    else:
        raise ValueError("Invalid coordinate type. Use 'Dec' for Declination or 'RA' for Right Ascension.")




app = Flask(__name__)

from flask import Flask, render_template, request, jsonify
import MySQLdb
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import meta_data
# Import database credentials from mysql_credentials.py
from mysql_credentials import db_config

# Initialize Flask and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
db = SQLAlchemy(app)

# Define AstroObject model
class AstroObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    distance_in_light_years = db.Column(db.Float)
    time_dec = db.Column(db.Float)
    time_ra = db.Column(db.Float)
    gravity = db.Column(db.Float)

# Initialize time index
time_index = {
    'Dec': 0,
    'RA': 0
}

@app.route('/')
def index():
    

    return render_template('index.html', metadata=meta_data, time_index=time_index)

@app.route('/astro_objects', methods=['POST'])
def create_astro_object():
    data = request.get_json()
    new_object = AstroObject(
        name=data['name'],
        distance_in_light_years=data['distance_in_light_years'],
        time_dec=data['time_dec'],
        time_ra=data['time_ra'],
        gravity=data['gravity']
    )
    db.session.add(new_object)
    db.session.commit()
    return jsonify({'message': 'New object created'}), 201







if __name__ == '__main__':
    app.run(debug=True)
