# Contributing

Thanks for your interest in contributing to `rag-lite-kit`.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

## Pull request checklist

- Keep the project runnable with the default lightweight setup
- Add or update tests for behavior changes
- Update README or docs if public behavior changes
- Prefer small, focused PRs

## Suggested areas to contribute

- document loaders
- vector store adapters
- model provider adapters
- evaluation and benchmarking
- observability and tracing
- Docker and deployment examples
