# Automated Validation & Metric Collection System

![CI](https://github.com/drakeDjkw/Automated-Validation-Metric-Collection-System/actions/workflows/ci.yml/badge.svg)

Minimal reference implementation for data validation, model evaluation, metric collection and storage.

Structure

- `src/avmcs/validation.py` — data validation functions
- `src/avmcs/metrics.py` — metric calculations
- `src/avmcs/storage.py` — saving/loading metrics
- `src/avmcs/pipeline.py` — simple evaluation pipeline
- `scripts/run_pipeline.py` — small runner demonstrating the flow
- `tests/test_pipeline.py` — basic unit test

Quick start

1. Create a virtualenv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the demo:

```bash
python scripts/run_pipeline.py
```

Developer — Linting & tests
--------------------------

If you're contributing or running checks locally, follow these steps. The package source is under `src/` so either set `PYTHONPATH=src` or use your own editable packaging.

1) Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2) Install developer dependencies:

```bash
pip install -r requirements.txt
```

3) Run linter (flake8):

```bash
PYTHONPATH=src python -m flake8 src tests
```

4) Run tests (pytest):

```bash
PYTHONPATH=src python -m pytest -q
```

5) Run the demo pipeline (sanity check):

```bash
PYTHONPATH=src python scripts/run_pipeline.py
```

Notes
- If you prefer not to set `PYTHONPATH` every time, add `export PYTHONPATH=src` to your shell session while developing.
- For CI we run the same commands; see `.github/workflows/ci.yml`.

3. Run tests:

```bash
pytest -q
```
