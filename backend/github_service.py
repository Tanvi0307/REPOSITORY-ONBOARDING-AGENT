import base64
import os

import httpx

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def parse_github_url(repo_url: str):
    parts = repo_url.rstrip("/").split("/")

    if len(parts) < 5:
        raise ValueError("Invalid GitHub URL")

    owner = parts[-2]
    repo = parts[-1]

    return owner, repo


async def get_repo_data(repo_url: str):

    owner, repo = parse_github_url(repo_url)

    headers = {
        "Accept": "application/vnd.github+json"
    }

    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    async with httpx.AsyncClient() as client:

        readme_response = await client.get(
            f"https://api.github.com/repos/{owner}/{repo}/readme",
            headers=headers
        )

        contents_response = await client.get(
            f"https://api.github.com/repos/{owner}/{repo}/contents",
            headers=headers
        )

    readme_data = {}

    if readme_response.status_code == 200:
        readme_data = readme_response.json()

    contents_data = []

    if contents_response.status_code == 200:
        contents_data = contents_response.json()

    return {
        "owner": owner,
        "repo": repo,
        "readme": readme_data,
        "contents": contents_data
    }


async def get_file_content(
    owner: str,
    repo: str,
    path: str
):
    headers = {
        "Accept": "application/vnd.github+json"
    }

    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"https://api.github.com/repos/{owner}/{repo}/contents/{path}",
            headers=headers
        )

    if response.status_code != 200:
        return ""

    data = response.json()

    if "content" not in data:
        return ""

    return base64.b64decode(
        data["content"]
    ).decode(
        "utf-8",
        errors="ignore"
    )