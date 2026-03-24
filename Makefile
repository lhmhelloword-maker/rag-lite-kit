.PHONY: install test run lint clean

install:
	python -m pip install -e .[dev]

test:
	pytest

run:
	uvicorn rag_lite_kit.api:app --reload

clean:
	rm -rf .pytest_cache .chromadb build dist *.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
