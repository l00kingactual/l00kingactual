from bs4 import BeautifulSoup
import requests
from pprint import pprint

class WebPageData:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.table_data = []

    def fetch(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.soup = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"An error occurred while fetching data from {self.url}: {e}")

    def process_tables(self):
        if self.soup:
            tables = self.soup.find_all('table')
            for table in tables:
                rows = table.find_all('tr')
                row_data = []
                for row in rows:
                    cells = row.find_all(['td', 'th'])
                    cell_data = [cell.get_text().strip() for cell in cells]
                    row_data.append(cell_data)
                self.table_data.append(row_data)

def read_urls_from_file(file_path):
    urls = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                urls.append(line.strip())
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return urls

def main():
    file_path = 'wikipedia\\missingDataURL.txt'
    urls = read_urls_from_file(file_path)

    for url in urls:
        webpage = WebPageData(url)
        webpage.fetch()

        if webpage.soup:
            print(f"Page Content for URL {url}:")
            print(webpage.soup.prettify())
            print("===================================")

if __name__ == "__main__":
    main()
