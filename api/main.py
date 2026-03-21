from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.blog_pipeline import generate_blog
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()


class BlogRequest(BaseModel):
    topic: str


@app.get("/", response_class=HTMLResponse)
def home():
    with open("api/templates/index.html") as f:
        return f.read()


@app.post("/generate-blog")
def generate(request: BlogRequest):
    try:
        article = generate_blog(request.topic)
        return {"article": article}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))