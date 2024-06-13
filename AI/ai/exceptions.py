import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import webbrowser

input_file_path = 'exceptions.txt'
output_dir = 'csv_data\\wikiData\\'

if not os.path.exists(output_dir):
    print("Creating output directory...")
    os.makedirs(output_dir)

def scrape_wikipedia_table(partial_url):
    print("Step 1: Initializing function...")
    
    url = f"https://en.wikipedia.org/wiki/{partial_url}"
    print(f"Step 2: Constructed URL - {url}")
    
    print("Step 3: Sending GET request...")
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Step 4: Failed to get the page - {url}")
        return
    
    print("Step 5: Parsing HTML content...")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print("Step 6: Searching for table with class 'wikitable'...")
    table = soup.find('table', {'class': 'wikitable'})
    
    if table is None:
        print(f"Step 7: No table found on the page - {url}")
        return
    
    print("Step 8: Table found. Parsing into DataFrame...")
    df = pd.read_html(str(table))[0]
    
    print("Step 9: Displaying first 5 rows of the DataFrame:")
    print(df.head())
    
    print("Step 10: Saving DataFrame to CSV and HTML...")
    csv_file = os.path.join(output_dir, f"{partial_url.replace('/', '_').replace('#', '_').replace('?', '_')}.csv")
    html_file = os.path.join(output_dir, f"{partial_url.replace('/', '_').replace('#', '_').replace('?', '_')}.html")
    
    df.to_csv(csv_file, index=False)
    df.to_html(html_file, index=False)
    
    print(f"Step 11: Data saved to {csv_file} and {html_file}")
    
    print("Step 12: Opening HTML file in Chrome...")
    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(html_file)
    
    print("Step 13: Function execution completed.")

# Read URLs from the input file
with open(input_file_path, 'r') as f:
    print("Reading URLs from input file...")
    urls = f.read().splitlines()

# Iterate through each URL and scrape table data
for url in urls:
    scrape_wikipedia_table(url)
