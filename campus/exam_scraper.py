import requests
from bs4 import BeautifulSoup

url = "https://neet.nta.nic.in/public-notices/"

keam_url = "https://cee.kerala.gov.in/"


headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=30)

response.encoding="utf-8"


print("Status:", response.status_code)
print("Final URL:", response.url)

soup = BeautifulSoup(response.text, "html.parser")

print("Page Title:", soup.title.get_text(strip=True))

print("\n--- NEET NOTIFICATION LINKS ---")

for link in soup.find_all("a", href=True):
    title = link.get_text(" ", strip=True)
    url = link["href"]

    if title and ("NEET" in title.upper() or "NOTICE" in title.upper()):
        print("\nTitle:", title)
        print("Link:", url)
        print("----------------------")