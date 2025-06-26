# tests/test_etl.py

from src import etl_pipeline

def test_etl_runs():
    try:
        etl_pipeline.main()
        success = True
    except Exception:
        success = False
    assert success
