install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	ruff check gendiff tests

test:
	pytest tests/