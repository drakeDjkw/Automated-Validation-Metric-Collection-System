"""Simple runner to demo the pipeline."""
import numpy as np
import pandas as pd
from pathlib import Path

from avmcs.validation import validate_data
from avmcs.pipeline import DummyModel, run_pipeline
from avmcs.storage import save_metrics


def make_dummy_dataset(n=500, features=5, seed=0):
    rng = np.random.RandomState(seed)
    X = rng.normal(loc=0.0, scale=1.0, size=(n, features))
    # target is sum of features + small noise
    y = X.sum(axis=1) + rng.normal(scale=0.5, size=n)
    return X, y


def main():
    X, y = make_dummy_dataset()

    # Create a DataFrame version for validation example
    df = pd.DataFrame(X, columns=[f"f{i}" for i in range(X.shape[1])])
    df["target"] = y

    checks = {f"f{i}": {"type": "numeric", "range": [-10, 10]} for i in range(X.shape[1])}
    chk_errs = validate_data(df, checks=checks)
    if chk_errs:
        print("Validation errors:")
        print(chk_errs)
        # For demo we continue; in production we might abort

    model = DummyModel(bias=0.1)
    results = run_pipeline(model, X, y, batch_size=64)

    out = Path("results.json")
    save_metrics(results, filename=str(out))
    print(f"Saved results to {out.resolve()}")


if __name__ == "__main__":
    main()
