import mysql.connector

def mysql_connection():
    try:
        connection = mysql.connector.connect(
            host="213.171.200.30",
            user="OuchAstronomy",
            password="@00e54m1sf1t?",
            database="ouchAstronomy"
        )
        if connection.is_connected():
            print("MySQL connection successful.")
            return connection
    except mysql.connector.Error as e:
        print(f"MySQL connection failed. Error: {e}")
        return None

# Test MySQL connection
mysql_connection()
