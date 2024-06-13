import requests
from bs4 import BeautifulSoup
import re

# Define headers to simulate a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Search items
items_to_search = [
    "Yamaha RX-V671 7.1 AV Receiver Amplifier Amp 1080p HDMI USB Zone2 CEC Dolby True",
    "KEF Speaker KEF KUBE-1 Subwoofer 200w"
]

def get_prices(item_title):
    url = f"https://www.ebay.co.uk/sch/i.html?_nkw={'+'.join(item_title.split())}&_sop=15"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    prices = []
    # Searching for the price using various possible classes and structures
    for item in soup.find_all('span', class_='s-item__price'):
        price_text = item.get_text()
        print(f"Found price text: {price_text}")  # Debugging line
        # Extract the price using regular expressions, considering different currency formats
        match = re.findall(r'[\d,]+\.\d{2}', price_text)
        if match:
            price = float(match[0].replace(',', ''))
            prices.append(price)
    
    if prices:
        min_price = min(prices)
        max_price = max(prices)
        avg_price = sum(prices) / len(prices)
        return min_price, max_price, avg_price
    else:
        return None, None, None

def main():
    for item in items_to_search:
        min_price, max_price, avg_price = get_prices(item)
        if min_price is not None:
            print(f"Item: {item}")
            print(f"Minimum Price: £{min_price:.2f}")
            print(f"Maximum Price: £{max_price:.2f}")
            print(f"Average Price: £{avg_price:.2f}")
            print('-' * 40)
        else:
            print(f"No prices found for item: {item}")
            print('-' * 40)

if __name__ == "__main__":
    main()
