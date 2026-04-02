# Automated Validation & Metric Collection System (AVMCS)

![CI](https://github.com/drakeDjkw/Automated-Validation-Metric-Collection-System/actions/workflows/ci.yml/badge.svg)

A minimal, production-oriented reference implementation for **data validation, model evaluation, metric collection, and storage**. Designed for reproducible machine learning experiments and academic workflows.

---

## 📦 Project Structure

.
├── src/avmcs/
│   ├── validation.py     # Data validation functions
│   ├── metrics.py        # Metric calculations (MAE, RMSE, etc.)
│   ├── storage.py        # Saving/loading metrics
│   └── pipeline.py       # Evaluation pipeline
├── scripts/
│   ├── run_pipeline.py   # Demo pipeline runner
│   └── run_experiments.py
├── experiments/
│   ├── results.csv
│   └── metrics.png
├── tests/
│   └── test_pipeline.py
├── requirements.txt
└── README.md

---

## ⚡ Quick Start (Recommended)

### 1. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate


⸻

2. Install Dependencies

pip install -r requirements.txt


⸻

3. Set Python Path (IMPORTANT)

export PYTHONPATH=src

This ensures Python can locate the avmcs package.

⸻

4. Run Demo Pipeline

python3 scripts/run_pipeline.py


⸻

5. Run Experiments

python3 scripts/run_experiments.py

Outputs:
	•	experiments/results.csv
	•	experiments/metrics.png

⸻

6. Run Tests

python3 -m pytest -q


⸻

🧪 Experiments

This repository includes a synthetic experiment demonstrating evaluation workflows.

Outputs
	•	results.csv — aggregated MAE and RMSE
	•	metrics.png — performance vs bias visualization

⸻

📊 Experiment Summary (Mean ± Std)

bias	MAE (mean ± std)	RMSE (mean ± std)
-1.00	1.6410 ± 0.0409	2.0513 ± 0.0392
-0.75	1.5488 ± 0.0292	1.9475 ± 0.0310
-0.50	1.4830 ± 0.0207	1.8714 ± 0.0252
-0.25	1.4433 ± 0.0127	1.8264 ± 0.0258
0.00	1.4344 ± 0.0041	1.8148 ± 0.0333
0.25	1.4563 ± 0.0180	1.8372 ± 0.0438
0.50	1.5075 ± 0.0340	1.8924 ± 0.0545
0.75	1.5863 ± 0.0466	1.9779 ± 0.0641
1.00	1.6883 ± 0.0584	2.0899 ± 0.0722


⸻

🧾 LaTeX Table (for Papers)

\begin{table}[ht]
\centering
\begin{tabular}{rcc}
\toprule
Bias & MAE (mean $\pm$ std) & RMSE (mean $\pm$ std)\\
\midrule
-1.00 & 1.6410 $\pm$ 0.0409 & 2.0513 $\pm$ 0.0392\\
-0.75 & 1.5488 $\pm$ 0.0292 & 1.9475 $\pm$ 0.0310\\
-0.50 & 1.4830 $\pm$ 0.0207 & 1.8714 $\pm$ 0.0252\\
-0.25 & 1.4433 $\pm$ 0.0127 & 1.8264 $\pm$ 0.0258\\
0.00 & 1.4344 $\pm$ 0.0041 & 1.8148 $\pm$ 0.0333\\
0.25 & 1.4563 $\pm$ 0.0180 & 1.8372 $\pm$ 0.0438\\
0.50 & 1.5075 $\pm$ 0.0340 & 1.8924 $\pm$ 0.0545\\
0.75 & 1.5863 $\pm$ 0.0466 & 1.9779 $\pm$ 0.0641\\
1.00 & 1.6883 $\pm$ 0.0584 & 2.0899 $\pm$ 0.0722\\
\bottomrule
\end{tabular}
\caption{MAE and RMSE across seeds for each model bias.}
\end{table}


⸻

🧑‍💻 Developer Guide

Lint Code

PYTHONPATH=src python3 -m flake8 src tests


⸻

Run Tests

PYTHONPATH=src python3 -m pytest -q


⸻

Run Pipeline

PYTHONPATH=src python3 scripts/run_pipeline.py


⸻

⚠️ Common Issues

❌ ModuleNotFoundError: avmcs

Fix:

export PYTHONPATH=src


⸻

❌ python: command not found (macOS)

Use:

python3


⸻

❌ pytest not found

Install:

pip install pytest


⸻

🚀 Future Improvements
	•	Convert to installable package (pyproject.toml)
	•	Add CLI (avmcs run)
	•	Docker support
	•	Experiment tracking (MLflow / Weights & Biases)

⸻

📄 License

MIT License

⸻

👤 Author

Sandrakh Yikwa
AI / Machine Learning Engineer

---

# 🔥 What I improved
- Fixed **my exact error (PYTHONPATH issue)**
- Made it **macOS-safe (`python3`)**
- Added **clear step-by-step execution**
- Added **Common Issues section (very important for GitHub users)**
- Upgraded to **portfolio / academic standard**