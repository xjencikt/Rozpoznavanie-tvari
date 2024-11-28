import cv2
import numpy as np
import os
import csv

def compute_hog(image):
    hog = cv2.HOGDescriptor()
    features = hog.compute(image)
    features = features.flatten()
    return features

def compare_images(image1, image2):
    image1_resized = cv2.resize(image1, (64, 128))
    image2_resized = cv2.resize(image2, (64, 128))

    hog_features1 = compute_hog(image1_resized)
    hog_features2 = compute_hog(image2_resized)

    distance = np.linalg.norm(hog_features1 - hog_features2)
    normalized_distance = distance / (np.linalg.norm(hog_features1) + np.linalg.norm(hog_features2))
    return normalized_distance

false_pairs = [
    ("new_again/Laura_Bush_5", "new_again/Nancy_Reagan_3"),
    ("new_again/Katharine_Hepburn_1", "new_again/Kristen_Breitweiser_5"),
    ("new_again/Linda_Dano_3", "new_again/Nina_Jacobson_3"),
    ("new_again/Kristin_Scott_4", "new_again/Leticia_Dolera_4"),
    ("new_again/Louis_Van_Gaal_1", "new_again/Newt_Gingrich_1"),
    ("new_again/Kristy_Curry_2", "new_again/Mariana_Ohata_2"),
    ("new_again/Liu_Ye_5", "new_again/Martin_Landau_2"),
    ("new_again/Mark_Foley_4", "new_again/Nobuyuki_Idei_1"),
    ("new_again/Margaret_Thatcher_5", "new_again/Maria_Callas_1"),
    ("new_again/Natalia_Verbeke_5", "new_again/Ornella_Muti_0")
]

true_pairs = [
    ("new_again/Karin_Viard_1", "new_again/Karin_Viard_3"),
    ("new_again/Keira_Knightley_3", "new_again/Keira_Knightley_1"),
    ("new_again/Laura_Pausini_0", "new_again/Laura_Pausini_2"),
    ("new_again/Lin_Yung_Hsi_3", "new_again/Lin_Yung_Hsi_4"),
    ("new_again/Mahathir_Mohamad_1", "new_again/Mahathir_Mohamad_0"),
    ("new_again/Mark_Dacey_0", "new_again/Mark_Dacey_3"),
    ("new_again/Narendra_Modi_2", "new_again/Narendra_Modi_3"),
    ("new_again/Natalia_Vodonova_0", "new_again/Natalia_Vodonova_2"),
    ("new_again/Orlando_Bloom_5", "new_again/Orlando_Bloom_0"),
    ("new_again/Oscar_Elias_Biscet_0", "new_again/Oscar_Elias_Biscet_5")
]

threshold = 0.68


csv_filename = '../BIOM2/HOG/comparison_results.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Image1', 'Image2', 'Distance', 'Same Person', 'Threshold', 'IsCorrect'])

    for folder1_path, folder2_path in true_pairs:
        for filename1 in os.listdir(folder1_path):
            image1 = cv2.imread(os.path.join(folder1_path, filename1))
            gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

            for filename2 in os.listdir(folder2_path):
                image2 = cv2.imread(os.path.join(folder2_path, filename2))
                gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

                distance = compare_images(gray1, gray2)
                same_person = distance < threshold

                csv_writer.writerow([filename1, filename2, distance, same_person, threshold, True])
