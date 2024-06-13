import requests
import csv

def get_wiki_data_by_pageid(pageid):
    try:
        api_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "pageids": pageid,
            "format": "json",
            "prop": "pageprops"
        }
        response = requests.get(api_url, params=params)
        data = response.json()
        
        if 'query' in data and 'pages' in data['query']:
            page_data = data['query']['pages'][str(pageid)]
            wikidata_qid = page_data['pageprops'].get('wikibase_item', 'N/A')
            return wikidata_qid
        else:
            print(f"No 'query' or 'pages' field in the response for pageid: {pageid}")
            return 'N/A'
    except Exception as e:
        print(f"Exception occurred: {e}")
        with open('data\\wikiRAW\\exceptions.log', 'a') as f:
            f.write(f"Exception for pageid {pageid}: {e}\n")
        return 'N/A'

# Read the existing CSV file to get the pageids
pageids = []
with open('data\\wikiRAW\\wiki_pageid.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header
    for row in csvreader:
        pageids.append(row[0])  # Assuming pageid is the first column

# Create a new CSV file to store the output
with open('data\\wikiRAW\\pageid_matching.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["page_pageid", "Wikidata_QID"])
    
    for pageid in pageids:
        print(f"Fetching data for pageid: {pageid}")
        wikidata_qid = get_wiki_data_by_pageid(pageid)
        csvwriter.writerow([pageid, wikidata_qid])
