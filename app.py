
# FastAPI app for serving the Cats vs Dogs model
from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io


import time
import logging
from prometheus_fastapi_instrumentator import Instrumentator
from src.inference import predict_image




# Configure logging to file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
    handlers=[
        logging.FileHandler("logs/app.log", mode="a"),
        logging.StreamHandler()
    ]
)

# Use a module-level logger
logger = logging.getLogger(__name__)


# Initialize FastAPI app
app = FastAPI()

# Prometheus metrics integration
Instrumentator().instrument(app).expose(app, endpoint="/metrics")


# Counter for requests (for logging)
REQUEST_COUNT = 0


# Health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}



# Prediction endpoint: accepts an image file and returns prediction
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read image from uploaded file
        image = Image.open(io.BytesIO(await file.read()))
        # Run inference
        prob, label = predict_image(image)
        logger.info(f"Prediction: label={label}, probability={prob}")
        return {
            "probability": prob,
            "label": label
        }
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=str(e))



# Middleware to log request count and latency
@app.middleware("http")
async def log_requests(request, call_next):
    global REQUEST_COUNT
    REQUEST_COUNT += 1
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    logger.info(f"Requests={REQUEST_COUNT}, Path={request.url.path}, Latency={duration:.4f}s, Status={response.status_code}")
    return response
