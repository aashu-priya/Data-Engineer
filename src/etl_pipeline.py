# src/etl_pipeline.py
# src/etl_pipeline.py

from pyspark.sql import SparkSession
from src.config import RAW_DATA_PATH, PROCESSED_DATA_DIR
from src.data_processor import clean_data, add_features
from src.s3_utils import upload_to_mock_s3


def main():
    spark = SparkSession.builder.appName("ETL-Pipeline").getOrCreate()

    df = spark.read.option("header", True).csv(str(RAW_DATA_PATH), inferSchema=True)

    df_clean = clean_data(df)
    df_feat = add_features(df_clean)

    df_feat.coalesce(1).write.mode("overwrite").option("header", True).csv(str(PROCESSED_DATA_DIR))

    upload_to_mock_s3(str(PROCESSED_DATA_DIR) + "/*.csv", "processed_data.csv")

    spark.stop()

if __name__ == "__main__":
    main()
