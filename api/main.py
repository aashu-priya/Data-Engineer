from fastapi import FastAPI
from api.endpoints import router
import pandas as pd
from src.config import PROCESSED_DATA_DIR

app = FastAPI(
    title="Data Engineer ETL API",
    description="API to access processed banking marketing data",
    version="1.0.0"
)

@app.get("/")
def root():
    df = pd.read_csv(PROCESSED_DATA_DIR)
    return df.sample(n=5).to_dict(orient="records")

app.include_router(router)
