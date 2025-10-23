# news_scraper.py

import requests
from bs4 import BeautifulSoup

# URL of the news website (example: BBC News)
url = "https://www.bbc.com/news"

# Custom headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

try:
    # Send GET request
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise error for bad status

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all headline tags (common tags are h1, h2, h3)
    headlines = soup.find_all("h3")  

    # Extract and clean text
    headline_texts = [headline.get_text(strip=True) for headline in headlines]

    # Save headlines to a text file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, text in enumerate(headline_texts, start=1):
            file.write(f"{i}. {text}\n")

    print("Headlines successfully scraped and saved to headlines.txt")

except requests.exceptions.RequestException as e:
    print("Error fetching the webpage:", e)
