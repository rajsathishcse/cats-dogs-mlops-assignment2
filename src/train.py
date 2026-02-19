
import mlflow
import mlflow.tensorflow
from src.preprocess import get_data_generators
from src.model import build_model
import logging


# Set up logger to log to file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
    handlers=[
        logging.FileHandler("logs/train.log", mode="a"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("train")

mlflow.set_experiment("cats_vs_dogs")

logger.info("Loading data generators...")
train, val, test = get_data_generators(
    "data/train",
    "data/val",
    "data/test"
)

with mlflow.start_run():
    logger.info("Building model...")
    model = build_model()
    logger.info("Starting training...")
    history = model.fit(train, validation_data=val, epochs=20)

    logger.info("Evaluating on test set...")
    loss, acc = model.evaluate(test)
    logger.info(f"Test accuracy: {acc}")

    mlflow.log_metric("accuracy", acc)
    mlflow.tensorflow.log_model(model, "model")

    logger.info("Saving model to model.h5...")
    model.save("model.h5")
