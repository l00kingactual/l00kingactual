import requests

def fetch_wikipedia_page(title):
    url = f"https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "format": "json",
        "titles": title
    }
    response = requests.get(url, params=params)
    data = response.json()
    page = next(iter(data["query"]["pages"].values()))
    content = page["revisions"][0]["*"]
    return content

if __name__ == "__main__":
    title = "Python_(programming_language)"
    content = fetch_wikipedia_page(title)
    print(content[:500])  # Print first 500 characters of the content
