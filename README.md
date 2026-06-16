# Repository Onboarding Agent

An AI-powered developer assistant that helps users quickly understand any GitHub repository.

Paste a GitHub repository URL, and the agent will automatically:

* Summarize the project
* Identify important files
* Generate a learning path
* Answer questions about the repository through an interactive chatbot

Built with **React**, **FastAPI**, **Ollama**, and the **GitHub REST API**.

---

## Features

* Repository analysis from a GitHub URL
* README extraction and summarization
* Important file identification
* Personalized learning path generation
* Interactive repository chatbot
* Local LLM support using Ollama
* Modern responsive UI

---

## Demo

Enter a GitHub repository URL:

```text
https://github.com/facebook/react
```

The agent provides:

* Project summary
* Important files
* Learning path
* Repository Q&A assistant

---

## Architecture

```text
React Frontend
       │
       ▼
FastAPI Backend
       │
       ├── GitHub REST API
       │
       └── Ollama (Local LLM)
```

### Workflow

1. User submits a GitHub repository URL.
2. FastAPI fetches repository metadata from GitHub.
3. The README and file structure are extracted.
4. Ollama analyzes the repository.
5. The frontend displays the generated insights.
6. Users can ask follow-up questions through the chatbot.

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
* Ollama
* HTTPX
* Pydantic

### APIs

* GitHub REST API

### Models

* `llama3.2:3b` for repository analysis
* `llama3.2:1b` for chatbot responses

---

## Project Structure

```text
repository-onboarding-agent/
│
├── backend/
│   ├── app.py
│   ├── analyzer.py
│   ├── github_service.py
│   ├── requirements.txt
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
4. Review the generated summary, important files, and learning path.
5. Ask questions using the chatbot.

---

## Example Questions

* What does this project do?
* Which file should I read first?
* How do I run this application?
* What framework does this repository use?
* Explain the README.
* What are the main dependencies?

---

## Environment Variables

| Variable          | Description                        |
| ----------------- | ---------------------------------- |
| `GITHUB_TOKEN`    | GitHub Personal Access Token       |
| `OLLAMA_BASE_URL` | Ollama server URL                  |
| `OLLAMA_MODEL`    | Model used for repository analysis |
| `CHAT_MODEL`      | Model used for chatbot responses   |

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
```

---

## Future Improvements

* Deep codebase analysis
* Dependency graph visualization
* Repository architecture diagrams
* Multi-repository comparison
* Support for private repositories
* Conversation memory
* Export reports as PDF

---

