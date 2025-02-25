import requests
from bs4 import BeautifulSoup

def get_competitor_price(url: str):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch data"}

    soup = BeautifulSoup(response.text, "lxml")

    # eBay product price extraction
    price_tag = soup.find("span", {"class": "s-item__price"})

    if price_tag:
        return {"price": price_tag.text.strip()}
    else:
        return {"error": "Price not found"}

import requests
from bs4 import BeautifulSoup

def search_competitors(query: str):
    """
    Searches eBay for a product and extracts competitor prices directly.
    Returns a list of competitor prices only.
    """
    url = f"https://www.ebay.com/sch/i.html?_nkw={query.replace(' ', '+')}"
    print(url)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch search results"}

    soup = BeautifulSoup(response.text, "lxml")

    # Extract all prices directly
    competitors = []
    for price_tag in soup.find_all("span", {"class": "s-item__price"}, limit=1000):
        print(price_tag.text)
        cleaned_price = price_tag.text.replace("$","").replace(",", "").strip()
        print(cleaned_price)

        try:
            price = float(cleaned_price)
            competitors.append(price)  # Store only the price
        except ValueError:
            continue  # Skip if price can't be converted

    return competitors[2:]
