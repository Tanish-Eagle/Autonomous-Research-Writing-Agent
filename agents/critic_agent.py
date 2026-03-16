from langchain_openai import ChatOpenAI


def review_article(article: str):

    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = f"""
You are a strict technical editor reviewing a blog post.

Evaluate the article using the following criteria:

1. Clarity – Are explanations easy to understand?
2. Structure – Does the article have a clear introduction, sections, and conclusion?
3. Technical Accuracy – Are claims reasonable and consistent with the context?
4. Completeness – Does the article fully address the topic?
5. Readability – Is the writing smooth and professional?

Score each category from 1 to 10.

Rules:
- If ANY category is below 7, the article must be revised.
- If ALL categories are 7 or higher, the article is approved.

Respond ONLY in the following format:

SCORES
Clarity: X/10
Structure: X/10
Accuracy: X/10
Completeness: X/10
Readability: X/10

VERDICT
APPROVED

OR

VERDICT
REVISE

FEEDBACK
Explain clearly what should be improved.

Article:
{article}
"""

    response = llm.invoke(prompt)

    return response.content