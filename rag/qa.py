from langchain_openai import ChatOpenAI
from rag.retriever import get_relevant_docs


def answer_question(query: str):

    docs = get_relevant_docs(query)

    context = "\n\n".join([d.page_content for d in docs])

    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = f"""
Use the following research context to answer the question.

Context:
{context}

Question:
{query}

Answer clearly and concisely.
"""

    response = llm.invoke(prompt)

    return response.content