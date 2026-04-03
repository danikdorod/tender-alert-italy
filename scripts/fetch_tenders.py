import requests
import xml.etree.ElementTree as ET
import json
from datetime import datetime

# TED RSS feed (Italy + IT services)
URL = "https://ted.europa.eu/TED/rss_en.xml"

response = requests.get(URL)

if response.status_code != 200:
    print("Error fetching RSS")
    exit(1)

root = ET.fromstring(response.content)

tenders = []

for item in root.findall(".//item")[:20]:
    title = item.find("title").text if item.find("title") is not None else ""
    link = item.find("link").text if item.find("link") is not None else ""
    pub_date = item.find("pubDate").text if item.find("pubDate") is not None else ""

    # SIMPLE FILTER (Italy + IT keywords)
    if "Italy" in title or "IT" in title or "software" in title.lower():
        tenders.append({
            "title": title,
            "link": link,
            "date": pub_date,
            "fetched_at": datetime.now().isoformat()
        })

# Save
with open("data/tenders.json", "w", encoding="utf-8") as f:
    json.dump(tenders, f, indent=2, ensure_ascii=False)

print(f"Saved {len(tenders)} tenders")
