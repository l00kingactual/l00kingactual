from bs4 import BeautifulSoup
import requests
import openpyxl
import re

# Initialize Excel workbook
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Messier Object", "Wikipedia Image URL"])

# Fetch Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_Messier_objects"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing Messier objects
table = soup.find('table', {'class': 'wikitable'})

# Loop through each row in the table
for row in table.find_all('tr')[1:]:  # Skip the header row
    cells = row.find_all('td')
    
    # Extract Messier object name
    messier_object = cells[0].text.strip()
    
    # Extract image URL
    img_tag = cells[1].find('img')
    img_url = "https:" + img_tag['src'] if img_tag else "No Image"
    
    # Append to Excel worksheet
    ws.append([messier_object, img_url])

# Save the Excel workbook
wb.save('messier_objects_with_images.xlsx')

print("Data extraction complete. Saved to messier_objects_with_images.xlsx.")
