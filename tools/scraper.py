import requests
from bs4 import BeautifulSoup


def scrape_page(url: str):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        # ❌ bad response
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = " ".join(p.get_text().strip() for p in paragraphs)

        # ❌ empty or weak content
        if not text or len(text) < 200:
            return None

        # ✅ limit size (important for embeddings)
        return text[:3000]

    except Exception:
        return None