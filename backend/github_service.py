import os
import re
import httpx

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def parse_url(url: str):
    match = re.search(r"github\.com/([^/]+)/([^/]+)", url)

    if not match:
        raise ValueError("Invalid GitHub URL")

    owner = match.group(1)
    repo = match.group(2).replace(".git", "")

    return owner, repo


async def get_repo_data(repo_url: str):
    owner, repo = parse_url(repo_url)

    headers = {
        "Accept": "application/vnd.github+json"
    }

    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    async with httpx.AsyncClient() as client:

        readme = await client.get(
            f"https://api.github.com/repos/{owner}/{repo}/readme",
            headers=headers,
        )

        contents = await client.get(
            f"https://api.github.com/repos/{owner}/{repo}/contents",
            headers=headers,
        )

    readme_data = readme.json()
    contents_data = contents.json()

    print("README:", readme_data)
    print("CONTENTS:", contents_data)

    return {
        "owner": owner,
        "repo": repo,
        "readme": readme_data,
        "contents": contents_data,
    }