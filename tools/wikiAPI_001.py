import requests
import pandas as pd

# Initialize an empty list to store the data
data_list = []

# Read the Wikipedia URLs from the file
with open("wikipeadia\\txt\\wikiURLSearch.txt", "r") as file:
    urls = file.readlines()

# Loop through each URL to fetch data
for url in urls:
    page_title = url.split("/")[-1].strip()  # Extract the page title from the URL
    params = {
        "action": "query",
        "format": "json",
        "titles": page_title,
        "prop": "extracts",
        "exintro": True
    }
    response = requests.get("https://en.wikipedia.org/w/api.php", params=params)
    json_data = response.json()
    page_data = json_data["query"]["pages"]
    for page_id, content in page_data.items():
        title = content.get("title", "N/A")
        extract = content.get("extract", "N/A")  # Use .get() to avoid KeyError
        data_list.append({"title": title, "extract": extract})

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data_list)

# Save the DataFrame to a CSV file
df.to_csv("data\\wikiRAW\\wiki_data.csv", index=False)
