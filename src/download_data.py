import sys
import os
import subprocess

DATASET = "bhavikjikadara/dog-and-cat-classification-dataset"

os.makedirs("data/raw", exist_ok=True)


def check_kaggle_installed():
    """Check if Kaggle API is installed."""
    try:
        import kaggle  # noqa: F401
    except ImportError:
        print("Kaggle API is not installed. Please run 'pip install kaggle' and authenticate.")
        sys.exit(1)


def check_kaggle_authenticated():
    """Check if Kaggle API is authenticated."""
    kaggle_json = os.path.expanduser("~/.kaggle/kaggle.json")
    if not os.path.exists(kaggle_json):
        print("Kaggle API credentials not found. Please place kaggle.json in ~/.kaggle and set permissions.")
        sys.exit(1)


check_kaggle_installed()
check_kaggle_authenticated()

subprocess.run([
    "kaggle", "datasets", "download",
    "-d", DATASET,
    "-p", "data/raw",
    "--unzip"
])
