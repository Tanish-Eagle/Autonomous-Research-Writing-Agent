from tools.search import run_search, extract_urls
from tools.scraper import scrape_page


query = "FastAPI vs Flask performance"

results = run_search(query)

#print(type(results))
urls = extract_urls(results)

for url in urls:
    text = scrape_page(url)
    print(text[:500])