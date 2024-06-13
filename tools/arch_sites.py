from bs4 import BeautifulSoup
import requests
import archaeological_sites_prep

import requests
from bs4 import BeautifulSoup

class ArchaeologicalSites:
    def __init__(self):
        self.data = {}
    
    def fetch_data(self):
        url = 'https://en.wikipedia.org/wiki/List_of_archaeological_sites_by_continent_and_age'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        data = {}
        current_h2 = None
        current_h3 = None
        current_h4 = None

        for tag in soup.find_all(['h2', 'h3', 'h4', 'ul']):
            if tag.name == 'h2':
                current_h2 = tag.text.strip()
                data[current_h2] = {}
            elif tag.name == 'h3':
                current_h3 = tag.text.strip()
                data[current_h2][current_h3] = {}
            elif tag.name == 'h4':
                current_h4 = tag.text.strip()
                data[current_h2][current_h3][current_h4] = []
            elif tag.name == 'ul':
                list_data = []
                for li_tag in tag.find_all('li'):
                    list_data.append(li_tag.text.strip())
                
                if current_h4:
                    data[current_h2][current_h3][current_h4] = list_data
                elif current_h3:
                    data[current_h2][current_h3] = list_data
                else:
                    data[current_h2] = list_data

        self.data = data

    def debug_data_structure(self):
        print(f"Data: {self.data}")

# Create an instance of the class
archaeological_sites_prep = ArchaeologicalSites()

# Fetch the data
archaeological_sites_prep.fetch_data()

# Debug to see if data is loaded correctly
archaeological_sites_prep.debug_data_structure()



def read_and_parse_html(file_path):
    with open(file_path, 'rb') as f:
        html_content_bytes = f.read()
    html_content = html_content_bytes.decode('utf-8', errors='ignore')
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup


def populate_archaeological_sites(soup):
    continents = []
    
    current_continent = None
    current_age = None
    
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'ul']):
        if tag.name == 'h1':
            if current_continent:
                continents.append(current_continent)
            current_continent = archaeological_sites_prep.Continent(tag.text.strip(), [])
            current_age = None
            
        elif tag.name in ['h2', 'h3', 'h4']:
            if current_age:
                current_continent.add_age(current_age)
            current_age = archaeological_sites_prep.Age(tag.text.strip(), [])
        
        elif tag.name == 'ul':
            sites = [li.text.strip() for li in tag.find_all('li')]
            current_age.sites = sites
    
    if current_age:
        current_continent.add_age(current_age)
    if current_continent:
        continents.append(current_continent)
    
    arch_sites = archaeological_sites_prep.ArchaeologicalSites(continents)
    return arch_sites

# Step 1: Read and parse the HTML
soup = read_and_parse_html('arch_sites.html')

# Step 2: Populate the ArchaeologicalSites instance with data from the HTML
archaeological_sites_prep = populate_archaeological_sites(soup)

# Step 3: (Optional) Debug to see if data is loaded correctly
archaeological_sites_prep.debug_data_structure()
