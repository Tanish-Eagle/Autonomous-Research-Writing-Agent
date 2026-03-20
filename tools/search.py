from langchain_community.tools import DuckDuckGoSearchResults

search = DuckDuckGoSearchResults(output_format="list")

def run_search(query: str):
    return search.invoke(query)

def extract_urls(results):

    urls = []

    for r in results:
        url = r.get("link")

        if not url:
            continue

        # basic filtering
        if not url.startswith("http"):
            continue

        urls.append(url)

    # limit number of URLs
    return urls[:5]