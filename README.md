# 🛣️ Road Pave Vision
 
A CNN-based road pavement detection system using **MobileNetV2 Transfer Learning** that classifies road images as **Good**, **Cracked**, or **Pothole** with **93.75% accuracy**.
 
---
 
## 📸 Demo
 
| Good Road | Cracked Road | Pothole |
|---|---|---|
| ![Good](screenshots/good_prediction.png) | ![Cracked](screenshots/cracked_prediction.png) | ![Pothole](screenshots/pothole_prediction.png) |
 
---
 
## 🚀 Features
 
- ✅ Real-time road condition detection from images
- ✅ Classifies roads as **Good**, **Cracked**, or **Pothole**
- ✅ Built with **MobileNetV2 Transfer Learning** for high accuracy
- ✅ Interactive **GUI** built with Tkinter
- ✅ Achieved **93.75% accuracy** on test dataset
- ✅ Supports any road image as input
---
 
## 🛠️ Tech Stack
 
| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **TensorFlow / Keras** | Deep learning framework |
| **MobileNetV2** | Transfer learning base model |
| **OpenCV** | Image processing |
| **Tkinter** | GUI development |
| **Pillow (PIL)** | Image handling |
| **NumPy** | Numerical computations |
 
---
 
## 📁 Project Structure
 
```
road-pave-vision/
├── dataset/
│   ├── train/
│   │   ├── cracked/
│   │   ├── good/
│   │   └── pothole/
│   ├── val/
│   │   ├── cracked/
│   │   ├── good/
│   │   └── pothole/
│   └── test/
│       ├── cracked/
│       ├── good/
│       └── pothole/
├── saved_models/
│   └── road_pavement_model.h5
├── screenshots/
│   ├── good_prediction.png
│   ├── cracked_prediction.png
│   └── pothole_prediction.png
├── demo.py
├── model.py
├── preprocessing.py
├── train.py
├── test.py
├── requirements.txt
└── README.md
```
 
---
 
## ⚙️ Installation & Setup
 
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Suresh-1116/road-pave-vision.git
cd road-pave-vision
```
 
### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```
 
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
 
### 4️⃣ Run the Demo
```bash
python demo.py
```
 
---
 
## 🏋️ Training the Model
 
If you want to retrain the model on your own dataset:
 
```bash
python train.py
```
 
Training uses **two phases:**
- **Phase 1** — Train only top layers (20 epochs)
- **Phase 2** — Fine-tune last 30 layers of MobileNetV2 (20 epochs)
---
 
## 📊 Model Performance
 
| Metric | Value |
|---|---|
| **Test Accuracy** | 93.75% |
| **Model Architecture** | MobileNetV2 + Custom Dense Layers |
| **Training Images** | 224 |
| **Validation Images** | 48 |
| **Test Images** | 35 |
| **Classes** | Cracked, Good, Pothole |
 
---
 
## 🧠 Model Architecture
 
```
MobileNetV2 (pretrained on ImageNet)
    ↓
GlobalAveragePooling2D
    ↓
Dense(256, relu)
    ↓
Dropout(0.5)
    ↓
Dense(128, relu)
    ↓
Dropout(0.3)
    ↓
Dense(3, softmax) → [Cracked, Good, Pothole]
```
 
---
 
## 📦 Requirements
 
```
tensorflow
opencv-python
Pillow
numpy
scipy
```
 
Install all with:
```bash
pip install -r requirements.txt
```
 
---
 
## 👨‍💻 Author
 
**V Suresh Kumar**
- 🎓 B.Tech CSE — Sri Venkateswara College of Engineering, Tirupati
- 💼 [LinkedIn](https://www.linkedin.com/in/suresh-kumar-43a458255/)
- 🐙 [GitHub](https://github.com/Suresh-1116)
---
 
## 📄 License
 
This project is open source and available under the [MIT License](LICENSE).
 
---
 
⭐ If you found this project helpful, please give it a star!
 