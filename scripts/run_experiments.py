"""Run multiple synthetic evaluation runs, write CSV of aggregated metrics, and plot trends.

Outputs:
 - experiments/results.csv
 - experiments/metrics.png

This script uses the `DummyModel` and `run_pipeline` from `avmcs.pipeline`.
"""
import os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from avmcs.pipeline import DummyModel, run_pipeline


def make_dummy_dataset(n=500, features=5, seed=0):
    rng = np.random.RandomState(seed)
    X = rng.normal(loc=0.0, scale=1.0, size=(n, features))
    y = X.sum(axis=1) + rng.normal(scale=0.5, size=n)
    return X, y


def run_many(bias_values, seeds, out_dir="experiments"):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    rows = []

    for bias in bias_values:
        for seed in seeds:
            X, y = make_dummy_dataset(n=500, features=5, seed=seed)
            model = DummyModel(bias=bias)
            results = run_pipeline(model, X, y, batch_size=64)
            agg = results.get("aggregated", {})
            rows.append({"bias": bias, "seed": seed, **agg})

    df = pd.DataFrame(rows)
    csv_path = out / "results.csv"
    df.to_csv(csv_path, index=False)

    # Plot MAE and RMSE vs bias (average across seeds)
    agg_by_bias = df.groupby("bias").mean().reset_index()

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(agg_by_bias["bias"], agg_by_bias["MAE"], marker="o", label="MAE")
    ax.plot(agg_by_bias["bias"], agg_by_bias["RMSE"], marker="s", label="RMSE")
    ax.set_xlabel("Model bias")
    ax.set_ylabel("Error")
    ax.set_title("MAE / RMSE vs model bias (synthetic dataset)")
    ax.grid(True)
    ax.legend()

    png_path = out / "metrics.png"
    fig.tight_layout()
    fig.savefig(png_path)
    plt.close(fig)

    print(f"Wrote CSV -> {csv_path.resolve()}")
    print(f"Wrote plot -> {png_path.resolve()}")


if __name__ == "__main__":
    # vary bias to see how error changes
    biases = np.linspace(-1.0, 1.0, 9)
    seeds = [0, 1, 2]
    run_many(bias_values=biases, seeds=seeds, out_dir="experiments")
