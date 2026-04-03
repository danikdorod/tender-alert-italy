import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

URL = "https://ted.europa.eu/TED/rss_en.xml"

response = requests.get(URL)

if response.status_code != 200:
    print("Error fetching RSS")
    exit(1)

# 🔥 PARSE WITH TOLERANT PARSER
soup = BeautifulSoup(response.content, "xml")

items = soup.find_all("item")

tenders = []

for item in items[:30]:
    title = item.title.text if item.title else ""
    link = item.link.text if item.link else ""
    pub_date = item.pubDate.text if item.pubDate else ""

    # 🔍 FILTER (basic, we improve later)
    keywords = ["software", "it", "digital", "system"]

    if any(k in title.lower() for k in keywords):
        tenders.append({
            "title": title,
            "link": link,
            "date": pub_date,
            "fetched_at": datetime.now().isoformat()
        })

# Ensure folder exists
os.makedirs("data", exist_ok=True)

with open("data/tenders.json", "w", encoding="utf-8") as f:
    json.dump(tenders, f, indent=2, ensure_ascii=False)

print(f"Saved {len(tenders)} tenders")
