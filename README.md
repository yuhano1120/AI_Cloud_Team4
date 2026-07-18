# CMU AI Student Support Assistant

Foundation architecture for a cloud-hosted AI assistant that helps CMU students ask questions about campus resources, academic support, administrative processes, and student services.

## What This Repository Contains

- A reproducible VS Code devcontainer.
- A small FastAPI prototype that accepts a CMU student question and returns a stubbed assistant response.
- A sane project structure for future cloud, model, retrieval, and frontend work.
- Architecture documentation and an AI provenance log for TM1 submission.

## Repository Structure

```text
.
├── .devcontainer/          # Reproducible development environment
├── .github/workflows/      # CI: lint and test on every push and pull request
├── app/                    # FastAPI application code
│   ├── model/              # Model-service boundary and stubbed answer generation
│   └── retrieval/          # RAG retrieval boundary and placeholder CMU context
├── docs/                   # Architecture diagram, narrative, and provenance log
├── scripts/                # Local helper commands
├── tests/                  # Prototype tests
├── pyproject.toml          # Python dependencies and tool configuration
└── README.md               # Setup and conventions
```

## Quick Start

### Option 1: Devcontainer

1. Open this repository in VS Code.
2. Choose **Reopen in Container**.
3. Run:

```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. Open `http://localhost:8000/docs`.

### Option 2: Local Python

Use Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload --port 8000
```

## Try the Prototype

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Where can I find academic support at CMU?"}'
```

Expected response shape:

```json
{
  "answer": "Stub response: ...",
  "status": "stubbed",
  "provider": "stub://local",
  "trace_id": "...",
  "retrieved_context": [
    {
      "title": "Academic Support",
      "content": "...",
      "source": "stub://cmu-academic-support",
      "score": 0.72
    }
  ]
}
```

## Tests and Linting

```bash
pytest
ruff check .
```

Both run automatically on every push and pull request via `.github/workflows/ci.yml`.

## Learner Lab Validation

The prototype was validated inside AWS Academy Learner Lab CloudShell on 2026-07-17. The repository was cloned from GitHub, dependencies were installed, `pytest` passed with 4 tests, and the running FastAPI service returned successful responses from both `/health` and `/ask`.

## Project Conventions

- Keep cloud-facing architecture decisions in `docs/architecture-narrative.md`.
- Keep diagrams in `docs/architecture-diagram.md`.
- Record AI-generated contributions in `docs/provenance-log.md`.
- Application endpoints belong in `app/main.py` until the prototype grows enough to justify routers.
- Retrieval and future RAG logic belong in `app/retrieval/`, not directly inside endpoint handlers.
- Model-provider calls belong in `app/model/`, so no endpoint imports a provider SDK directly.
- Request and response contracts should be represented with Pydantic models.
- New behavior should include at least one focused test in `tests/`.
- Run `ruff check .` and `pytest` before pushing; CI enforces both.

## Current Prototype Scope

The application currently accepts a CMU student support question, calls a stubbed retrieval layer, passes the question and retrieved context through a stubbed model adapter, and returns a deterministic answer with placeholder retrieved context. This proves the future RAG path at the module-boundary level while leaving room to connect a real model provider, a CMU resource knowledge base, authentication, feedback collection, and a deployment pipeline in later milestones.
