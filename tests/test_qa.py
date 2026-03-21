from rag.qa import answer_question

query = "Which is faster, FastAPI or Flask?"

answer = answer_question(query)

print("\nANSWER:\n")
print(answer)