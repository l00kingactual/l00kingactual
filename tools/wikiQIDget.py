import requests
import csv

def get_wikidata_qid(pageid, page_title):
    print(f"Attempting to fetch Wikidata QID for pageid: {pageid}")
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "pageids": pageid,
        "prop": "pageprops",
        "format": "json"
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    
    try:
        qid = data['query']['pages'][str(pageid)]['pageprops']['wikibase_item']
        print(f"Successfully fetched QID: {qid} for pageid: {pageid}")
        return qid
    except KeyError as e:
        print(f"Exception for pageid {pageid}: {e}. Attempting with page title.")
        with open('data\\wikiRAW\\exceptions.log', 'a', encoding='utf-8') as f:
            f.write(f"Exception for pageid {pageid}, URL {page_title}: {e}\n")
            f.write(f"API response: {data}\n")
        
        # Fallback to using page title if pageid fails
        params["titles"] = page_title
        params.pop("pageids", None)
        response = requests.get(api_url, params=params)
        data = response.json()
        
        try:
            qid = list(data['query']['pages'].values())[0]['pageprops']['wikibase_item']
            print(f"Successfully fetched QID: {qid} for page title: {page_title}")
            return qid
        except KeyError as e2:
            print(f"Exception for page title {page_title}: {e2}")
            with open('data\\wikiRAW\\exceptions.log', 'a', encoding='utf-8') as f:
                f.write(f"Exception for page title {page_title}: {e2}\n")
                f.write(f"API response: {data}\n")
            return None

# Read the existing CSV file to get the pageids
page_data = []
with open('data\\wikiRAW\\wiki_pageid.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header
    for row in csvreader:
        if row:  # Check if row is not empty
            pageid = row[0]  # Assuming pageid is the first column
            page_title = f"https://en.wikipedia.org/?curid={pageid}"  # Construct URL from pageid
            page_data.append((pageid, page_title))

# Create a new CSV file to store the output
with open('data\\wikiRAW\\pageid_QID_matching.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["PageID", "PageURL", "Wikidata_QID", "WikidataQID_URL"])
    
    for pageid, page_title in page_data:
        if pageid != "N/A":
            qid = get_wikidata_qid(pageid, page_title)
            if qid:
                wikidata_qid_url = f"https://www.wikidata.org/wiki/{qid}"
                csvwriter.writerow([pageid, page_title, qid, wikidata_qid_url])

