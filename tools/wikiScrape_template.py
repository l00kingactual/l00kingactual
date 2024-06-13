import requests
from bs4 import BeautifulSoup

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

# Main function
def main():
    urls = read_urls_from_file("your_file.txt")  # Replace with your actual file
    for url in urls:
        print(f"Processing URL: {url}")

        # Scrape tables
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table', {'class': ['wikitable', 'sortable', 'jquery-tablesorter']})
        
        for i, table in enumerate(tables):
            table_data = process_table(table)
            if table_data:
                print(f"Successfully processed table {i+1}")
            else:
                print(f"Failed to process table {i+1}")

        # Scrape headings
        headings = scrape_headings(url)
        if headings:
            print(f"Successfully scraped headings: {headings}")
        else:
            print("Failed to scrape headings")

if __name__ == "__main__":
    main()
