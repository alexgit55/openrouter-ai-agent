# Calculator App

A simple Python command-line calculator that evaluates space-separated infix expressions and prints JSON output.

## Features

- Supports operators: `+`, `-`, `*`, `/`
- Honors standard precedence (`*` and `/` before `+` and `-`)
- Accepts integer or floating-point operands
- Returns formatted JSON output
- Includes unit tests

## Project Structure

```text
calculator/
├── main.py
├── tests.py
├── README.md
└── pkg/
    ├── calculator.py
    ├── render.py
    
```

## Requirements

- Python 3.10+ (works with the parent project requirement of Python 3.13+)

No third-party dependencies are required for this calculator app.

## Usage

From the `calculator` directory:

```bash
python main.py "3 + 5"
```

Example output:

```json
{
  "expression": "3 + 5",
  "result": 8
}
```

If no expression is provided:

```bash
python main.py
```

Output:

```text
Calculator App
Usage: python main.py "<expression>"
Example: python main.py "3 + 5"
```

## Expression Rules

- Tokens must be separated by spaces
- Valid: `"2 * 3 - 8 / 2 + 5"`
- Invalid: `"2*3+4"` (missing spaces between tokens)

The evaluator processes infix tokens and uses operator/operand stacks internally.

## Error Handling

The app reports clear errors for invalid input, for example:

- Invalid token (for unsupported symbols)
- Not enough operands
- Empty or whitespace-only expressions

Examples:

```bash
python main.py "$ 3 5"
# Error: Invalid token: $

python main.py "+ 3"
# Error: Not enough operands for operator +
```

## Run Tests

From the `calculator` directory:

```bash
python tests.py
```

Or with `unittest` discovery:

```bash
python -m unittest tests.py
```

## Implementation Notes

- Core evaluator class: `pkg/calculator.py` (`Calculator`)
- JSON formatting helper: `pkg/render.py` (`format_json_output`)
- CLI entrypoint: `main.py`

The JSON renderer converts whole-number floats (for example `8.0`) to integers (`8`) for cleaner output.