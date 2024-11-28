import os
import numpy as np
import csv
from deepface import DeepFace

def get_image_paths(root_dir):
    image_paths = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                image_path = os.path.join(root, file)
                image_paths.append((root, file, image_path))

    return image_paths


def process_images_in_folder_and_save(folder_name):
    image_paths = get_image_paths(os.path.join("../BIOM2/normalized_faces_mtcnn_cropped", folder_name))
    features = []

    for folder, filename, image_path in image_paths:
        try:
            image_features = DeepFace.represent(img_path=image_path, model_name="Facenet512", enforce_detection=True,
                                                detector_backend="mtcnn")
        except ValueError as e:
            print(f"No face found in {filename}. Skipping.")
            continue

        if isinstance(image_features, list):
            image_features = np.array(image_features)

        features.append(np.concatenate([[folder, filename], image_features.flatten()]))

    features = np.array(features)

    csv_file = f"aaa/embeddings/{folder_name}_features.csv"
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Folder", "Filename", "Embedding"])
        writer.writerows(features)

folders_to_process = [
    "Karin_Viard_1","Karin_Viard_3","Katharine_Hepburn_1", "Kristen_Breitweiser_5",
    "Keira_Knightley_3","Keira_Knightley_1","Linda_Dano_3", "Nina_Jacobson_3",
    "Laura_Pausini_0","Laura_Pausini_2","Kristin_Scott_4", "Leticia_Dolera_4",
    "Lin_Yung_Hsi_3","Lin_Yung_Hsi_4","Louis_Van_Gaal_1", "Newt_Gingrich_1",
    "Mahathir_Mohamad_1","Mahathir_Mohamad_0","Kristy_Curry_2", "Mariana_Ohata_2",
    "Mark_Dacey_0","Mark_Dacey_3","Liu_Ye_5", "Martin_Landau_2",
    "Narendra_Modi_2","Narendra_Modi_3","Mark_Foley_4", "Nobuyuki_Idei_1",
    "Natalia_Vodonova_0","Natalia_Vodonova_2","Margaret_Thatcher_5", "Maria_Callas_1",
    "Orlando_Bloom_5","Orlando_Bloom_0","Natalia_Verbeke_5", "Ornella_Muti_0",
    "Oscar_Elias_Biscet_0","Oscar_Elias_Biscet_5","Laura_Bush_5", "Nancy_Reagan_3"
]

for folder_name in folders_to_process:
    process_images_in_folder_and_save(folder_name)
