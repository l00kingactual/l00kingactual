import os
import requests
import logging
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

# Initialize logging
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w')

# Function to check if a table is interesting based on its dimensions
def is_table_interesting(table):
    rows = table.find_all('tr')
    if len(rows) > 5:  # More than 5 rows
        cols = rows[0].find_all(['td', 'th'])
        if len(cols) > 2:  # More than 2 columns
            return True
    return False

# Function to scrape tables from a given URL
from io import StringIO
import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Function to determine if a table is interesting (placeholder, you can use ML here)
def is_table_interesting(table):
    """
    Determines if a table is interesting based on certain criteria.
    This is a rule-based approach and can be replaced with a machine learning model.
    
    Parameters:
        table (bs4.element.Tag): The table element from BeautifulSoup.
        
    Returns:
        bool: True if the table is interesting, False otherwise.
    """
    try:
        # Rule 1: Table should have more than 2 rows
        if len(table.find_all('tr')) <= 2:
            return False

        # Rule 2: Table should have more than 1 column
        if len(table.find_all('tr')[0].find_all('td')) <= 1:
            return False

        # Rule 3: Check for certain keywords in the table header or first row
        interesting_keywords = ['name', 'id', 'description', 'value', 'date']
        first_row_text = table.find_all('tr')[0].get_text().lower()
        if not any(keyword in first_row_text for keyword in interesting_keywords):
            return False

        # Rule 4: The table should not be a navigation or footer table (common in Wikipedia)
        if 'navbox' in table.get('class', '') or 'footer' in table.get('class', ''):
            return False

        return True

    except Exception as e:
        # Log the exception and return False
        logging.error(f"An error occurred while evaluating if the table is interesting: {e}")
        return False


# Function to scrape tables
import os
from urllib.parse import urlparse, unquote


def scrape_tables(url, output_dir):
    logging.info(f"Connecting to URL: {url}")
    print(f"Connecting to URL: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"An error occurred while fetching {url}: {e}")
        with open('exceptions.txt', 'a') as f:
            f.write(f"An error occurred while fetching {url}: {e}\n")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    logging.info(f"Found {len(tables)} tables on the page.")
    print(f"Found {len(tables)} tables on the page.")

    if not tables:
        logging.warning(f"No tables found on the webpage: {url}")
        return

    for i, table in enumerate(tables):
        if is_table_interesting(table):
            df = pd.read_html(StringIO(str(table)))[0]
            page_name = url.split('/')[-1]
            csv_file_path = os.path.join(output_dir, f"{page_name}_table_{i}.csv")
            logging.info(f"Saving table {i+1} to {csv_file_path}")
            print(f"Saving table {i+1} to {csv_file_path}")
            df.to_csv(csv_file_path, index=False)

def main():
    input_file_path = 'C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\AI\\ai\\playground\\playground_data\\txt\\wikiURLSearch.txt'
    logging.info(f"Current Working Directory: {os.getcwd()}")
    print(f"Current Working Directory: {os.getcwd()}")

    if os.path.exists(input_file_path):
        logging.info(f"The file exists at {input_file_path}")
    else:
        logging.error(f"The file does not exist at {input_file_path}")
        return

    with open(input_file_path, 'r') as f:
        urls = f.read().splitlines()
    logging.info(f"Read URLs: {urls}")
    print(f"Read URLs: {urls}")

    output_dir = 'C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\AI\\ai\\playground\\data'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for url in urls:
        logging.info(f"Processing URL: {url}")
        print(f"Processing URL: {url}")
        try:
            scrape_tables(url, output_dir)
        except Exception as e:
            logging.error(f"Error scraping tables from {url}: {e}")
            with open('exceptions.txt', 'a') as f:
                f.write(f"Error scraping tables from {url}: {e}\n")

if __name__ == '__main__':
    main()