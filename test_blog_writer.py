from agents.blog_writer import write_blog

topic = "FastAPI vs Flask performance comparison"

blog = write_blog(topic)

print(blog)