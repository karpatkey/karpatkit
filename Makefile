install:
	uv sync --dev
test:
	uv run pytest -v src

pretty:
	uv run ruff format
	uv run ruff check --fix-only

lint:
	uv run ruff check

