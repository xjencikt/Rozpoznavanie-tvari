import os
import numpy as np
import csv
from PIL import Image
from deepface import DeepFace

def get_image_paths(root_dir):
    image_paths = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                image_path = os.path.join(root, file)
                image_paths.append(image_path)

    return image_paths


root_dir = "../BIOM2/normalized_faces_mtcnn/Karin_Viard_1"

image_paths = get_image_paths(root_dir)

features = []

for image_path in image_paths:
    image = Image.open(image_path)
    resized_image = image.resize((image.width * 2, image.height * 2), Image.LANCZOS)
    resized_image_path = "resized_image.jpg"
    resized_image.save(resized_image_path)
    image_features = DeepFace.represent(img_path=resized_image_path, model_name="VGG-Face", enforce_detection=False)
    if isinstance(image_features, list):
        image_features = np.array(image_features)
    if image_features.shape[0] != 1 or image_features.shape[0] != 2:
        image_features = np.resize(image_features, (1,))
    features.append(image_features.flatten())

    os.remove(resized_image_path)

features = np.array(features)


csv_file = "../BIOM2/true_features/Karin_Viard_1.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(features)

