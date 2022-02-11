.PHONY:
check:
	python setup.py check -m -s
	pre-commit run --all-files
test:
	python -m unittest
dependencies:
	pip install -e .
dependencies.dev:
	make dependencies
	pip install -e .[dev]
