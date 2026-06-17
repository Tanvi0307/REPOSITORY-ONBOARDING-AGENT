import base64
import json
import os

from ollama import Client

from rag_service import get_retriever

client = Client(
    host=os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )
)

MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2:3b"
)

CHAT_MODEL = os.getenv(
    "CHAT_MODEL",
    "llama3.2:1b"
)


def analyze_repo(data):
    readme = ""

    if "content" in data["readme"]:
        readme = base64.b64decode(
            data["readme"]["content"]
        ).decode(
            "utf-8",
            errors="ignore"
        )

    contents = data.get("contents", [])

    if not isinstance(contents, list):
        raise Exception(
            f"GitHub API error: {contents}"
        )

    ignore = {
        "venv",
        "node_modules",
        ".git",
        "__pycache__"
    }

    files = [
        item["name"]
        for item in contents
        if item["name"] not in ignore
    ]

    prompt = f"""
You are a senior software engineer helping a new developer understand a repository.

Repository: {data["owner"]}/{data["repo"]}

README:
{readme[:1500]}

Files:
{files[:15]}

Return ONLY valid JSON in this format:

{{
  "summary": "short explanation",
  "important_files": ["file1", "file2"],
  "learning_path": ["step 1", "step 2"],
  "project_structure": ["folder description"]
}}
"""

    response = client.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json"
    )

    result = json.loads(
        response["message"]["content"]
    )

    result["readme"] = readme[:1000]

    result["repo_name"] = (
        f'{data["owner"]}/{data["repo"]}'
    )

    return result


def chat_with_repo(question, repo_name):

    retriever = get_retriever(repo_name)

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [
            f"File: {doc.metadata['source']}\n"
            f"{doc.page_content}"
            for doc in docs
        ]
    )

    prompt = f"""
You are a helpful repository assistant.

Answer the user's question using ONLY the repository context below.

Repository Context:

{context}

User Question:
{question}

Rules:

- Mention file names when relevant.
- If the answer is not in the context, say:

"I couldn't find that information in the repository."
"""

    response = client.chat(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]