import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import os

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to read URLs from a text file
def read_urls_from_file(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Function to scrape tables from a URL
def scrape_tables(url, output_dir):
    logging.info(f"Visiting URL: {url}")
    response = requests.get(url)
    
    if response.status_code != 200:
        logging.error(f"Failed to retrieve the webpage: {url}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    
    if not tables:
        logging.warning(f"No tables found on the webpage: {url}")
        return
    
    for i, table in enumerate(tables):
        df = pd.read_html(str(table))[0]
        csv_file_path = os.path.join(output_dir, f"{url.split('/')[-1]}_table_{i}.csv")
        logging.info(f"Saving table {i+1} to {csv_file_path}")
        df.to_csv(csv_file_path, index=False)

# Main function
def main():
    # Read URLs from text files
    wiki_urls = read_urls_from_file("C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\AI\\ai\\playground\\playground_data\\txt\\wikiURLSearch.txt")
    exception_urls = read_urls_from_file("C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\AI\\ai\\playground\\playground_data\\txt\\exceptions.txt")
    
    # Output directory
    output_dir = "C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\AI\\ai\\playground\\data"
    
    # Scrape tables from wiki URLs
    for url in wiki_urls:
        scrape_tables(url, output_dir)
    
    # Scrape tables from exception URLs
    for url in exception_urls:
        scrape_tables(url, output_dir)

if __name__ == "__main__":
    main()
