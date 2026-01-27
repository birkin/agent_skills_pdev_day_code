# Plan: Convert DigitalOcean LLM usage to LMStudio (local)

## Context summary (from AGENTS.md)
- Primary language: Python 3.12, use `uv` for execution/tests.
- HTTP calls should use `httpx` (AGENTS.md directive).
- Keep code changes minimal and match existing conventions.

## Known DigitalOcean-specific spots (from codebase scan)
- `agent_example.py` uses the DigitalOcean Serverless Inference endpoint:
  - API URL: `https://inference.do-ai.run/v1/chat/completions`
  - Auth header: `Authorization: Bearer <DIGITAL_OCEAN_MODEL_ACCESS_KEY>`
  - Uses `requests` (conflicts with `httpx` directive)
  - Model: `llama3.3-70b-instruct`
  - Env var: `DIGITAL_OCEAN_MODEL_ACCESS_KEY`

## Goal
Switch the agent demo to call a local LMStudio server on the Mac (OpenAI-compatible API).

---

## Plan

### 1) Confirm LMStudio API assumptions
- Verify the local server is running and the endpoint follows the OpenAI-compatible API.
- Typical defaults (confirm in LMStudio UI):
  - Base URL: `http://localhost:1234/v1`
  - Chat endpoint: `/chat/completions`
  - No API key required, or use `Authorization: Bearer <token>` if configured.
- Identify the exact model ID exposed by LMStudio (e.g., `local-model`, `llama-3.1-8b-instruct`, etc.).

### 2) Update configuration points
- Replace DigitalOcean URL with LMStudio base URL.
- Rename env var to something local, e.g. `LMSTUDIO_API_KEY` (optional) and/or `LMSTUDIO_BASE_URL`.
- Decide whether to keep a fallback to DigitalOcean (likely no; goal is local-only).

### 3) Update HTTP client usage
- Replace `requests` with `httpx` for all HTTP calls in the agent client.
- Ensure headers and payload match LMStudio OpenAI-compatible schema:
  - `model`: LMStudio model ID.
  - `messages`: same list of role/content.
  - `temperature`, `max_tokens` as needed.
- Handle timeouts and error reporting consistently.

### 4) Update docs/instructions
- Update README or usage docs (if any) to:
  - Explain how to run LMStudio locally.
  - Mention required env vars (`LMSTUDIO_*`).
  - Example run command using `uv`.

### 5) Smoke test
- Run `uv run ./agent_example.py` and verify:
  - Local LMStudio receives requests.
  - Function-calling loop still works.
  - Response parsing remains valid.

---

## Notes for a new session
- Respect AGENTS.md directives (httpx, type hints, etc.).
- The key touchpoints are in `agent_example.py` (API URL, headers, env var, request library).
- If LMStudio is not OpenAI-compatible in this setup, inspect its API docs and adjust payload accordingly.
- Keep changes minimal and focused to the agent demo unless other scripts also call the DO endpoint.
