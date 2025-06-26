# tests/test_data_processor.py

import pytest
from pyspark.sql import SparkSession
from src.data_processor import clean_data, add_features

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[*]").appName("pytest").getOrCreate()

@pytest.fixture
def raw_df(spark):
    data = [
        (25, "admin", "single", 1000, 100),
        (25, "admin", "single", 1000, 100),  # duplicate
        (30, None, "married", 1500, 0),
        (None, "technician", "single", None, 200),
    ]
    columns = ["age", "job", "marital", "balance", "duration"]
    return spark.createDataFrame(data, columns)

def test_clean_data_deduplication(raw_df):
    cleaned_df = clean_data(raw_df)
    assert cleaned_df.count() == 3  # one duplicate removed

def test_clean_data_nulls(raw_df):
    cleaned_df = clean_data(raw_df)
    assert cleaned_df.filter(cleaned_df.age.isNull()).count() == 0

def test_add_features(raw_df):
    cleaned_df = clean_data(raw_df)
    featured_df = add_features(cleaned_df)
    assert "balance_per_second" in featured_df.columns
