from collections import defaultdict
import requests
from bs4 import BeautifulSoup
import csv

def fetch_data():
    urls = [
        'https://en.wikipedia.org/wiki/List_of_archaeological_sites_by_continent_and_age',
        'https://en.wikipedia.org/wiki/List_of_paleocontinents',
        'https://en.wikipedia.org/wiki/Category:Historical_continents'
    ]
    
    historical_continents = []
    
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        if 'Category:Historical_continents' in url:
            div_content = soup.find('div', {'id': 'mw-content-text'})
            links = div_content.find_all('a')
            for link in links:
                if 'title' in link.attrs:
                    # Note the use of 'utf-8' encoding
                    historical_continents.append(link['title'].replace(" ", "_").replace("/", "_").replace(":", "").encode('utf-8').decode())
                    
    # Write the list to a CSV file
    with open('wikipeadia\\historical_continents.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Historical_Continents'])  # Header row
        for continent in historical_continents:
            writer.writerow([continent])

if __name__ == "__main__":
    fetch_data()
