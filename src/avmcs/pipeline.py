from typing import Callable, List, Dict, Any
import numpy as np

from .metrics import compute_metrics


class DummyModel:
    """A simple model stub that implements predict(X) for demo/testing."""

    def __init__(self, bias: float = 0.0):
        self.bias = bias

    def predict(self, X: np.ndarray) -> np.ndarray:
        # trivial "prediction": average of features plus bias
        return np.mean(X, axis=1) + self.bias


def run_pipeline(
    model: Callable[..., Any],
    X: np.ndarray,
    y: np.ndarray,
    batch_size: int = 32,
) -> Dict[str, Any]:
    """Run evaluation in batches, compute metrics per-batch and aggregate.

    Returns a dict with per-batch metrics and aggregated mean metrics.
    """
    n = X.shape[0]
    batch_metrics: List[Dict[str, float]] = []

    for i in range(0, n, batch_size):
        xb = X[i:i + batch_size]
        yb = y[i:i + batch_size]

        y_pred = model.predict(xb) if hasattr(model, "predict") else model(xb)

        m = compute_metrics(yb, y_pred)
        batch_metrics.append(m)

    # aggregate by averaging each metric
    agg: Dict[str, float] = {}
    if batch_metrics:
        keys = batch_metrics[0].keys()
        for k in keys:
            agg[k] = float(np.mean([bm[k] for bm in batch_metrics]))

    return {"batch_metrics": batch_metrics, "aggregated": agg}
