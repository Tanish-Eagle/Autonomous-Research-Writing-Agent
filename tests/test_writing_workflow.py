from agents.blog_writer import write_blog
from agents.critic_agent import review_article


def write_blog_with_review(topic: str, max_iterations: int = 3):

    article = write_blog(topic)

    for i in range(max_iterations):

        print(f"\n--- Review Round {i+1} ---\n")

        review = review_article(article)

        print("CRITIC RESPONSE:")
        print(review)

        if review.startswith("APPROVED"):
            print("\nArticle approved.\n")
            return article

        else:
            print("\nRewriting article based on feedback...\n")

            article = write_blog(
                topic + "\n\nEditor feedback:\n" + review
            )

    return article


topic = "FastAPI vs Flask performance"

final_article = write_blog_with_review(topic)

print("\nFINAL ARTICLE:\n")
print(final_article)