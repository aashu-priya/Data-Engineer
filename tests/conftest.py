# tests/conftest.py

import pytest
import pandas as pd

@pytest.fixture
def sample_dataframe():
    data = {
        "age": [25, 30, None, 40],
        "job": ["admin", None, "technician", "admin"],
        "marital": ["single", "married", "single", "married"],
        "balance": [1000, 1500, None, 2000],
        "duration": [100, 0, 200, 300],
    }
    return pd.DataFrame(data)
