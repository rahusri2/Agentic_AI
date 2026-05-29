# Langchain Study Project

Python learning project for LangChain, managed with [uv](https://docs.astral.sh/uv/).

## Prerequisites

Install uv (macOS):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify:

```bash
uv --version
```

## UV setup (full workflow)

These are the steps used to bootstrap this project from scratch.

### 1. Go to the project directory

```bash
cd Agentic_AI/Langchain
```

### 2. Initialize a uv project

```bash
uv init
```

This creates:

- `pyproject.toml` — project metadata and dependencies
- `main.py` — entry script
- `.python-version` — pinned Python (3.12)

**Important:** `uv init` sets the project `name` from the folder name. Because this folder is named `Langchain`, uv defaulted to `name = "langchain"`. That **conflicts** with the PyPI package `langchain` when you try to install it.

**Fix:** Rename the project in `pyproject.toml` before adding dependencies:

```toml
[project]
name = "langchain-study"   # must NOT match any dependency name
```

Use any unique name (e.g. `langchain-study`, `agentic-langchain`). Do not use `langchain`.

### 3. Create a virtual environment

```bash
uv venv
```

Creates `.venv` using the Python version in `.python-version` (CPython 3.12).

### 4. Activate the virtual environment (optional)

```bash
source .venv/bin/activate
```

Your shell prompt may show `(Langchain)`. You can also run commands without activating by using `uv run` (see below).

### 5. Add dependencies from `requirements.txt`

Create or edit `requirements.txt`:

```text
langchain
langchain_community
langchain-openai
langchain-groq
python-dotenv
langchain-google-genai
```

Install into the project (updates `pyproject.toml` and `uv.lock`):

```bash
uv add -r requirements.txt
```

Expected success output:

```text
Resolved 72 packages in ...
Checked 69 packages in ...
```

**If you see this error**, the project name still shadows `langchain`:

```text
error: Requirement name `langchain` matches project name `langchain`, but self-dependencies are not permitted...
```

Rename the project in `pyproject.toml` (step 2) and run `uv add -r requirements.txt` again.

### 6. Run the app

With venv activated:

```bash
python main.py
```

Or without activating (uv uses `.venv` automatically):

```bash
uv run python main.py
```

## Day-to-day uv commands

| Task | Command |
|------|---------|
| Add one package | `uv add <package>` |
| Add dev dependency | `uv add --dev pytest` |
| Sync env from lockfile | `uv sync` |
| Run a script | `uv run python main.py` |
| Show installed packages | `uv pip list` |
| Update lockfile after editing `pyproject.toml` | `uv lock` |

## Project layout

```text
Langchain/
├── .python-version      # 3.12
├── .venv/               # virtualenv (gitignored)
├── pyproject.toml       # project name + dependencies
├── uv.lock              # locked versions
├── requirements.txt     # convenience list (optional after uv add)
├── main.py
└── README.md
```

## Environment variables

For API keys (OpenAI, Groq, Google GenAI), use a `.env` file in this directory (already in `.gitignore`):

```bash
# .env — do not commit
OPENAI_API_KEY=...
GROQ_API_KEY=...
GOOGLE_API_KEY=...
```

Load in Python with `python-dotenv` (already installed).

## Quick reference: commands from this session

```bash
cd Agentic_AI/Langchain
uv init
# edit pyproject.toml → name = "langchain-study"
uv venv
source .venv/bin/activate
uv add -r requirements.txt
uv run python main.py
```
