import requests
import csv
import logging  # Import the logging module

# Initialize logging
logging.basicConfig(level=logging.INFO)

def get_wikidata_qid(pageid, page_title):
    # Function definition here
    pass

# Rest of your code


def get_wikidata_qids(page_ids, page_titles):
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "pageids": "|".join(page_ids),
        "prop": "pageprops",
        "format": "json"
    }
    
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        qids = {}
        for pageid, page_data in data['query']['pages'].items():
            try:
                qids[pageid] = page_data['pageprops']['wikibase_item']
            except KeyError:
                # Fallback to using title if pageid fails
                title = page_titles.get(pageid, None)
                if title:
                    params["titles"] = title
                    params.pop("pageids", None)
                    response = requests.get(api_url, params=params)
                    data = response.json()
                    qids[pageid] = list(data['query']['pages'].values())[0]['pageprops']['wikibase_item']
        return qids
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return None

# Read the existing CSV file to get the pageids and titles
page_data = {}
with open('data\\wikiRAW\\wiki_pageid.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header
    for row in csvreader:
        if row and len(row) >= 5:  # Check if row is not empty and has at least 5 columns
            pageid = row[2]  # pageid is the third column
            title = row[4]  # title is the fifth column
            page_data[pageid] = title


# Batch process pageids
batch_size = 50
page_ids = list(page_data.keys())
page_titles = page_data

for i in range(0, len(page_ids), batch_size):
    batch_ids = page_ids[i:i+batch_size]
    qids = get_wikidata_qids(batch_ids, page_titles)
    
    if qids:
        with open('data\\wikiRAW\\pageid_QID_matching.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            for pageid, qid in qids.items():
                wikidata_qid_url = f"https://www.wikidata.org/wiki/{qid}"
                csvwriter.writerow([pageid, page_titles[pageid], qid, wikidata_qid_url])
    time.sleep(1)  # To avoid hitting API rate limits






# Read URLs from wikiURLSearch.txt
urls = []
with open('wikipeadia\\txt\\wikiURLSearch.txt', 'r', encoding='utf-8') as f:
    urls = f.readlines()

# Read pageid and title from wiki_data_002b.csv
page_data = {}
with open('data\\wikiRAW\\wiki_data_002b.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        if row:
            title = row[4]
            pageid = row[2]
            page_data[title] = pageid

# Generate new CSV with QIDs
output_data = []
for url in urls:
    title = url.split('/')[-1].strip()
    pageid = page_data.get(title, "N/A")
    qid = get_wikidata_qid(pageid, title)
    if qid:
        wikidata_qid_url = f"https://www.wikidata.org/wiki/{qid}"
        output_data.append([pageid, url, qid, wikidata_qid_url])

# Only write to CSV if there is data
if output_data:
    with open('data\\wikiRAW\\pageid_QID_matching.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["PageID", "PageURL", "Wikidata_QID", "WikidataQID_URL"])
        csvwriter.writerows(output_data)
else:
    logging.error("No data to write to CSV.")


# Read URLs from wikiURLSearch.txt
urls = []
with open('wikipeadia\\txt\\wikiURLSearch.txt', 'r', encoding='utf-8') as f:
    urls = f.readlines()

# Read pageid and title from wiki_data_002b.csv
page_data = {}
with open('data\\wikiRAW\\wiki_data_002b.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        if row:
            wikiURL_page = row[0]
            wikiAPI_query_fields_available = row[1]
            pageid = row[2]
            ns = row[3]
            title = row[4]
            extract = row[5]
            page_data[title] = pageid

# Generate new CSV with QIDs
with open('data\\wikiRAW\\pageid_QID_matching.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["PageID", "PageURL", "Wikidata_QID", "WikidataQID_URL"])
    
    for url in urls:
        title = url.split('/')[-1].strip()
        pageid = page_data.get(title, None)
        if pageid:
            qid = get_wikidata_qid(pageid, title)
            if qid:
                wikidata_qid_url = f"https://www.wikidata.org/wiki/{qid}"
                csvwriter.writerow([pageid, url, qid, wikidata_qid_url])
