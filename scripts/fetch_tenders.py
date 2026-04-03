import requests
from bs4 import BeautifulSoup

url = "https://ted.europa.eu/TED/search/searchResult.do?format=rss&page=1&scope=3&country=IT"

response = requests.get(url)
soup = BeautifulSoup(response.content, "xml")

items = soup.find_all("item")

tenders = []

for item in items:
    title = item.title.text if item.title else ""
    link = item.link.text if item.link else ""

    tenders.append({
        "title": title,
        "link": link
    })

print(f"Saved {len(tenders)} tenders")
