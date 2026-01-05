OmniTrainer: Multimodal Moderation Sandbox
Author: Saad Iqbal
Date: 05/01/2026
OmniTrainer is an AI-powered multimodal content moderation sandbox built for a fictional ACME Enterprise helpdesk.

The project simulates real-world customer support interactions where a trainee agent engages with an angry customer, while all user inputs are moderated in real time across text, images, audio, and video using Google Gemini-style LLMs.
The system exposes both an interactive Gradio chat UI and programmatic FastAPI endpoints, with full OpenTelemetry tracing and Arize Phoenix observability to inspect moderation behavior, conversation flow, and feedback signals.
Key Features
✅ Structured moderation outputs via a shared ModerationResult Pydantic model
🧠 LLM-based moderation agents for text, image, audio, and video inputs
💬 Simulated LLM customer agent with contextual, stateful responses
🖥️ Gradio multimodal chat UI with pre-display moderation enforcement
🌐 FastAPI endpoints for programmatic moderation access
🔍 End-to-end tracing using OpenTelemetry and Arize Phoenix
🧪 Pydantic-based evals and comprehensive unit test coverage

Repository Structure
Plain text
ANTLR4
Bash
C
C#
CSS
CoffeeScript
CMake
Dart
Django
Docker
EJS
Erlang
Git
Go
GraphQL
Groovy
HTML
Java
JavaScript
JSON
JSX
Kotlin
LaTeX
Less
Lua
Makefile
Markdown
MATLAB
Markup
Objective-C
Perl
PHP
PowerShell
.properties
Protocol Buffers
Python
R
Ruby
Sass (Sass)
Sass (Scss)
Scheme
SQL
Shell
Swift
SVG
TSX
TypeScript
WebAssembly
YAML
XML

multimodal_moderation/
├── agents/                  # Moderation agents (text, image, audio, video)
│   └── customer_agent.py    # Simulated LLM customer
├── types/
│   └── moderation_result.py # Pydantic schema for structured moderation output
├── gradio_app.py            # Multimodal chat UI with moderation hooks
├── fastapi_app.py           # REST API for moderation services
├── tracing.py               # OpenTelemetry + Phoenix tracing setup
├── __main__.py              # Entrypoint to run all services together
evals/
├── text/                    # Text moderation evaluation cases
├── image/                   # Image moderation evaluation cases
├── audio/                   # Audio moderation evaluation cases
├── video/                   # Video moderation evaluation cases
tests/
├── test_moderation_result.py
├── test_text_agent.py
├── test_image_agent.py
├── test_gradio_app.py
example.env                  # Environment variable template
requirements.txt             # Full dependency set
requirements_slim.txt        # Minimal runtime dependencies
uv.lock                      # Locked dependency graph



Setup
1. Create and Activate a Virtual Environment
Using uv (recommended):
Plain text
ANTLR4
Bash
C
C#
CSS
CoffeeScript
CMake
Dart
Django
Docker
EJS
Erlang
Git
Go
GraphQL
Groovy
HTML
Java
JavaScript
JSON
JSX
Kotlin
LaTeX
Less
Lua
Makefile
Markdown
MATLAB
Markup
Objective-C
Perl
PHP
PowerShell
.properties
Protocol Buffers
Python
R
Ruby
Sass (Sass)
Sass (Scss)
Scheme
SQL
Shell
Swift
SVG
TSX
TypeScript
WebAssembly
YAML
XML

uv sync --dev
uv pip install -e .



Using standard venv + pip:
Plain text
ANTLR4
Bash
C
C#
CSS
CoffeeScript
CMake
Dart
Django
Docker
EJS
Erlang
Git
Go
GraphQL
Groovy
HTML
Java
JavaScript
JSON
JSX
Kotlin
LaTeX
Less
Lua
Makefile
Markdown
MATLAB
Markup
Objective-C
Perl
PHP
PowerShell
.properties
Protocol Buffers
Python
R
Ruby
Sass (Sass)
Sass (Scss)
Scheme
SQL
Shell
Swift
SVG
TSX
TypeScript
WebAssembly
YAML
XML

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .



2. Configure Environment Variables
Plain text
ANTLR4
Bash
C
C#
CSS
CoffeeScript
CMake
Dart
Django
Docker
EJS
Erlang
Git
Go
GraphQL
Groovy
HTML
Java
JavaScript
JSON
JSX
Kotlin
LaTeX
Less
Lua
Makefile
Markdown
MATLAB
Markup
Objective-C
Perl
PHP
PowerShell
.properties
Protocol Buffers
Python
R
Ruby
Sass (Sass)
Sass (Scss)
Scheme
SQL
Shell
Swift
SVG
TSX
TypeScript
WebAssembly
YAML
XML

cp example.env .env



Edit .env and provide:
GEMINI_API_KEY – API key for the Gemini-compatible LLM
USER_API_KEY – arbitrary key used for FastAPI authentication

3. (Optional) IDE Configuration
Select the virtual environment interpreter in your IDE to enable linting, type hints, and autocomplete.
Running the Project
Run All Tests
Plain text
ANTLR4
Bash
C
C#
CSS
CoffeeScript
CMake
Dart
Django
Docker
EJS
Erlang
Git
Go
GraphQL
Groovy
HTML
Java
JavaScript
JSON
JSX
Kotlin
LaTeX
Less
Lua
Makefile
Markdown
MATLAB
Markup
Objective-C
Perl
PHP
PowerShell
.properties
Protocol Buffers
Python
R
Ruby
Sass (Sass)
Sass (Scss)
Scheme
SQL
Shell
Swift
SVG
TSX
TypeScript
WebAssembly
YAML
XML

uv run pytest tests/ -vv



Start the Full Application Stack
Plain text
ANTLR4
Bash
C
C#
CSS
CoffeeScript
CMake
Dart
Django
Docker
EJS
Erlang
Git
Go
GraphQL
Groovy
HTML
Java
JavaScript
JSON
JSX
Kotlin
LaTeX
Less
Lua
Makefile
Markdown
MATLAB
Markup
Objective-C
Perl
PHP
PowerShell
.properties
Protocol Buffers
Python
R
Ruby
Sass (Sass)
Sass (Scss)
Scheme
SQL
Shell
Swift
SVG
TSX
TypeScript
WebAssembly
YAML
XML

uv run multimodal-moderation



This launches:
Gradio UI: http://localhost:7860
FastAPI Docs: http://0.0.0.0:8000/docs
Phoenix Dashboard: http://localhost:6006/projects




