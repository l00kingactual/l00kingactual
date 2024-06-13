import requests
from bs4 import BeautifulSoup
import os
import csv
import webbrowser

# Initialize variables
input_file_path = 'data/wikiURLSearch.txt'  # Source file for URLs
exception_file_path = 'data/exceptions.txt'  # Source file for exception URLs
output_dir = 'data/wikiData/'  # Output directory for storing results
exception_dir = 'data/exceptions/'  # Directory for storing exception HTMLs

# Check if the output and exception directories exist; if not, create them
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
if not os.path.exists(exception_dir):
    os.makedirs(exception_dir)

# Read URLs from the input and exception files
with open(input_file_path, 'r') as f:
    urls = f.read().splitlines()
with open(exception_file_path, 'r') as f:
    exception_urls = f.read().splitlines()

# Compile a new list of target URLs
target_urls = list(set(urls) - set(exception_urls))

# List to keep track of URLs where scraping failed or no table was found
failed_urls = []

# Function to scrape Wikipedia tables
def scrape_wikipedia_table(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table')
            if table:
                # Logic to scrape table goes here
                # ...
                print(f"Table found for URL: {url}")
            else:
                print(f"No table found for URL: {url}")
                failed_urls.append(url)
                # Logic to save entire HTML page for review goes here
                # ...
        else:
            print(f"Failed to fetch URL: {url}, Status Code: {response.status_code}")
            failed_urls.append(url)
    except Exception as e:
        print(f"An error occurred while processing URL: {url}, Error: {e}")

# Iterate through each URL and scrape table data
for url in target_urls:
    scrape_wikipedia_table(url)

# Write failed URLs to a file
with open('data/failed_urls.txt', 'w') as f:
    for url in failed_urls:
        f.write(f"{url}\n")
