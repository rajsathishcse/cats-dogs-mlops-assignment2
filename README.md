# Cats vs Dogs MLOps Project

## Overview
This project implements an end-to-end MLOps pipeline for binary image classification (Cats vs Dogs) for a pet adoption platform. The pipeline covers model building, artifact/image creation, packaging, containerization, and CI/CD-based deployment using open-source tools.

- **Use case:** Binary image classification (Cats vs Dogs)
- **Dataset:** Kaggle Cats and Dogs dataset
- **Image Preprocessing:** 224x224 RGB images for standard CNNs
- **Data Split:** Train/Validation/Test (e.g., 80%/10%/10%)
- **Data Augmentation:** Applied for better generalization

---

## M1: Model Development & Experiment Tracking
**Objective:** Build a baseline model, track experiments, and version all artifacts.

### 1. Data & Code Versioning
- Use **Git** for source code versioning (project structure, scripts, and notebooks).
- Use **DVC** for dataset versioning and to track pre-processed data.
- DVC pipelines (`dvc.yaml`) automate preprocessing and training for reproducibility.

### 2. Model Building
- Implement at least one baseline model (e.g., simple CNN or logistic regression on flattened pixels).
- Save the trained model in a standard serialized format (`.h5`, `.pt`, `.pkl`).
- Organize models in a dedicated directory (e.g., `models/` or `artifacts/`).

### 3. Experiment Tracking
- Use **MLflow** to log runs, parameters, metrics (accuracy, loss), and artifacts (confusion matrix, loss curves).
- Register models in MLflow’s model registry for easy deployment and versioning.

---

## Best Practices & Tips
- Use `.gitignore` and `.dvcignore` to avoid tracking unnecessary files.
- Document your pipeline and usage instructions in this README.
- For data augmentation, use Keras’ `ImageDataGenerator` or PyTorch’s `transforms`.
- Automate environment setup with `requirements.txt` or `environment.yml`.

---

_Continue to add details for each pipeline stage as you progress (data prep, training, deployment, etc.)._

---

## Local CI/CD Demo

This project includes a local CI/CD workflow file (`ci-demo.yml`) that demonstrates the full pipeline: testing, Docker build, and smoke testing the API endpoints.

### How to Use

You can use this file as a reference for your own CI/CD setup, or run the steps manually for demo purposes:

1. **Run tests:**
	```bash
	pytest
	```
2. **Build Docker image:**
	```bash
	docker build -t cats-dogs-mlops .
	```
3. **Start with Docker Compose:**
	```bash
	docker-compose up -d
	```
4. **Smoke test the API:**
	```bash
	curl -f http://localhost:8000/health
	curl -f -X POST "http://localhost:8000/predict" -F "file=@tests/sample.jpg"
	```

The same steps are automated in the `ci-demo.yml` file for demonstration or CI/CD learning purposes.

---

## Monitoring, Logging & Post-Deployment Metrics

### Logging & Monitoring
- All API requests, responses, and errors are logged to both the console and log files in the `logs/` directory (e.g., `logs/app.log`).
- The inference service tracks request count and latency in logs for basic monitoring.

### Post-Deployment Model Performance
- Use the provided `collect_metrics.py` script to send a batch of requests to the deployed API and compare predictions with true labels.
- Results and accuracy are saved to `logs/post_deploy_metrics.txt`.

#### Example usage:
```bash
python collect_metrics.py
cat logs/post_deploy_metrics.txt
```

You can add more test images and true labels in `collect_metrics.py` for a more comprehensive evaluation.

---

## Running the API

### Local
```bash
uvicorn app:app --reload
```
or
```bash
python -m uvicorn app:app --reload
```

### Docker
Build and run the container:
```bash
docker build -t cats-dogs-mlops .
docker run -p 8000:8000 cats-dogs-mlops
```
Or with docker-compose:
```bash
docker-compose up --build
```

### API Endpoints
- `GET /health` — Health check
- `POST /predict` — Predict cat/dog from image file

- `GET /metrics` — Prometheus metrics endpoint (for monitoring)

#### Example: Predict with curl
```bash

## Prometheus & Grafana Monitoring

### Prometheus
- A sample `prometheus.yml` is provided to scrape metrics from the FastAPI service at `/metrics`.
- To run Prometheus locally:
	1. [Download Prometheus](https://prometheus.io/download/)
	2. Place `prometheus.yml` in the Prometheus directory.
	3. Start Prometheus:
		 ```bash
		 ./prometheus --config.file=prometheus.yml
		 ```
	4. Visit [http://localhost:9090](http://localhost:9090) to view metrics.

### Grafana (Optional)
- Add Prometheus as a data source in Grafana.
- Create dashboards to visualize request count, latency, and other metrics.

This enables real-time monitoring of your deployed ML API.
curl -X POST "http://localhost:8000/predict" -F "file=@path_to_image.jpg"
```

#### FastAPI Docs
Interactive docs available at [http://localhost:8000/docs](http://localhost:8000/docs)

