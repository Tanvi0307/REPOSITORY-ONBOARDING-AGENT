from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from github_service import get_repo_data
from analyzer import analyze_repo, chat_with_repo
from rag_service import build_vectorstore

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class RepoRequest(BaseModel):
    url: str


class ChatRequest(BaseModel):
    question: str
    repo_name: str


@app.post("/analyze")
async def analyze(request: RepoRequest):

    # Existing repository analysis
    repo_data = await get_repo_data(request.url)

    result = analyze_repo(repo_data)

    # Build vector database for RAG
    repo_name = build_vectorstore(request.url)

    # Save repo name for chatbot
    result["repo_name"] = repo_name

    return result


@app.post("/chat")
async def chat(request: ChatRequest):

    answer = chat_with_repo(
        request.question,
        request.repo_name
    )

    return {
        "answer": answer
    }