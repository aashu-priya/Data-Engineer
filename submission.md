# 📄 Project Submission: Data Engineering ETL Pipeline

## 🧾 Project Title
**End-to-End ETL Pipeline with PySpark, FastAPI, and Docker**

---

## 👩‍💻 Author

- **Name:** Ashu Priya  
- **GitHub:** [@aashu-priya](https://github.com/aashu-priya)  
- **Repository Link:** [Data-Engineer](https://github.com/aashu-priya/Data-Engineer)

---

## 📝 Project Description

This project demonstrates a complete **data engineering workflow**, from raw data ingestion to serving cleaned data via a REST API. The ETL pipeline is built using:

- **PySpark**: Efficient processing of large-scale data.
- **FastAPI**: Lightweight and fast API framework to serve cleaned data.
- **Docker**: For containerized, reproducible environments.
- **Airflow (optional)**: For scheduling and orchestrating pipeline tasks.

The main goal is to simulate a real-world ETL use case where dirty data from CSV is cleaned, deduplicated, and made available through a REST API.

---

## 📁 Directory Structure

```
Data-Engineer/
│
├── data/                # Contains the input raw_data.csv
│
├── mock_s3/             # Stores the cleaned data after ETL (mimicking S3)
│
├── src/
│   └── etl_pipeline.py  # PySpark code that handles Extract, Transform, Load
│
├── api/
│   └── main.py          # FastAPI app exposing endpoints for data access
│
├── tests/               # Unit tests for ETL logic and API
│
├── airflow/
│   └── dags/
│       └── etl_dag.py   # Optional DAG for orchestrating ETL tasks
│
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container setup
├── docker-compose.yml   # Multi-container orchestration
└── README.md            # Setup and usage instructions
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/aashu-priya/Data-Engineer.git
cd Data-Engineer
```

### 2. Set Up the Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Place Your Dataset

The ETL pipeline expects a CSV file located at `data/raw_data.csv` with:
- At least **1000+ records**
- Some **missing** and **duplicate** values

```bash
# Example
data/raw_data.csv
```

### 5. Run the ETL Pipeline

Processes the raw data and stores the cleaned output to the mock S3 bucket:

```bash
PYTHONPATH=. python src/etl_pipeline.py
```

### 6. Launch the FastAPI Server

Starts the backend API to serve the cleaned data:

```bash
uvicorn api.main:app --reload
```

Open Swagger UI in your browser:

```
http://127.0.0.1:8000/docs
```

### 7. Sample API Endpoint

Fetch sample data from the cleaned dataset using:

```bash
curl "http://127.0.0.1:8000/data/sample?limit=10"
```

Or test directly in Swagger.

### 8. Run Unit Tests

Run `pytest` to ensure everything works as expected:

```bash
pytest tests/
```

Tests include:
- Verifying if data is loaded correctly
- Ensuring missing/duplicate values are handled
- Testing API response and edge cases

---

## 📊 Dataset Explanation

The dataset should:
- Be in **CSV** format
- Contain **realistic dirty data**: missing values, duplicated rows, inconsistent types
- Be placed in `data/raw_data.csv`

The ETL pipeline handles:
- **Missing value imputation**
- **Removing duplicates**
- **Column renaming and normalization**

---

## 🔍 ETL Pipeline Overview

- **Extract**: Load raw CSV using PySpark.
- **Transform**: Clean missing values, drop duplicates, and standardize columns.
- **Load**: Save the cleaned dataset to `mock_s3/cleaned_data.csv`.

Key features:
- Modular PySpark logic
- Easily extendable for JSON, Parquet, or real S3

---

## 🌐 FastAPI Overview

FastAPI exposes endpoints like:

- `GET /data/sample?limit=10`: Fetch sample rows from cleaned dataset
- Swagger UI: Auto-generated documentation for easy testing

Built using:
- `pandas` to read cleaned file
- `FastAPI` to serve endpoints

---

## 🐳 Docker Overview (Optional)

Containerizes the full pipeline for deployment or portability:

### Build Docker Containers

```bash
docker compose build
```

### Run Services

```bash
docker compose up
```

### Access API Container

```bash
docker compose run --service-ports api bash
```

---

## ⛓️ Airflow DAG (Optional)

File: `airflow/dags/etl_dag.py`

Simulates scheduled execution of the ETL job using Airflow DAGs. Helpful if deployed in an actual Airflow environment.

---

## ✅ Submission Checklist

- [x] Dataset present and correctly placed
- [x] ETL logic implemented and working
- [x] Cleaned data saved in mock S3
- [x] API exposes sample data
- [x] Swagger UI running
- [x] Unit tests written
- [x] Docker container works (optional)
- [x] Airflow DAG present (optional)

---

## 📅 Submission Date

**June 26, 2025**
