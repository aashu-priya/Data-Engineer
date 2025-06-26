# src/data_processor.py

from pyspark.sql import DataFrame
import pyspark.sql.functions as F

def clean_data(df: DataFrame) -> DataFrame:
    df = df.dropDuplicates()

    for col, dtype in df.dtypes:
        if dtype in ("int", "double", "float", "bigint"):
            avg = df.select(F.mean(col)).first()[0]
            if avg is not None:
                df = df.fillna({col: avg})
        else:
            df = df.fillna({col: "Unknown"})
    return df

def add_features(df: DataFrame) -> DataFrame:
    # Sample feature: balance to duration ratio (safe check for nonzero)
    if "balance" in df.columns and "duration" in df.columns:
        df = df.withColumn(
            "balance_per_second",
            F.when(df["duration"] != 0, df["balance"] / df["duration"]).otherwise(0)
        )
    return df
