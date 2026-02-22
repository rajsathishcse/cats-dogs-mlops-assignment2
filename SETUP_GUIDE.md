# MLOps Project Setup Guide

## 1. Clone the Repository
If you haven't already:
```
git clone https://github.com/rajsathishcse/cats-dogs-mlops-assignment2
cd cats-dogs-mlops
```

## 2. Create and Activate Virtual Environment
```
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

## 3. Install Requirements
```
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Run MLflow Tracking UI (optional)
```
python -m mlflow ui
# Visit http://localhost:5000
```

## 5. Run FastAPI with Uvicorn
```
python -m uvicorn app:app --reload
# Visit http://127.0.0.1:8000/docs
```

## 6. Run Metrics Collection Script
```
python collect_metrics.py
```

## 7. Run Tests and Lint
```
python -m pytest
python -m flake8 src/ --max-line-length=120
```

## 8. Build and Run Docker Container
```
docker build -t cats-dogs-mlops .
docker run -p 8000:8000 cats-dogs-mlops
```

## 9. Run Prometheus
- Download Prometheus from https://prometheus.io/download/
- Extract and open terminal in the folder with prometheus.exe
- Run:
```
./prometheus.exe --config.file="C:\Users\skumarp3\Documents\cats-dogs-mlops\cats-dogs-mlops\prometheus.yml"
```
- Visit http://localhost:9090

## 10. Run Grafana
- Download Grafana from https://grafana.com/grafana/download
- Extract and open terminal in the folder with grafana-server.exe
- Run:
```
bin\grafana-server.exe
```
- Visit http://localhost:3000
- Login (admin/admin)
- Add Prometheus as a data source
- Import grafana_dashboard.json

## 11. CI/CD (GitHub Actions)
- Push code to GitHub
- Workflow runs automatically (see .github/workflows/ci.yml)

---

**Troubleshooting:**
- If a command is not recognized, check your PATH or run from the correct directory.
- For Docker, Prometheus, and Grafana, you can use Docker Compose for easier setup.
- For Prometheus targets, check http://localhost:9090/targets.
- For API docs, visit http://127.0.0.1:8000/docs.

**Contact:**
- For issues, open a GitHub issue or ask your instructor.
