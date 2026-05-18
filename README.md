Claude integration (Python)
---------------------------

Quick start:

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and set `CLAUDE_API_KEY`.

3. Run a test prompt:

```bash
python run_claude.py "Write a one-line summary of today's weather."
```

Notes:
- This uses the official `anthropic` Python SDK; ensure your key has access.
- The model default is `claude-2.1`. You provided version `2.1.143`; set `CLAUDE_MODEL_VERSION` in `.env` for bookkeeping.
- If you edited `claude_client.py` earlier, it now uses `anthropic` SDK instead of raw HTTP.
