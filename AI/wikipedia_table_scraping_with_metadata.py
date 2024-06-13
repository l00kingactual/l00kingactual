
import requests
from bs4 import BeautifulSoup
import csv
import os

def scrape_wikipedia_table(url):
    # Fetch HTML content from the URL
    response = requests.get(url)
    html_content = response.text
    
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the first table on the Wikipedia page
    table = soup.find('table')
    
    # Initialize an empty list to store table data
    table_data = []
    
    # Initialize a dictionary to store meta-data like description and image URL
    metadata = {}
    
    # Extract description if available
    description_tag = soup.find('p')
    if description_tag:
        metadata['Description'] = description_tag.get_text().strip()
    
    # Extract image URL if available
    image_tag = soup.find('img')
    if image_tag:
        metadata['Image_URL'] = image_tag['src']
    
    # Iterate through each table row
    if table:
        for row in table.findAll('tr'):
            row_data = []
            # Iterate through each table cell
            for cell in row.findAll(['td', 'th']):
                row_data.append(cell.get_text().strip())
            table_data.append(row_data)
    
    # Print metadata and table data (first 5 rows)
    print("Metadata:", metadata)
    print("Table Data:", table_data[:5])

# URL to scrape (replace with the actual URL)
url = "https://en.wikipedia.org/wiki/Your_Target_Page"

# Call the function to perform scraping
scrape_wikipedia_table(url)
