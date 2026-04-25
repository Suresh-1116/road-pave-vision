import os

train_dir = "dataset/train"
for folder in os.listdir(train_dir):
    count = len(os.listdir(os.path.join(train_dir, folder)))
    print(f"{folder}: {count} images")