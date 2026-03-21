from agent.research_agent import research

query = "What are the performance differences between FastAPI and Flask?"

answer = research(query)

print("\nFINAL ANSWER:\n")
print(answer)