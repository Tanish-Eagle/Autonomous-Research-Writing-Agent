from tools.search import run_search, extract_urls
from tools.scraper import scrape_page
from rag.ingest import ingest_text


query = "FastAPI vs Flask performance"

results = run_search(query)

urls = extract_urls(results)

for url in urls[:3]:

    print(f"Scraping: {url}")

    text = scrape_page(url)

    if text:
        ingest_text(text, source=url)