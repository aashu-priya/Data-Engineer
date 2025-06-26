# src/config.py

from pathlib import Path

# Explicit path to your Desktop project folder
BASE_DIR = Path.home() / "Desktop" / "Data-Engineer"

RAW_DATA_PATH = BASE_DIR / "data" / "raw_data.csv"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed_data.csv"
MOCK_S3_DIR = BASE_DIR / "mock_s3"
