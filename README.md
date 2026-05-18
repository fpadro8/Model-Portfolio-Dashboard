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

Deployment
----------

This dashboard runs as a Python web service and proxies Yahoo Finance requests through `dashboard_server.py`.

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run locally:

```bash
python dashboard_server.py
```

3. Open the app in your browser at:

```bash
http://localhost:8001/
```

4. Deploy to Render:

- Add the repository to Render.
- Render will use `render.yaml` and the included `Procfile`.
- The service starts with:

```bash
python dashboard_server.py
```
