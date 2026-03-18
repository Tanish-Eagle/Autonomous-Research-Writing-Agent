from agents.blog_pipeline import generate_blog

topic = "FastAPI vs Flask performance"

article = generate_blog(topic)

print("\nFINAL BLOG ARTICLE\n")
print(article)