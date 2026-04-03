import requests
import json
from datetime import datetime

# TED API endpoint (simplified search)
URL = "https://ted.europa.eu/api/v2/notices/search"

# Basic query: Italy + IT services
params = {
    "query": "IT services",
    "country": "IT",
    "limit": 20
}

response = requests.get(URL, params=params)

if response.status_code != 200:
    print("Error fetching data")
    exit()

data = response.json()

tenders = []

for item in data.get("results", []):
    tenders.append({
        "title": item.get("title"),
        "buyer": item.get("buyer"),
        "deadline": item.get("deadline"),
        "link": item.get("url"),
        "date_fetched": datetime.now().isoformat()
    })

# Save to file
with open("data/tenders.json", "w", encoding="utf-8") as f:
    json.dump(tenders, f, indent=2, ensure_ascii=False)

print("Saved", len(tenders), "tenders")