## OmniTrainer: Multimodal Moderation Sandbox

AI-powered content moderation sandbox for a fictional ACME Enterprise helpdesk. The project simulates a conversation between a trainee agent and an angry customer while moderating text, images, audio, and video using Google Gemini. It exposes both a Gradio chat UI and FastAPI endpoints, with Phoenix tracing for observability.

### Repository structure
- `multimodal_moderation/`: core package  
  - `agents/`: text, image, audio, video moderation agents plus the LLM customer agent  
  - `types/moderation_result.py`: Pydantic schemas for moderation outputs  
  - `gradio_app.py`: chat UI for trainee-customer simulations  
  - `fastapi_app.py`: REST endpoints for programmatic moderation  
  - `tracing.py`: Phoenix tracing integration  
  - `__main__.py`: entrypoint to run services together
- `evals/`: evaluation cases for text, image, audio, and video agents
- `tests/`: unit tests for agents, schema, and Gradio app
- `example.env`: template for required environment variables
- `requirements.txt` / `requirements_slim.txt` / `uv.lock`: dependency specs

### Setup
1) Create and activate a virtual environment (uv recommended):
   ```bash
   uv sync --dev
   uv pip install -e .
   ```
   Or with vanilla venv/pip:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   pip install -e .
   ```

2) Configure credentials:
   ```bash
   cp example.env .env
   # edit .env with GEMINI_API_KEY and a USER_API_KEY of your choice
   ```

3) (Optional) Select the venv interpreter in your IDE for linting/completions.

### Running
- Run all tests: `uv run pytest tests/ -vv`
- Start the combined services (FastAPI backend, Gradio frontend, Phoenix): `uv run multimodal-moderation`
- Gradio UI: http://localhost:7860  
  FastAPI docs: http://0.0.0.0:8000/docs  
  Phoenix UI: http://localhost:6006/projects
