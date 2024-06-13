import json
import pymysql
import math
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection
def connect_to_db():
    logging.info("Connecting to the database.")
    return pymysql.connect(
        host='213.171.200.30',
        user='OuchAstronomy',
        password='@00E54m1sf1t?',
        database='ouchAstronomy'
    )

# Load JSON data
logging.info("Loading JSON data.")
with open(r"C:\Users\andy\OneDrive\Documents\AstroAI\ouchAstronomy\AI\ai\csv_data_json.json", "r") as f:
    data_object = json.load(f)

# Connect to MySQL database
conn = connect_to_db()
cursor = conn.cursor()

# Iterate through each table and populate it
for table, info in data_object.items():
    logging.info(f"Processing table: {table}")

    # Truncate the table
    try:
        cursor.execute(f"TRUNCATE TABLE `{table}`")
        logging.info(f"Truncated table: {table}")
    except Exception as e:
        logging.error(f"An error occurred while truncating {table}: {e}")

    headers = info['headers']
    data = info['data']

    # Create the SQL query string
    columns_str = ", ".join([f"`{header}`" for header in headers])  # Enclose column names in backticks
    values_str = ", ".join(["%s"] * len(headers))
    sql_query = f"INSERT INTO `{table}` ({columns_str}) VALUES ({values_str})"

    logging.info(f"SQL Query: {sql_query}")  # Log the SQL query

    # Execute the SQL query for each row
    for row in data:
        # Replace 'nan' or NaN with None (which translates to NULL in MySQL)
        row = [None if (isinstance(x, float) and math.isnan(x)) or x == 'nan' else x for x in row]

    try:
        logging.info(f"Row Data: {row}")  # Log the row data
        cursor.execute(sql_query, row)
    except Exception as e:
        logging.error(f"An error occurred while inserting data into {table}: {e}")

        try:
            cursor.execute(sql_query, row)
        except Exception as e:
            logging.error(f"An error occurred while inserting data into {table}: {e}")

    # Commit changes
    logging.info(f"Committing changes for table: {table}")
    conn.commit()

# Close the cursor and connection
logging.info("Closing the cursor and database connection.")
cursor.close()
conn.close()
