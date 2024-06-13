import requests
import json
import csv

import requests

def get_wiki_data(url):
    # Extract the page title from the URL
    page_title = url.split('/')[-1]
    
    # Define the Wikipedia API endpoint and parameters
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": page_title,
        "prop": "extracts",
        "exintro": True
    }
    
    # Make the API request
    response = requests.get(api_url, params=params)
    data = response.json()
    
    # Extract the relevant fields
    page = next(iter(data["query"]["pages"].values()))
    pageid = page.get("pageid", "N/A")
    ns = page.get("ns", "N/A")
    title = page.get("title", "N/A")
    extract = page.get("extract", "N/A")
    
    return {
        "pageid": pageid,
        "ns": ns,
        "title": title,
        "extract": extract
    }



def get_wiki_fields(url):
    # Extract the page title from the URL
    page_title = url.split("/")[-1]
    
    # Wikipedia API endpoint
    api_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&titles={page_title}"
    
    # Make the API request
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        page_data = list(data['query']['pages'].values())[0]
        
        # Identify available fields
        available_fields = list(page_data.keys())
        
        return available_fields
    else:
        print(f"Failed to retrieve data for {url}")
        return None

# Read URLs from file
with open('wikipeadia\\txt\\wikiURLSearch.txt', 'r') as f:
    urls = f.readlines()

# Prepare CSV output
with open('data\\wikiRAW\\wiki_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['wikiURL_page', 'wikiAPI_query_fields_available', 'pageid', 'ns', 'title', 'extract']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    # Loop through each URL to get available fields and their values
    for url in urls:
        url = url.strip()
        available_fields = get_wiki_fields(url)
        
        if available_fields:
            # Assuming you have a function get_wiki_data that returns a dictionary with the fields
            wiki_data = get_wiki_data(url)
            
            writer.writerow({
                'wikiURL_page': url, 
                'wikiAPI_query_fields_available': ', '.join(available_fields),
                'pageid': wiki_data.get('pageid', 'N/A'),
                'ns': wiki_data.get('ns', 'N/A'),
                'title': wiki_data.get('title', 'N/A'),
                'extract': wiki_data.get('extract', 'N/A')
            })

print("CSV file has been written.")
