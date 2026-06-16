from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from github_service import get_repo_data
from analyzer import analyze_repo, chat_with_repo

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
    repo_data: dict


@app.post("/analyze")
async def analyze(request: RepoRequest):

    repo_data = await get_repo_data(request.url)

    print(repo_data)

    result = analyze_repo(repo_data)

    return result


@app.post("/chat")
async def chat(request: ChatRequest):

    answer = chat_with_repo(
        request.question,
        request.repo_data
    )

    return {"answer": answer}