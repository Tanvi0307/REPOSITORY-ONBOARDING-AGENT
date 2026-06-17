# Repository Onboarding Agent

An AI-powered developer assistant that helps users quickly understand and explore any GitHub repository using **Large Language Models (LLMs)** and **Retrieval-Augmented Generation (RAG)**.

Paste a GitHub repository URL, and the agent will automatically:

* Summarize the project
* Identify important files with contextual descriptions
* Generate a personalized learning path
* Build a searchable knowledge base from the repository source code
* Answer questions through an interactive RAG-powered chatbot

Built with **React**, **FastAPI**, **Ollama**, **ChromaDB**, **LangChain**, and the **GitHub REST API**.

---

## Features

* Repository analysis from a GitHub URL
* README extraction and summarization
* Important file identification with descriptions
* Personalized learning path generation
* Recursive codebase indexing
* RAG-powered repository chatbot
* Semantic search across repository files
* Local LLM support using Ollama
* Persistent vector database for faster subsequent analysis
* Modern responsive UI

---

## Demo

Enter a GitHub repository URL:

```text
https://github.com/facebook/react
```

The agent provides:

* Project summary
* Important files and descriptions
* Learning path
* Interactive repository chatbot

Example questions:

* How does authentication work?
* Which file initializes the application?
* Where are the API routes defined?
* How is the database configured?
* Explain the project architecture.

---

## Architecture

```text
                    ┌───────────────────┐
                    │   React Frontend  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  FastAPI Backend  │
                    └─────────┬─────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
 ┌───────────────┐   ┌─────────────────┐   ┌───────────────┐
 │ GitHub API    │   │ Ollama LLMs     │   │ ChromaDB      │
 └───────────────┘   └─────────────────┘   └───────────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  RAG Retrieval    │
                    └───────────────────┘
```

---

## RAG Workflow

```text
User submits repository URL
            │
            ▼
Repository cloned locally
            │
            ▼
Source files recursively loaded
            │
            ▼
Files chunked into smaller sections
            │
            ▼
Embeddings generated using nomic-embed-text
            │
            ▼
Vectors stored in ChromaDB
            │
            ▼
User asks a question
            │
            ▼
Relevant code chunks retrieved
            │
            ▼
LLM generates context-aware answers
```

---

## Tech Stack

### Frontend

* React
* Vite
* Tailwind CSS
* Axios
* Lucide React
* React Spinners

### Backend

* Python
* FastAPI
* Uvicorn
* Pydantic
* HTTPX

### AI & RAG

* Ollama
* LangChain
* ChromaDB
* Ollama Embeddings

### APIs

* GitHub REST API

---

## Models

| Purpose             | Model              |
| ------------------- | ------------------ |
| Repository analysis | `llama3.2:3b`      |
| Chatbot responses   | `llama3.2:1b`      |
| Embeddings          | `nomic-embed-text` |

---

## Project Structure

```text
repository-onboarding-agent/
│
├── backend/
│   ├── app.py
│   ├── analyzer.py
│   ├── github_service.py
│   ├── rag_service.py
│   ├── requirements.txt
│   ├── vector_db/
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── api.js
│   │   └── components/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## Installation

### Prerequisites

Install:

* Python 3.10+
* Node.js 18+
* Git
* Ollama

Download Ollama:

```text
https://ollama.com/download
```

---

## Install Ollama Models

Pull the required models:

```bash
ollama pull llama3.2:3b
ollama pull llama3.2:1b
ollama pull nomic-embed-text
```

Start Ollama:

```bash
ollama serve
```

---

## Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GITHUB_TOKEN=your_github_token
OLLAMA_BASE_URL=http://localhost:11434

OLLAMA_MODEL=llama3.2:3b
CHAT_MODEL=llama3.2:1b
EMBEDDING_MODEL=nomic-embed-text
```

Start the backend:

```bash
python -m uvicorn app:app --reload
```

Backend URL:

```text
http://localhost:8000
```

---

## Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## Usage

1. Open the frontend application.
2. Paste a GitHub repository URL.
3. Click **Analyze**.
4. Wait while the repository is indexed.
5. Review the generated insights.
6. Ask questions using the chatbot.

> **Note:** The first analysis of a repository may take longer because embeddings and the vector database are created. Subsequent analyses reuse the stored vectors for faster responses.

---

## Environment Variables

| Variable          | Description                           |
| ----------------- | ------------------------------------- |
| `GITHUB_TOKEN`    | GitHub Personal Access Token          |
| `OLLAMA_BASE_URL` | Ollama server URL                     |
| `OLLAMA_MODEL`    | Model used for repository analysis    |
| `CHAT_MODEL`      | Model used for chatbot responses      |
| `EMBEDDING_MODEL` | Embedding model for vector generation |

---

## Security

Never commit sensitive files.

Ensure the following are included in `.gitignore`:

```text
.env
*.env
node_modules/
venv/
__pycache__/
vector_db/
```

---

## Future Improvements

* Repository architecture diagrams
* Dependency graph visualization
* Multi-repository comparison
* Support for private repositories
* Conversation memory
* Incremental indexing for repository updates
* Multi-modal repository analysis
* PDF report generation
* Support for GitLab and Bitbucket
* Agentic code exploration workflows

---

