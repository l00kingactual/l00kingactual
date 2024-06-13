import requests
from bs4 import BeautifulSoup
import mysql.connector

# MySQL connection setup
def mysql_connection():
    return mysql.connector.connect(
        host="213.171.200.30",
        user="OuchAstronomy",
        password="@00e54m1sf1t?",
        database="ouchAstronomy"
    )

# Function to insert data into MySQL
def insert_into_mysql(data):
    connection = mysql_connection()
    cursor = connection.cursor()
    
    sql = """INSERT INTO planets (name, description, image_url, vrml_url, wikipedia_url)
             VALUES (%s, %s, %s, %s, %s)"""
    val = (data['name'], data['description'], data['image_url'], data['vrml_url'], data['wikipedia_url'])
    
    cursor.execute(sql, val)
    connection.commit()

# Web scraping
def scrape_wikipedia():
    url = "https://en.wikipedia.org/wiki/List_of_gravitationally_rounded_objects_of_the_Solar_System"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Your scraping logic here
    # Populate the 'data' dictionary with scraped data
    data = {
        'name': 'Earth',
        'description': 'Third planet from the Sun',
        'image_url': 'https://example.com/earth.jpg',
        'vrml_url': 'https://example.com/earth.vrml',
        'wikipedia_url': 'https://en.wikipedia.org/wiki/Earth'
    }
    
    insert_into_mysql(data)

# Main function
if __name__ == "__main__":
    scrape_wikipedia()
