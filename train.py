from preprocessing import train_data, val_data
from model import build_transfer_model
import tensorflow as tf
import os

# Create saved_models directory if not exists
os.makedirs("saved_models", exist_ok=True)

# Build model
model, base_model = build_transfer_model(input_shape=(224,224,3), num_classes=3)

print("✅ Phase 1 — Training top layers only...")

# Callbacks
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.2,
    patience=3,
    min_lr=0.00001
)

# Phase 1 — Train only top layers
history1 = model.fit(
    train_data,
    validation_data=val_data,
    epochs=20,
    callbacks=[early_stopping, reduce_lr]
)

print("✅ Phase 2 — Fine tuning base model...")

# Phase 2 — Unfreeze last 30 layers and fine tune
base_model.trainable = True
for layer in base_model.layers[:-30]:
    layer.trainable = False

# Recompile with lower learning rate
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.00001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

history2 = model.fit(
    train_data,
    validation_data=val_data,
    epochs=20,
    callbacks=[early_stopping, reduce_lr]
)

# Save model
model.save("saved_models/road_pavement_model.h5")
print("✅ Model training complete and saved!")
print(f"Final val accuracy: {max(history2.history['val_accuracy'])*100:.2f}%")