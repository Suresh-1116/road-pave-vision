from preprocessing import train_data, val_data
from model import build_cnn
import tensorflow as tf
# Build model
model = build_cnn(input_shape=(224,224,3), num_classes=3)
# Train
history = model.fit(train_data, validation_data=val_data, epochs=10)
# Save model
model.save("saved_models/road_pavement_model.h5")
print("✅ Model training complete and saved")
 