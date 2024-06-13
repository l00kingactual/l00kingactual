# Importing MySQL Connector for MySQL database operations
import mysql.connector

# Importing py2neo for Neo4j database operations
from py2neo import Graph

# Initialize Neo4j graph and test connection
try:
    graph = Graph("bolt://brightstar:7687", auth=("neo4j", "@00e54m1sf1t?"))
    print("Neo4j connection successful.")
except Exception as e:
    print(f"Neo4j connection failed. Error: {e}")

# MySQL connection setup and test
def mysql_connection():
    try:
        connection = mysql.connector.connect(
            host="213.171.200.30",
            user="OuchAstronomy",
            password="@00e54m1sf1t?",
            database="ouchAstronomy"
        )
        print("MySQL connection successful.")
        return connection
    except Exception as e:
        print(f"MySQL connection failed. Error: {e}")
        return None

# Test MySQL connection
mysql_connection()
