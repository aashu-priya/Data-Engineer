# Data-Engineer
## Objective

Design and build a complete data engineering pipeline that:
- Ingests raw data from a CSV file using **PySpark**
- Cleans and processes the data (e.g., deduplication, null handling, feature engineering)
- Saves the transformed data to local storage (mock S3 bucket)
- Serves the cleaned data through a RESTful **FastAPI** service
- Includes unit tests and optional orchestration (e.g., Airflow)

---

##  Project Structure
```text
Data-Engineer/
├── airflow/
│   └── dags/
│       └── etl_dag.py
├── api/
│   ├── __init__.py
│   ├── endpoints.py
│   ├── main.py
│   └── models.py
├── data/
│   └── .gitkeep
├── mock_s3/
│   └── processed_data.csv
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_processor.py
│   ├── etl_pipeline.py
│   └── s3_utils.py
├── tests/
│   ├── conftest.py
│   ├── test_api.py
│   ├── test_data_processor.py
│   └── test_etl.py
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
├── requirements.txt
└── submission.md
```

---

## 🛠️ Getting Started

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

Download a CSV dataset (at least 1000+ rows with some missing/duplicate values) and save it as:

```bash
data/raw_data.csv
```

### 5. Run the ETL Pipeline

This reads the raw data, processes it using PySpark, and stores the cleaned data in a mock S3 bucket (`mock_s3/`):

```bash
PYTHONPATH=. python src/etl_pipeline.py
```

### 6. Launch the FastAPI Server

```bash
uvicorn api.main:app --reload
```

Then open your browser and visit:

```
http://127.0.0.1:8000/docs
```

This will open the Swagger UI for testing the API.

### 7. Sample API Endpoint

Fetch 10 rows from the cleaned dataset:

```bash
curl "http://127.0.0.1:8000/data/sample?limit=10"
```

### 8. Run Unit Tests

```bash
pytest tests/
```

---

## 🐳 Optional: Docker Setup

### 9. Build Docker Containers

```bash
docker compose build
```

### 10. Run the Services

```bash
docker compose up
```

### 11. Access Container for Debugging

```bash
docker compose run --service-ports api bash
```

---

## ⛓️ Optional: Airflow Orchestration

Airflow DAG is defined in:

```bash
airflow/dags/etl_dag.py
```

You can set up a local Airflow environment or mock the structure for demonstration purposes.
