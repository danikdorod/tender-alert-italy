import requests

url = "https://api.ted.europa.eu/v3/notices/search"

payload = {
    "query": "publicationDate:[2024-01-01 TO 2026-12-31]",
    "page": 1
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

for n in notices:
    print(n.get("title"))
