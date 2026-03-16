from tools.search import run_search, extract_urls
from tools.scraper import scrape_page
from rag.ingest import ingest_text
from rag.qa import answer_question
from rag.retriever import get_relevant_docs


def research(query: str):

    print(f"\nResearching: {query}\n")

    # Check existing knowledge first
    docs = get_relevant_docs(query)

    if len(docs) < 3:

        print("Knowledge insufficient, searching web...\n")

        results = run_search(query)
        urls = extract_urls(results)

        # scrape and store knowledge
        for url in urls[:3]:

            print(f"Scraping {url}")

            text = scrape_page(url)

            if text:
                ingest_text(text, source=url)

    else:

        print("Using existing knowledge base.\n")

    # generate answer
    answer = answer_question(query)

    return answer