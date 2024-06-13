import requests
from bs4 import BeautifulSoup
from pprint import pprint


class WebPageData:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.table_data = []

    def fetch(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.content, 'html.parser')
        else:
            print(f"Failed to retrieve {self.url}")

# create the definition for scrapping headings h1-h4 from wikipeadia urls

def process_table(table):
    try:
        rows = table.find_all('tr')
        headers = [header.text.strip() for header in rows[0].find_all('th')]
        table_data = []

        for row in rows[1:]:
            cells = row.find_all('td')
            if len(cells) == len(headers):  # Error-checking for IndexError
                row_data = {headers[i]: cells[i].text.strip() for i in range(len(cells))}
                table_data.append(row_data)

        return table_data
    except Exception as e:
        print(f"An exception occurred in process_table: {e}")
        return None

def read_urls_from_file(file_path):
    urls = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                urls.append(line.strip())
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return urls

def scrape_headings(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to get content from {url}, status code: {response.status_code}")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        headings = {}
        for tag in soup.find_all(['h1', 'h2', 'h3', 'h4']):
            headings[tag.name] = tag.text.strip()

        return headings
    except Exception as e:
        print(f"An exception occurred in scrape_headings: {e}")
        return None

def main():
    file_path = 'wikipeadia\\txt\\wikiURLSearch.txt'
    missing_data_file_path = 'wikipeadia\\txt\\missingDataURL.txt'
    
    urls = read_urls_from_file(file_path)
    print(f"Read {len(urls)} URLs from file.")

    missing_data_urls = []

    for url in urls:
        print(f"Processing URL: {url}")
        webpage = WebPageData(url)
        webpage.fetch()
        
        if webpage.soup:
            print("Fetched webpage content.")
            # Assuming you want to add a process_tables method to WebPageData class
            # webpage.process_tables()
            webpage.table_data = process_table(webpage.soup.find('table'))
            
            if not webpage.table_data:
                print(f"No table data found for URL: {url}")
                missing_data_urls.append(url)
                continue

            print(f"Data for URL {url} (first 5 rows of each table)")
            pprint(webpage.table_data[:5])
        else:
            print(f"Failed to fetch webpage content for URL: {url}")
            missing_data_urls.append(url)

    if missing_data_urls:
        print(f"Writing missing data URLs to {missing_data_file_path}.")
        with open(missing_data_file_path, 'w') as file:
            for url in missing_data_urls:
                file.write(f"{url}\n")

if __name__ == "__main__":
    main()
