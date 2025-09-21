import tensorflow as tf
from preprocessing import test_data
import numpy as np
# Load trained model
model = tf.keras.models.load_model("saved_models/road_pavement_model.h5")
classes = list(test_data.class_indices.keys())
# Evaluate
loss, accuracy = model.evaluate(test_data)
print(f"✅ Test Accuracy: {accuracy*100:.2f}%")
# Optional: Predictions
predictions = model.predict(test_data)
predicted_classes = np.argmax(predictions, axis=1)
for i, pred_class in enumerate(predicted_classes):
    print(f"Image {i+1}: Predicted -> {classes[pred_class]}")