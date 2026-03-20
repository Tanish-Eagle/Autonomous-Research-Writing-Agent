from langchain_openai import ChatOpenAI
from rag.retriever import get_relevant_docs


def write_blog(topic: str, feedback: str | None = None):

    docs = get_relevant_docs(topic)

    # Build context with source information
    context = "\n\n".join(
        f"Source: {d.metadata['source']}\nContent: {d.page_content}"
        for d in docs
    )

    # Collect unique sources for reference
    sources = list({d.metadata["source"] for d in docs})

    llm = ChatOpenAI(model="gpt-4o-mini")

    revision_section = ""
    if feedback:
        revision_section = f"""
The previous version of the article was reviewed by an editor.

Editor Feedback:
{feedback}

Revise the article to address ALL feedback while keeping the article clear and well structured.
"""

    prompt = f"""
You are a professional technical writer specializing in developer-focused content.

Write a clear, accurate, and well-structured technical blog post.

Topic:
{topic}

Research Context:
{context}

{revision_section}

Writing Guidelines:
- Write a well structured article.
- Include a clear and descriptive title.
- Start with an introduction explaining the topic and why it matters.
- Organize the article into logical sections with headings.
- Explain concepts clearly for developers.
- Use concise paragraphs.
- Avoid repeating the same idea multiple times.
- Ensure technical claims are consistent with the research context.
- Conclude with a short summary.
- Do not fabricate facts not present in the research context.
- If information is insufficient, say so clearly.
- Avoid speculation.

Citation Rules:
- Base the article on the research context.
- Do not invent sources.
- Use the provided sources for references.

Available Sources:
{chr(10).join(sources)}

At the end include a section:

Sources
- source_url
- source_url

Blog Post:
"""

    response = llm.invoke(prompt)

    return response.content