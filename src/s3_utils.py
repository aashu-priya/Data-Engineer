# src/s3_utils.py

from src.config import MOCK_S3_DIR
from pathlib import Path
import shutil
import glob

def upload_to_mock_s3(source_pattern: str, destination_filename: str):
    MOCK_S3_DIR.mkdir(parents=True, exist_ok=True)
    files = glob.glob(source_pattern)
    if not files:
        raise FileNotFoundError("No files matched the pattern")

    source_file = files[0]
    dest_file = MOCK_S3_DIR / destination_filename
    shutil.copy(source_file, dest_file)
