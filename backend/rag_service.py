import os
import shutil
import tempfile

from git import Repo

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


# Ignore generated folders

IGNORE_DIRS = {
    ".git",
    "node_modules",
    "venv",
    ".venv",
    "__pycache__",
    "dist",
    "build",
    ".next",
    ".idea",
    ".vscode",
    "coverage",
    "target",
    "out",
    ".cache"
}


# Supported file types

ALLOWED_EXTENSIONS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".go",
    ".rs",
    ".php",
    ".rb",
    ".cs",
    ".cpp",
    ".c",
    ".h",
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".xml",
    ".html",
    ".css",
    ".scss",
    ".sql",
    ".sh"
}


MAX_FILE_SIZE = 500_000  # 500 KB


embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


def clone_repo(repo_url: str) -> str:
    """
    Clone repository to a temporary directory.
    """

    temp_dir = tempfile.mkdtemp()

    repo = Repo.clone_from(
        repo_url,
        temp_dir
    )

    repo.close()

    return temp_dir


def load_documents(repo_path: str):
    """
    Load all supported files recursively.
    """

    documents = []

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [
            d for d in dirs
            if d not in IGNORE_DIRS
        ]

        for file in files:

            extension = os.path.splitext(file)[1].lower()

            if extension not in ALLOWED_EXTENSIONS:
                continue

            file_path = os.path.join(root, file)

            try:
                if os.path.getsize(file_path) > MAX_FILE_SIZE:
                    continue

                loader = TextLoader(
                    file_path,
                    encoding="utf-8"
                )

                docs = loader.load()

                relative_path = os.path.relpath(
                    file_path,
                    repo_path
                )

                for doc in docs:
                    doc.metadata["source"] = relative_path

                documents.extend(docs)

            except Exception:
                continue

    return documents


def build_vectorstore(repo_url: str) -> str:
    """
    Build and persist the vector database.
    """

    repo_name = (
        repo_url.rstrip("/")
        .split("/")[-1]
        .replace(".git", "")
    )

    persist_dir = os.path.join(
        "vector_db",
        repo_name
    )

    # Reuse existing vector database

    if os.path.exists(persist_dir):
        return repo_name

    repo_path = clone_repo(repo_url)

    documents = load_documents(repo_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    # Limit chunks for faster indexing

    chunks = chunks[:300]

    os.makedirs(
        persist_dir,
        exist_ok=True
    )

    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir
    )

    try:
        shutil.rmtree(repo_path)
    except PermissionError:
        pass

    return repo_name


def get_retriever(repo_name: str):
    """
    Load the vector database retriever.
    """

    persist_dir = os.path.join(
        "vector_db",
        repo_name
    )

    if not os.path.exists(persist_dir):
        raise FileNotFoundError(
            f"Vector database not found for {repo_name}"
        )

    vectorstore = Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings
    )

    return vectorstore.as_retriever(
        search_kwargs={"k": 5}
    )