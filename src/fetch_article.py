# src/fetch_article.py
import requests
from bs4 import BeautifulSoup

def fetch_article_text(url: str):
    try:
        page = requests.get(url, timeout=10)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, "html.parser")

        # Extract title
        title = soup.title.string if soup.title else "Unknown Title"

        # Extract paragraphs
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        text = "\n".join(paragraphs)

        return {
            "title": title.strip(),
            "authors": [],
            "publish_date": None,
            "text": text
        }
    except Exception as e:
        return {
            "title": "Error fetching article",
            "authors": [],
            "publish_date": None,
            "text": str(e)
        }
