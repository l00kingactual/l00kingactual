import requests
from bs4 import BeautifulSoup
import mysql.connector
import json

# 1. Connect to the MySQL database and test the connection
try:
    conn = mysql.connector.connect(
        host="213.171.200.30",
        user="OuchAstronomy",
        password="@00e54m1sf1t?",
        database="ouchAstronomy"
    )
    cursor = conn.cursor()
    print("Database connection established.")
except Exception as e:
    print(f"Database connection failed: {e}")

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS planets
                  (name VARCHAR(50) PRIMARY KEY, data JSON)''')

# 2. Build a dictionary of planets including Pluto
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

# 3. For each planet, connect to Wikipedia and get the infobox data
for planet in planet_names:
    url = f"https://en.wikipedia.org/wiki/{planet}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Successfully fetched data for {planet}.")
        soup = BeautifulSoup(response.text, 'html.parser')
        infobox = soup.find('table', {'class': 'infobox'})
        
        # Check if infobox exists
        if infobox:
            # Extracting all available data from the infobox
            planet_data = {}
            for row in infobox.find_all('tr'):
                header = row.find('th')
                value = row.find('td')
                if header and value:
                    planet_data[header.text.strip()] = value.text.strip()
            
            # Update the MySQL database with the data
            cursor.execute("INSERT INTO planets (name, data) VALUES (%s, %s) ON DUPLICATE KEY UPDATE data = %s", (planet, json.dumps(planet_data), json.dumps(planet_data)))
            conn.commit()
            
            print(f"Database updated for {planet}.")
            print(f"Infobox data: {planet_data}")
        else:
            print(f"No infobox found for {planet}.")
    else:
        print(f"Failed to fetch data for {planet}.")

# Close the MySQL database connection
conn.close()
