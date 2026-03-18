from agents.research_agent import research
from agents.blog_writer import write_blog
from agents.critic_agent import review_article


def generate_blog(topic: str, max_revisions: int = 3):

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