import requests
from bs4 import BeautifulSoup

url = "https://ncs.gov.in/latest-update"

headers = {
    "User-Agent": "Mozilla/5.0"
}


response = requests.get(url, headers=headers, timeout=30)

response.encoding="utf-8"

soup = BeautifulSoup(response.text, "html.parser")

print("Status:", response.status_code)
print("Page Title:", soup.title.get_text(strip=True) if soup.title else "No title")

for row in soup.select("tr"):
    cells = row.find_all(["th", "td"])

    if len(cells) == 7:
        print(" | ".join(cell.get_text(" ", strip=True) for cell in cells))