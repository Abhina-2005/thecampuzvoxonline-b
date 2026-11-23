import requests
from bs4 import BeautifulSoup

url = "https://egrantz.kerala.gov.in/"

headers = {
    "User-Agent": "Mozilla/5.0"
}


response = requests.get(url, headers=headers, timeout=30)

print("Status:", response.status_code)
print("Final URL:", response.url)

soup = BeautifulSoup(response.text, "html.parser")

print("Page Title:", soup.title.get_text(strip=True))

print("\n--- LATEST 4 SCHOLARSHIP NOTIFICATIONS ---")

notice_section = soup.find(id="scholarships")

if notice_section:
    for item in notice_section.find_all("li")[:4]:
        title = item.get_text(" ", strip=True)

        link_tag = item.find("a", href=True)
        pdf_link = link_tag["href"] if link_tag else "No PDF link"

        if title:
            print("\nTitle:", title)
            print("PDF Link:", pdf_link)
            print("----------------------")