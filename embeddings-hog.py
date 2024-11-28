import cv2
import os
import pandas as pd
from tqdm import tqdm


def extract_hog_features(image_path):
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (64, 128))
    hog = cv2.HOGDescriptor()
    hog_features = hog.compute(resized_image)
    return hog_features.flatten()


file = "Ornella_Muti_0"
folder_path = "normalized_faces_mtcnn_cropped/" + file

data = []

for filename in tqdm(os.listdir(folder_path)):
    if filename.endswith(".jpg"):
        image_path = os.path.join(folder_path, filename)
        embedding = extract_hog_features(image_path)
        embedding_dict = {'embedding': embedding.tolist()}
        data.append([folder_path, filename, embedding_dict])

df = pd.DataFrame(data, columns=["Folder", "Filename", "Embedding"])
df.to_csv("aaa/embeddings-HOG/embeddings" + file + ".csv", index=False)
