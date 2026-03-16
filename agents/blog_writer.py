from langchain_openai import ChatOpenAI
from rag.retriever import get_relevant_docs


def write_blog(topic: str):

    docs = get_relevant_docs(topic)

    # Build context with source information
    context = "\n\n".join(
        f"Source: {d.metadata['source']}\nContent: {d.page_content}"
        for d in docs
    )

    # Collect unique sources for reference
    sources = list({d.metadata["source"] for d in docs})

    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = f"""
You are a professional technical writer.

Using the research context provided below, write a clear and informative blog post about the topic.

Topic:
{topic}

Research Context:
{context}

Guidelines:
- Write a well structured article.
- Include a clear title.
- Start with an introduction explaining the topic.
- Organize the content into logical sections with headings.
- Explain concepts clearly for developers.
- Conclude with a short summary.
- At the end of the article include a "Sources" section listing the referenced URLs.

Available Sources:
{chr(10).join(sources)}

Blog Post:
"""

    response = llm.invoke(prompt)

    return response.content