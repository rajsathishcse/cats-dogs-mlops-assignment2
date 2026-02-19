
# Data generators for training, validation, and test sets
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Image size and batch size constants
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# Returns data generators for train, val, and test directories
def get_data_generators(train_dir, val_dir, test_dir):
    # Data augmentation for training
    train_gen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        zoom_range=0.2,
        horizontal_flip=True
    )

    # Only rescaling for validation and test
    val_test_gen = ImageDataGenerator(rescale=1./255)

    train = train_gen.flow_from_directory(
        train_dir,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='binary'
    )

    val = val_test_gen.flow_from_directory(
        val_dir,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='binary'
    )

    test = val_test_gen.flow_from_directory(
        test_dir,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='binary'
    )

    return train, val, test
