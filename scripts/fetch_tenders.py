import requests

url = "https://api.ted.europa.eu/v3/notices/search"

payload = {
    "query": "placeOfPerformance.countryCode:ITA",
    "limit": 10
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()

notices = data.get("results", [])

print(f"Saved {len(notices)} tenders")

for n in notices:
    print(n.get("title"))
