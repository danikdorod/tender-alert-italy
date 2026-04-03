import requests
import xml.etree.ElementTree as ET
import json
import re
from datetime import datetime

URL = "https://ted.europa.eu/TED/rss_en.xml"

response = requests.get(URL)

if response.status_code != 200:
    print("Error fetching RSS")
    exit(1)

clean_xml = re.sub(r"[^\x09\x0A\x0D\x20-\x7F]+", "", response.text)

try:
    root = ET.fromstring(clean_xml)
except Exception as e:
    print("XML parsing failed:", e)
    exit(1)

tenders = []

for item in root.findall(".//item")[:30]:
    title = item.find("title").text if item.find("title") is not None else ""
    link = item.find("link").text if item.find("link") is not None else ""
    pub_date = item.find("pubDate").text if item.find("pubDate") is not None else ""

    # 🔍 BASIC FILTER (we improve later)
    if any(keyword in title.lower() for keyword in ["software", "it", "digital", "system"]):
        tenders.append({
            "title": title,
            "link": link,
            "date": pub_date,
            "fetched_at": datetime.now().isoformat()
        })

# Ensure folder exists
import os
os.makedirs("data", exist_ok=True)

with open("data/tenders.json", "w", encoding="utf-8") as f:
    json.dump(tenders, f, indent=2, ensure_ascii=False)

print(f"Saved {len(tenders)} tenders")
