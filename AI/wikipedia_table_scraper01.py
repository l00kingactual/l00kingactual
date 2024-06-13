import os
import csv
import requests
from bs4 import BeautifulSoup
import webbrowser

# Initialize variables
input_file_path = 'data/wikiURLSearch.txt'
output_dir = 'data/wikiData/'
no_data_urls = []

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read URLs from the file
with open(input_file_path, 'r') as f:
    urls = f.read().splitlines()

def scrape_wikipedia_table(url):
    print(f"Connecting to URL: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table')
        if table is not None:
            table_data = []
            for row in table.findAll('tr'):
                row_data = []
                for cell in row.findAll(['td', 'th']):
                    row_data.append(cell.get_text().strip())
                table_data.append(row_data)
            
            csv_file_path = os.path.join(output_dir, f"{url.split('/')[-1]}.csv")
            html_file_path = os.path.join(output_dir, f"{url.split('/')[-1]}.html")
            
            with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                for row in table_data:
                    csv_writer.writerow(row)
            
            with open(html_file_path, 'w', encoding='utf-8') as htmlfile:
                html_content = """<!DOCTYPE html><html><head><title>Table Data</title></head><body><table>"""
                for row in table_data:
                    html_content += "<tr>" + "".join([f"<td>{cell}</td>" for cell in row]) + "</tr>"
                html_content += "</table></body></html>"
                htmlfile.write(html_content)
            
            webbrowser.open(html_file_path)
            print(f"HTML file opened in web browser: {html_file_path}")
        else:
            print(f"No table found on {url}")
            no_data_urls.append(url)
    else:
        print(f"Failed to fetch URL: {url}, Status Code: {response.status_code}")
        no_data_urls.append(url)

# Iterate through each URL and scrape table data
for url in urls:
    scrape_wikipedia_table(url)

print("All steps completed.")
print(f"URLs with no table data or fetch failures: {no_data_urls}")
