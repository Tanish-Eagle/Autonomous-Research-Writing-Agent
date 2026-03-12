from tools.scraper import scrape_page

url = "https://en.wikipedia.org/wiki/FastAPI"

text = scrape_page(url)

print(text[:1000])

