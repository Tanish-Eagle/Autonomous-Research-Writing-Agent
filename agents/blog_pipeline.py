from agents.research_agent import research
from agents.blog_writer import write_blog
from agents.critic_agent import review_article

def validate_query(query: str):

    if not query or len(query.strip()) < 5:
        raise ValueError("Query is too short. Please provide a meaningful topic.")

    if len(query) > 200:
        raise ValueError("Query is too long.")

    banned_words = ["hack", "exploit", "bypass"]

    if any(word in query.lower() for word in banned_words):
        raise ValueError("Query contains unsafe content.")


def generate_blog(topic: str, max_revisions: int = 3):

    validate_query(topic)

    print("\n--- RESEARCH PHASE ---\n")

    research(topic)

    print("\n--- WRITING PHASE ---\n")

    article = write_blog(topic)

    for i in range(max_revisions):

        print(f"\n--- CRITIC REVIEW ROUND {i+1} ---\n")

        review = review_article(article)

        print(review)

        if "APPROVED" in review:

            print("\nArticle approved.\n")
            return article

        print("\nRevising article based on feedback...\n")

        article = write_blog(topic, feedback=review)

    print("\nMax revisions reached. Returning latest version.\n")

    return article