import numpy as np

from avmcs.pipeline import DummyModel, run_pipeline
from avmcs.storage import save_metrics, load_metrics


def test_run_pipeline_and_save(tmp_path):
    # small dataset
    X = np.zeros((10, 3))
    y = np.zeros(10)

    model = DummyModel(bias=0.0)
    results = run_pipeline(model, X, y, batch_size=4)

    assert "batch_metrics" in results
    assert "aggregated" in results
    assert "MAE" in results["aggregated"]

    out = tmp_path / "results.json"
    save_metrics(results, filename=str(out))
    assert out.exists()

    loaded = load_metrics(filename=str(out))
    assert isinstance(loaded, dict)
    assert "aggregated" in loaded
