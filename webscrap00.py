from bs4 import BeautifulSoup
import requests
import json

def scrape_wikipedia_planet_data(planet_name):
    url = f"https://en.wikipedia.org/wiki/{planet_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract specific data here
    # For demonstration, let's say we are extracting the first paragraph
    first_paragraph = soup.find('p').text
    
    return first_paragraph

planet_data = scrape_wikipedia_planet_data("Earth")

def transform_to_json(data):
    json_data = json.dumps({"description": data})
    return json_data

json_data = transform_to_json(planet_data)
