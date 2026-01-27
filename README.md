# Goal

Experiment with the new concept of using "skill" files for agents, for a professional-development day.

---

# LMStudio setup

1. Start LMStudio and enable the local server (OpenAI-compatible API).
2. Note the model ID shown in LMStudio (used in `LMSTUDIO_MODEL`).

## Environment variables

- `LMSTUDIO_BASE_URL` (optional, default: `http://localhost:1234/v1`)
- `LMSTUDIO_API_KEY` (optional; set if your LMStudio server requires auth)
- `LMSTUDIO_MODEL` (optional, default: `local-model`)

## Run the agent demo

```bash
uv run ./agent_example.py
```

---