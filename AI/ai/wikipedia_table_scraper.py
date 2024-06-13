
# Import required modules
import os
import csv
from bs4 import BeautifulSoup
import requests
import webbrowser

# Initialize variables
input_file_path = 'C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\AI\\ai\\playground\\playground_data\\txt\\wikiURLSearch.txt'  # Source file for URLs
output_dir = 'C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\AI\\ai\\csv_data\\wikiData\\'  # Output directory for storing results

# Check if the output directory exists, if not, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read URLs from the input file
with open(input_file_path, 'r') as f:
    urls = f.read().splitlines()

# Create a function to scrape table data from a Wikipedia page
def scrape_wikipedia_table(url):
    # Console log: Connecting to URL
    print(f"Connecting to URL: {url}")
    
    # Fetch HTML content from the URL
    response = requests.get(url)
    html_content = response.text
    
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the first table on the Wikipedia page
    table = soup.find('table')
    
    # Initialize an empty list to store table data
    table_data = []
    
    # Iterate through each table row
    for row in table.findAll('tr'):
        row_data = []
        # Iterate through each table cell
        for cell in row.findAll(['td', 'th']):
            row_data.append(cell.get_text().strip())
        table_data.append(row_data)
    
    # Console log: Displaying table data
    print(f"Table data from {url}:")
    print(table_data[:5])  # Display first five rows
    
    # Generate output file paths
    csv_file_path = os.path.join(output_dir, f"{url.split('/')[-1]}.csv")
    html_file_path = os.path.join(output_dir, f"{url.split('/')[-1]}.html")
    
    # Write table data to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in table_data:
            csv_writer.writerow(row)
 
    # Console log: CSV file created
    print(f"CSV file created: {csv_file_path}")
    
    # Write table data to a Bootstrap 5 HTML file
    with open(html_file_path, 'w', encoding='utf-8') as htmlfile:
        # Bootstrap 5 HTML structure
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
            html_content += "<tr>"
            for cell in row:
                html_content += f"<td>{cell}</td>"
            html_content += "</tr>"
        html_content += """
                </table>
            </div>
        </body>
        </html>
        """
        htmlfile.write(html_content)
    
    # Console log: HTML file created
    print(f"HTML file created: {html_file_path}")
    
    # Open the HTML file in a web browser
    webbrowser.open(html_file_path)

    # Console log: HTML file opened in web browser
    print(f"HTML file opened in web browser: {html_file_path}")

# Iterate through each URL and scrape table data
for url in urls:
    scrape_wikipedia_table(url)

# Console log: All steps completed
print("All steps completed.")
