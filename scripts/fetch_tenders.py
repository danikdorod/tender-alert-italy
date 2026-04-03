import requests

url = "https://api.ted.europa.eu/v3/notices/search"

payload = {
    "query": "placeOfPerformance.countryCode=ITA",
    "page": 1,
    "fields": [
        "OPP-021-Contract",   # contract ID
        "BT-13(t)-Part",      # title (THIS is the real title field)
        "place-performance-streetline1-part"
    ]
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0"
}

response = requests.post(url, json=payload, headers=headers)

print("STATUS:", response.status_code)
print("RAW RESPONSE:", response.text[:1000])

data = response.json()

print("KEYS:", data.keys())

notices = (
    data.get("results")
    or data.get("notices")
    or data.get("content")
    or []
)

print(f"Saved {len(notices)} tenders")

for n in notices[:5]:
    print(n)
