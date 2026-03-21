from rag.retriever import get_relevant_docs

query = "FastAPI vs Flask performance"

docs = get_relevant_docs(query)

for d in docs:
    print("\n---\n")
    print(d.page_content)