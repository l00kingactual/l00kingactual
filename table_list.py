import os
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import logging
# MySQL Database Details
def Credentials():
    host = "213.171.200.30"
    user = "OuchAstronomy"
    password = "@00E54m1sf1t?"
    database = "ouchAstronomy"
def connect_to_mysql(Credentials):
    try:
        engine = create_engine(f"mysql+mysqlconnector://{Credentials}:{Credentials}@{Credentials}/{Credentials}")
        print(f"Successfully connected to MySQL database {Credentials}")
        logging.info(f"Successfully connected to MySQL database {Credentials}")
        return engine
    except Exception as e:
        print(f"An error occurred while connecting to MySQL: {str(e)}")
        logging.error(f"An error occurred while connecting to MySQL: {str(e)}")
        return None

def create_mysql_table_from_csv(engine, csv_file_path, table_name):
    try:
        df = pd.read_csv(csv_file_path)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Successfully created table {table_name}")
        logging.info(f"Successfully created table {table_name}")
        return True
    except Exception as e:
        print(f"An error occurred while creating table {table_name}: {str(e)}")
        logging.error(f"An error occurred while creating table {table_name}: {str(e)}")
        return False

        if connection.is_connected():
            print(f"Successfully connected to MySQL database {database_name}")

            # Create a new cursor object
            cursor = connection.cursor()

            # Execute the table creation query
            cursor.execute(table_creation_query)

            print(f"Table created successfully in MySQL database {database_name}")

import csv
from mysql.connector import Error, errorcode
import mysql.connector

def create_table(database_name, table_creation_query, table_id, table_name, fields):
    connection = None
    cursor = None
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database=database_name,
            port=3306  # Ensure this is an integer
        )
        
        if connection.is_connected():
            print(f"Successfully connected to MySQL database {database_name}")

            # Create a new cursor object
            cursor = connection.cursor()

            # Execute the table creation query
            cursor.execute(table_creation_query)

            print(f"Table created successfully in MySQL database {database_name}")

            # Write to CSV
            with open('tables_list.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([table_id, table_name, fields])

    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied: Incorrect username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"Database {database_name} does not exist")
        elif err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists")
        else:
            print(f"An error occurred: {err}")
    finally:
        # Close the cursor and connection
        if cursor is not None and cursor.is_connected():
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print(f"MySQL connection to {database_name} is closed")

# Example usage
database_name = "ouchAstronomy"
table_creation_query = """
CREATE TABLE Asteroid_dataset_cleaned (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    diameter FLOAT NOT NULL
);
"""
table_id = 1
table_name = "Asteroid_dataset_cleaned"
fields = "id, name, diameter"

# Initialize CSV file with headers
with open('tables_list.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Table Name', 'Fields'])

create_table(database_name, table_creation_query, table_id, table_name, fields)
