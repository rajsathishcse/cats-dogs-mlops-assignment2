
# Inference utilities for Cats vs Dogs model

import tensorflow as tf
import numpy as np
from PIL import Image
import logging

# Path to trained model
MODEL_PATH = "model.h5"
# Image size expected by the model
IMG_SIZE = (224, 224)


# Set up logger to log to file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
    handlers=[
        logging.FileHandler("logs/inference.log", mode="a"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("inference")

# Load model once at import
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    logger.info(f"Model loaded from {MODEL_PATH}")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    model = None


def preprocess_image(image: Image.Image):
    """
    Takes PIL image and returns model-ready numpy array
    """
    image = image.resize(IMG_SIZE)
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def predict_image(image: Image.Image):
    """
    Returns probability and label
    """
    if model is None:
        logger.error("Model is not loaded.")
        raise RuntimeError("Model is not loaded.")
    img = preprocess_image(image)
    try:
        pred = model.predict(img)[0][0]
        label = "Dog" if pred > 0.5 else "Cat"
        logger.info(f"Predicted: label={label}, probability={pred}")
        return float(pred), label
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise
