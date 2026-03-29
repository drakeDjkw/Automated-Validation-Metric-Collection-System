import json
from typing import Any


def save_metrics(metrics: Any, filename: str = "results.json") -> None:
    with open(filename, "w") as f:
        json.dump(metrics, f, indent=4)


def load_metrics(filename: str = "results.json") -> Any:
    with open(filename, "r") as f:
        return json.load(f)
