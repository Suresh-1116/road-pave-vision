import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# Dataset paths
train_dir = "dataset/train"
val_dir = "dataset/val"
test_dir = "dataset/test"
# Image settings
IMG_HEIGHT = 224
IMG_WIDTH = 224
BATCH_SIZE = 32
# Preprocessing
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)
# Load datasets
train_data = train_datagen.flow_from_directory(
train_dir,
target_size=(IMG_HEIGHT, IMG_WIDTH),
batch_size=BATCH_SIZE,
class_mode="categorical"
)
val_data = val_datagen.flow_from_directory(
val_dir,
target_size=(IMG_HEIGHT, IMG_WIDTH),
batch_size=BATCH_SIZE,
class_mode="categorical"
)
test_data = test_datagen.flow_from_directory(
test_dir,
target_size=(IMG_HEIGHT, IMG_WIDTH),
batch_size=BATCH_SIZE,
class_mode="categorical",
shuffle=False
)
print("✅ Dataset preprocessing complete"
)
print("Classes:", train_data.class_indices)