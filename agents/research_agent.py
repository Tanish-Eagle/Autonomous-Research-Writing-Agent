from tools.search import run_search, extract_urls
from tools.scraper import scrape_page
from rag.ingest import ingest_text
from rag.qa import answer_question


def research(query: str):

    print(f"\nResearching: {query}\n")

    results = run_search(query)

    urls = extract_urls(results)

    # scrape and store knowledge
    for url in urls[:3]:

        print(f"Scraping {url}")

        text = scrape_page(url)

        if text:
            ingest_text(text, source=url)

    # generate answer
    answer = answer_question(query)

    return answer