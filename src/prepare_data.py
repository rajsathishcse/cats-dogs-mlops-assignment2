
# Script to split raw dataset into train/val/test and copy images
import os
import shutil
import random
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
    handlers=[
        logging.FileHandler("logs/prepare_data.log", mode="a"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("prepare_data")

SRC = "data/raw/PetImages"
DEST = "data"

def is_image(filename):
    """Check if file is an image."""
    return filename.lower().endswith((".jpg", ".jpeg", ".png"))

def split_files(files):
    """Split files into train/val/test sets."""
    n = len(files)
    return files[:int(0.8 * n)], files[int(0.8 * n):int(0.9 * n)], files[int(0.9 * n):]

def safe_copy(src, dst):
    """Safely copy a file and log errors."""
    try:
        shutil.copy2(src, dst)
    except Exception as e:
        logger.error(f"Failed to copy {src} to {dst}: {e}")

# Script to split raw dataset into train/val/test and copy images
import os
import shutil
import random
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
    handlers=[
        logging.FileHandler("logs/prepare_data.log", mode="a"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("prepare_data")

SRC = "data/raw/PetImages"
DEST = "data"


def is_image(filename):
    """Check if file is an image."""
    return filename.lower().endswith((".jpg", ".jpeg", ".png"))


import os, shutil, random
    """Split files into train/val/test sets."""
    n = len(files)
    return files[:int(0.8 * n)], files[int(0.8 * n):int(0.9 * n)], files[int(0.9 * n):]



    """Safely copy a file and log errors."""
    try:
        shutil.copy(src, dst)
        logger.debug(f"Copied {src} to {dst}")
    except Exception as e:
        logger.error(f"Failed to copy {src} to {dst}: {e}")


# Create output directories for each split/class
for split in ["train", "val", "test"]:
    for cls in ["Cat", "Dog"]:
        os.makedirs(f"{DEST}/{split}/{cls}", exist_ok=True)

# List and filter image files
cats = [f for f in os.listdir(f"{SRC}/Cat") if is_image(f)]
dogs = [f for f in os.listdir(f"{SRC}/Dog") if is_image(f)]
logger.info(f"Found {len(cats)} cat images and {len(dogs)} dog images.")

# Shuffle for randomness
random.shuffle(cats)
random.shuffle(dogs)

cat_train, cat_val, cat_test = split_files(cats)
dog_train, dog_val, dog_test = split_files(dogs)
logger.info(f"Cat split: train={len(cat_train)}, val={len(cat_val)}, test={len(cat_test)}")
logger.info(f"Dog split: train={len(dog_train)}, val={len(dog_val)}, test={len(dog_test)}")

for f in cat_train:
    safe_copy(f"{SRC}/Cat/{f}", f"{DEST}/train/Cat/{f}")
for f in cat_val:
    safe_copy(f"{SRC}/Cat/{f}", f"{DEST}/val/Cat/{f}")
for f in cat_test:
    safe_copy(f"{SRC}/Cat/{f}", f"{DEST}/test/Cat/{f}")

for f in dog_train:
    safe_copy(f"{SRC}/Dog/{f}", f"{DEST}/train/Dog/{f}")
for f in dog_val:
    safe_copy(f"{SRC}/Dog/{f}", f"{DEST}/val/Dog/{f}")
for f in dog_test:
    safe_copy(f"{SRC}/Dog/{f}", f"{DEST}/test/Dog/{f}")
SRC = "data/raw/PetImages"
DEST = "data"

def is_image(filename):
    return filename.lower().endswith((".jpg", ".jpeg", ".png"))

for split in ["train", "val", "test"]:
    for cls in ["Cat", "Dog"]:
        os.makedirs(f"{DEST}/{split}/{cls}", exist_ok=True)

cats = os.listdir(f"{SRC}/Cat")
dogs = os.listdir(f"{SRC}/Dog")

cats = [f for f in os.listdir(f"{SRC}/Cat") if is_image(f)]
dogs = [f for f in os.listdir(f"{SRC}/Dog") if is_image(f)]

random.shuffle(cats)
random.shuffle(dogs)

def split_files(files):
    n = len(files)
    return files[:int(0.8*n)], files[int(0.8*n):int(0.9*n)], files[int(0.9*n):]

cat_train, cat_val, cat_test = split_files(cats)
dog_train, dog_val, dog_test = split_files(dogs)

for f in cat_train:
    shutil.copy(f"{SRC}/Cat/{f}", f"{DEST}/train/Cat/{f}")
for f in cat_val:
    shutil.copy(f"{SRC}/Cat/{f}", f"{DEST}/val/Cat/{f}")
for f in cat_test:
    shutil.copy(f"{SRC}/Cat/{f}", f"{DEST}/test/Cat/{f}")

for f in dog_train:
    shutil.copy(f"{SRC}/Dog/{f}", f"{DEST}/train/Dog/{f}")
for f in dog_val:
    shutil.copy(f"{SRC}/Dog/{f}", f"{DEST}/val/Dog/{f}")
for f in dog_test:
    shutil.copy(f"{SRC}/Dog/{f}", f"{DEST}/test/Dog/{f}")
