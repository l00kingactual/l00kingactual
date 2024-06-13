import os
import csv
from bs4 import BeautifulSoup
import requests
import webbrowser

input_file_path = 'C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\AI\\ai\\playground\\playground_data\\txt\\wikiURLSearch.txt'
output_dir = 'C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\AI\\ai\\csv_data\\wikiData\\'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(input_file_path, 'r') as f:
    urls = f.read().splitlines()

def scrape_wikipedia_table(url):
    print(f"Connecting to URL: {url}")
    
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    tables = soup.find_all('table')
    
    if tables:
        for i, table in enumerate(tables):
            table_data = []
            for row in table.find_all('tr'):
                row_data = [cell.get_text().strip() for cell in row.find_all(['td', 'th'])]
                table_data.append(row_data)
            
            print(f"Table {i+1} data from {url}:")
            print(table_data[:5])
            
            csv_file_path = os.path.join(output_dir, f"{url.split('/')[-1]}_table_{i}.csv")
            html_file_path = os.path.join(output_dir, f"{url.split('/')[-1]}_table_{i}.html")
            
            with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(table_data)
            
            print(f"CSV file created: {csv_file_path}")
            
            with open(html_file_path, 'w', encoding='utf-8') as htmlfile:
                html_content = """
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Table Data</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet">
                </head>
                <body>
                    <div class="container mt-5">
                        <table class="table table-bordered">
                """
                for row in table_data:
                    html_content += "<tr>" + "".join([f"<td>{cell}</td>" for cell in row]) + "</tr>"
                html_content += """
                        </table>
                    </div>
                </body>
                </html>
                """
                htmlfile.write(html_content)
            
            print(f"HTML file created: {html_file_path}")
            webbrowser.open(html_file_path)
    else:
        print(f"No tables found on {url}")

for url in urls:
    scrape_wikipedia_table(url)

print("All steps completed.")
