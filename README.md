# Autonomous Research and Writing Agent

An AI-powered system that autonomously researches a topic, builds a knowledge base using Retrieval-Augmented Generation (RAG), and generates a structured blog post with self-critique and revision.

---


## Overview

This project implements a multi-agent pipeline that:

1. Searches the web for relevant information  

2. Scrapes and filters useful content  

3. Stores knowledge in a vector database (ChromaDB)  

4. Retrieves relevant context using RAG  

5. Generates a blog post using an LLM  

6. Evaluates the article using a critic agent  

7. Iteratively improves the article until it meets quality standards  

---

## System Architecture

User Input

↓

Input Validation (Guardrails)

↓

Research Agent (Search + Scrape)

↓

RAG Pipeline (ChromaDB)

↓

Writer Agent

↓

Critic Agent (Scoring + Feedback)

↓

Revision Loop

↓

Final Blog Output

---

## Tech Stack

* Backend: FastAPI  

* LLM: OpenAI (via LangChain)  

* Vector DB: ChromaDB  

* Search: DuckDuckGo (via LangChain Community Tools)  

* Scraping: Requests + BeautifulSoup  

* Environment Management: python-dotenv  

---

## Guardrails Implemented

To ensure reliability and output quality, guardrails are applied across the pipeline:

1. Input Guardrails

    * Rejects very short or unsafe queries  

    * Prevents malformed input  

2. Search Guardrails

    * Filters invalid or malformed URLs  

    * Limits number of search results  

3. Scraping Guardrails

    * Skips failed or blocked requests  

    * Filters out low-content or empty pages  

    * Limits text size for efficient processing  

4. RAG Guardrails

    * Removes weak or very short chunks  

    * Deduplicates retrieved content  

    * Limits number of retrieved documents  

5. Generation Guardrails

    * Writer agent constrained to provided context  

    * Prevents hallucination and unsupported claims  

6. Critic Agent

    * Scores article across multiple dimensions:

        - Clarity

        - Structure

        - Accuracy

        - Completeness

        - Readability  

    Enforces revision loop until quality threshold is met  

## Setup Instructions:

1. Clone the Repository

```
git clone https://github.com/Tanish-Eagle/Autonomous-Research-Writing-Agent

cd Autonomous-Research-Writing-Agent
```

2. Create Virtual Environment

```
python -m venv .venv

.venv\Scripts\activate # Windows
```

3. Install Dependencies

```
pip install -r requirements.txt
```

4. Setup Environment Variables

Create a .env file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

5. Run the Application

```
uvicorn api.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/
```

Usage

1. Enter a topic in the UI

2. System performs:

    * Research

    * Knowledge ingestion

    * Blog generation

    * Self-critique and revision

3. Final blog article is displayed

Example Topics

* FastAPI vs Flask performance

* What is Retrieval-Augmented Generation?

* Microservices vs Monolith architecture


Performance Note

* Initial requests may take 10–30 seconds due to:

    * Web scraping

    * Embedding generation

    * LLM processing

Limitations

* Depends on external web content quality

* Scraping may fail on some websites

* LLM responses may vary slightly between runs

* No advanced ranking of sources (basic filtering applied)

Future Improvements

* Streaming responses in UI

* Better source ranking and citation formatting

* Async scraping for faster performance

* Caching layer for repeated queries

* Enhanced UI/UX

## License

This project is for educational purposes. It is licensed under MIT license.

Author

Tanish Shrivastava
