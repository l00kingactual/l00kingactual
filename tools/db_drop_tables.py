import json
import pymysql
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Load MySQL credentials from JSON file
try:
    with open('json\\mysql_credentials.json', 'r') as f:
        credentials = json.load(f)
except Exception as e:
    logging.error(f"Failed to load credentials: {e}")
    exit(1)

# Connect to MySQL database
try:
    connection = pymysql.connect(
        host=credentials['host'],
        user=credentials['user'],
        password=credentials['passwd'],
        database=credentials['db']
    )
except Exception as e:
    logging.error(f"Failed to connect to database: {e}")
    exit(1)

# Drop all tables
try:
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for table in tables:
            table_name = table[0]
            logging.info(f"Attempting to drop table {table_name}")
            cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    connection.commit()
except Exception as e:
    logging.error(f"An error occurred while dropping tables: {e}")
finally:
    connection.close()


logging.info("Successfully dropped all tables.")
