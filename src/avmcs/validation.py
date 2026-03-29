import pandas as pd
from typing import Dict, Any


def validate_data(
    df: pd.DataFrame, checks: Dict[str, Any] = None
) -> Dict[str, Any]:
    """Run basic validation checks on a DataFrame.

    Returns a dict of errors; empty dict means no errors.

    Basic checks implemented:
    - missing values per column
    - numeric dtype checks if column specified in checks
    - range checks if provided in checks as (min, max)

    checks example:
    {
        "temperature": {"type": "numeric", "range": [-50, 60]},
        "humidity": {"type": "numeric", "range": [0, 100]},
    }
    """
    errors = {}

    # Missing values
    missing = df.isnull().sum()
    if missing.sum() > 0:
        errors["missing_values"] = missing[missing > 0].to_dict()

    if checks is None:
        checks = {}

    for col, spec in checks.items():
        if col not in df.columns:
            errors.setdefault("missing_columns", {})[col] = "Column not found"
            continue

        if spec.get("type") == "numeric":
            if not pd.api.types.is_numeric_dtype(df[col]):
                errors.setdefault("type_errors", {})[col] = "Not numeric"

        if "range" in spec:
            lo, hi = spec["range"]
            if (df[col] < lo).any() or (df[col] > hi).any():
                msg = f"Values outside [{lo}, {hi}]"
                errors.setdefault("range_errors", {})[col] = msg

    return errors
