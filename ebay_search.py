import json
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

# eBay API credentials
app_id = 'YOUR_APP_ID'  # Replace with your actual eBay App ID

# Search items
items_to_search = [
    "Yamaha RX-V671 7.1 AV Receiver Amplifier Amp 1080p HDMI USB Zone2 CEC Dolby True",
    "KEF Speaker KEF KUBE-1 Subwoofer 200w"
]

def get_prices(item_title):
    try:
        api = Finding(appid=app_id, config_file=None)
        response = api.execute('findItemsByKeywords', {
            'keywords': item_title,
            'sortOrder': 'PricePlusShippingLowest'
        })
        
        prices = []
        items = response.reply.searchResult.item
        for item in items:
            price = float(item.sellingStatus.currentPrice.value)
            prices.append(price)
        
        if prices:
            min_price = min(prices)
            max_price = max(prices)
            avg_price = sum(prices) / len(prices)
            return min_price, max_price, avg_price
        else:
            return None, None, None
    except ConnectionError as e:
        print(f"Error: {e}")
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
