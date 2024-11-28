import os
import random
import pandas as pd
from deepface import DeepFace

def compare_and_save_to_csv(pair, csv_filename):
    dir1 = pair[0]
    dir2 = pair[1]
    results = []
    distances = []

    dir1_files = random.sample(os.listdir(dir1), min(5, len(os.listdir(dir1))))
    dir2_files = random.sample(os.listdir(dir2), min(5, len(os.listdir(dir2))))

    for file1 in dir1_files:
        if file1.endswith(".jpg") or file1.endswith(".jpeg"):
            for file2 in dir2_files:
                if file2.endswith(".jpg") or file2.endswith(".jpeg"):
                    img1_path = os.path.join(dir1, file1)
                    img2_path = os.path.join(dir2, file2)
                    result = DeepFace.verify(img1_path=img1_path,
                                             img2_path=img2_path,
                                             model_name="Facenet",
                                             detector_backend="mtcnn",
                                             threshold=0.5,)

                    results.append({"Folder1": dir1, "Image1": file1,"Folder2": dir2, "Image2": file2, "Result": result})
                    distances.append(result["distance"])

    max_distance = max(distances)
    min_distance = min(distances)
    avg_distance = sum(distances) / len(distances)

    distances.remove(max_distance)
    distances.remove(min_distance)

    random_distance = random.choice(distances)

    df = pd.DataFrame(results)

    df['isCorrect'] = True

    df.to_csv(csv_filename, mode='a', index=False, header=not os.path.exists(csv_filename))

    return min_distance, max_distance, avg_distance, random_distance



pairs = [
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

csv_filename = "../rozpoznavanieTvari/rozpoznavanie.csv"

for pair in true_pairs:
    min_distance, max_distance, avg_distance, random_distance = compare_and_save_to_csv(pair, csv_filename)
    min_distance_rounded = round(min_distance, 3)
    max_distance_rounded = round(max_distance, 3)
    avg_distance_rounded = round(avg_distance, 3)
    random_distance_rounded = round(random_distance, 3)

    print("Pair:", pair)
    print("Randomly selected distance (not max or min):", random_distance_rounded)
    print("Average Distance:", avg_distance_rounded)
    print("Maximum Distance:", max_distance_rounded)
    print("Minimum Distance:", min_distance_rounded)
