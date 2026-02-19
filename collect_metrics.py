def predict_image(path):

# Script to collect post-deployment model performance metrics
import requests
import os
import logging
from PIL import Image
import io

# Configure logging to file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
    handlers=[
        logging.FileHandler("logs/collect_metrics.log", mode="a"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("collect_metrics")

# Simulated batch of test images and true labels
# Place real test images in tests/batch/ and update this list accordingly
BATCH = [
    ("tests/sample.jpg", "Cat"),
    # ("tests/dog1.jpg", "Dog"),
    # ("tests/cat2.jpg", "Cat"),
]

API_URL = os.environ.get("API_URL", "http://localhost:8000/predict")

results = []
correct = 0

# Function to send image to API and get prediction
def predict_image(path):
    try:
        with open(path, "rb") as f:
            files = {"file": (os.path.basename(path), f, "image/jpeg")}
            r = requests.post(API_URL, files=files)
            if r.status_code == 200:
                label = r.json().get("label")
                logger.info(f"Predicted {label} for {path}")
                return label
            else:
                logger.error(f"Error for {path}: {r.text}")
                return None
    except Exception as e:
        logger.error(f"Exception for {path}: {e}")
        return None

# Run batch predictions and collect results
for img_path, true_label in BATCH:
    pred_label = predict_image(img_path)
    results.append((img_path, true_label, pred_label))
    if pred_label == true_label:
        correct += 1

accuracy = correct / len(BATCH) if BATCH else 0

# Write results to file
with open("logs/post_deploy_metrics.txt", "w") as f:
    f.write("image,true_label,pred_label\n")
    for row in results:
        f.write(f"{row[0]},{row[1]},{row[2]}\n")
    f.write(f"\nAccuracy: {accuracy}\n")

logger.info(f"Post-deployment batch accuracy: {accuracy}")
print(f"Post-deployment batch accuracy: {accuracy}")
