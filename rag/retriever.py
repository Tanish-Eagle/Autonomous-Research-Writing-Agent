from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def get_relevant_docs(query: str, k: int = 5):

    embedding = OpenAIEmbeddings()

    vectordb = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": k})

    docs = retriever.invoke(query)

    # ✅ Guardrail 1: filter empty or tiny chunks
    docs = [d for d in docs if d.page_content and len(d.page_content.strip()) > 100]

    # ✅ Guardrail 2: remove duplicates (by content)
    seen = set()
    unique_docs = []

    for d in docs:
        content = d.page_content.strip()
        if content not in seen:
            seen.add(content)
            unique_docs.append(d)

    # ✅ Guardrail 3: cap final docs
    return unique_docs[:5]