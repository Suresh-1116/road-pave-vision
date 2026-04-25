import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import tensorflow as tf
# Load model
model = tf.keras.models.load_model("saved_models/road_pavement_model.h5")
classes = ["cracked", "good", "pothole"]
# Function to upload and predict
def upload_and_predict():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    img = cv2.imread(file_path)
    img_resized = cv2.resize(img, (224,224)) / 255.0
    img_input = np.expand_dims(img_resized, axis=0)
    pred = model.predict(img_input)
    class_idx = np.argmax(pred)
    pred_class = classes[class_idx]
    color = (0, 255, 0) if pred_class=="good" else (0, 255, 255) if pred_class=="cracked" else (0,0,255)
    cv2.putText(img, f"Prediction: {pred_class}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)
    image_label.config(image=img_tk)
    image_label.image = img_tk
    result_label.config(text=f"Prediction: {pred_class}")
# GUI setup
root = tk.Tk()
root.title("Road Pavement Detection")
upload_btn = tk.Button(root, text="Upload Road Image",
command=upload_and_predict)
upload_btn.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(pady=10)
image_label = tk.Label(root)
image_label.pack()
root.mainloop()
 