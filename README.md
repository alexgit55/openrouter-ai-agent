# OpenRouter AI Agent

A Python CLI coding agent that uses OpenRouter via the OpenAI SDK and supports tool calling for local file operations.

The agent can:

- List files and directories
- Read file contents (with truncation)
- Run Python files with optional arguments
- Write or overwrite files

## How It Works

The entrypoint is `main.py`.

1. A user prompt is sent to the model (`openrouter/free`)
2. The model can request one or more tool calls
3. Tool calls are executed locally
4. Tool results are sent back to the model
5. The loop continues until the model returns a final response or `MAX_ITERS` is reached

For safety, tool calls are sandboxed to `./calculator` in `call_function.py`.

## Project Structure

```text
.
├── main.py
├── call_function.py
├── prompts.py
├── functions/
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── run_python_file.py
│   └── write_file.py
├── calculator/
│   ├── main.py
│   ├── tests.py
│   └── pkg/
└── test_*.py
```

## Requirements

- Python 3.13+
- An OpenRouter API key

Dependencies (from `pyproject.toml`):

- `openai==2.44.0`
- `python-dotenv==1.1.0`

## Setup

### 1. Clone and enter the repository

```bash
git clone https://github.com/alexgit55/openrouter-ai-agent.git
cd openrouter-ai-agent
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Using pip:

```bash
pip install openai==2.44.0 python-dotenv==1.1.0
```

Or using your preferred `pyproject.toml` workflow (for example, `uv`).

### 4. Configure environment variables

Create a `.env` file in the repository root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
MAX_ITERS=8
MAX_CHARS=4000
```

Variable reference:

- `OPENROUTER_API_KEY`: required API key
- `MAX_ITERS`: max model/tool-call loop iterations in `main.py`
- `MAX_CHARS`: max characters returned by `get_file_content`

## Usage

Run the agent:

```bash
python main.py "your prompt here"
```

Verbose mode:

```bash
python main.py "inspect calculator project and summarize it" --verbose
```

Example prompts:

- `List all files in the project root and explain what each does`
- `Read pkg/calculator.py and find potential bugs`
- `Run tests.py and summarize failures`
- `Create a new file called notes.txt with a short summary`

## Available Tools

### `get_files_info`

- Lists files in a target directory
- Returns file size and whether each entry is a directory
- Rejects access outside the configured working directory

### `get_file_content`

- Reads a file from the working directory
- Truncates output at `MAX_CHARS`
- Appends a truncation notice when content is longer
- Rejects access outside the working directory

### `run_python_file`

- Runs a `.py` file with optional arguments
- Returns `STDOUT`, `STDERR`, and non-zero exit codes
- Enforces a 30-second timeout
- Rejects non-Python files and paths outside the working directory

### `write_file`

- Writes text content to a file (overwrite behavior)
- Creates parent directories if needed
- Rejects directory targets and paths outside the working directory

## Running Local Tests

The repository includes script-style test files for each tool.

```bash
python test_get_files_info.py
python test_get_file_content.py
python test_run_python_file.py
python test_write_file.py
```

The calculator sample app also has unit tests:

```bash
python calculator/tests.py
```

## Notes and Limitations

- Tool execution is currently pinned to `./calculator` in `call_function.py`
- `main.py` expects `MAX_ITERS` to be set; missing value raises an error
- `get_file_content` expects `MAX_CHARS` to be set; missing value raises an error

## Troubleshooting

### `OPENROUTER_API_KEY environment variable not set`

- Ensure `.env` exists in the repository root
- Confirm `OPENROUTER_API_KEY` is defined

### Immediate runtime error on startup

- Verify both `MAX_ITERS` and `MAX_CHARS` are set to integers in `.env`

### No useful model response

- Try `--verbose` to inspect token usage and function call flow
- Increase `MAX_ITERS` if tasks require multiple tool calls

## License

Add a license section here if/when you choose a license for the project.
