# Automated Validation & Metric Collection System

![CI](https://github.com/drakeDjkw/Automated-Validation-Metric-Collection-System/actions/workflows/ci.yml/badge.svg)

Minimal reference implementation for data validation, model evaluation, metric collection and storage.

Structure

- `src/avmcs/validation.py` — data validation functions
- `src/avmcs/metrics.py` — metric calculations

Experiments
-----------

This repository contains a small synthetic experiment used as a paper-style example. Running the experiments produces a CSV log and a sample plot under the `experiments/` directory. The committed outputs are:

- `experiments/results.csv` — aggregated MAE and RMSE per run (columns: bias, seed, MAE, RMSE)
- `experiments/metrics.png` — plot of MAE and RMSE vs model bias (averaged across seeds)

To reproduce locally (after creating and activating your virtualenv):

```bash
# install deps (if not already)
pip install -r requirements.txt

# run experiments (writes CSV and PNG to experiments/)
PYTHONPATH=src python scripts/run_experiments.py
```

The `metrics.png` image is committed so it will render on GitHub. For paper figures, you can generate SVG/PDF by modifying `scripts/run_experiments.py` (replace `fig.savefig(png_path)` with `fig.savefig(svg_path)` or add an extra save call).

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
