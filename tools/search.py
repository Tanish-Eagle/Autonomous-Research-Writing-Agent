from langchain_community.tools import DuckDuckGoSearchResults

search = DuckDuckGoSearchResults(output_format="list")

def run_search(query: str):
    return search.invoke(query)

def extract_urls(results, max_results=3):
    urls = []

    for result in results[:max_results]:
        if "link" in result:
            urls.append(result["link"])

    return urls