import csv
import ast
import random
from sklearn.metrics.pairwise import cosine_similarity


def parse_embedding(embedding_str):
    embedding_dict = ast.literal_eval(embedding_str)
    return embedding_dict['embedding']


def calculate_similarity(embedding1, embedding2):
    return cosine_similarity([embedding1], [embedding2])[0][0]


def read_csv(file_path):
    data = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['Embedding'] = parse_embedding(row['Embedding'])
                data.append(row)
    except FileNotFoundError:
        print("Directory not found:", file_path)
    return data

# true_pairs = [
#     ("Karin_Viard_1_embeddings.csv", "Karin_Viard_3_embeddings.csv"),
#     ("Keira_Knightley_3_embeddings.csv", "Keira_Knightley_1_embeddings.csv"),
#     ("Laura_Pausini_0_embeddings.csv", "Laura_Pausini_2_embeddings.csv"),
#     ("Lin_Yung_Hsi_3_embeddings.csv", "Lin_Yung_Hsi_4_embeddings.csv"),
#     ("Mahathir_Mohamad_1_embeddings.csv", "Mahathir_Mohamad_0_embeddings.csv"),
#     ("Mark_Dacey_0_embeddings.csv", "Mark_Dacey_3_embeddings.csv"),
#     ("Narendra_Modi_2_embeddings.csv", "Narendra_Modi_3_embeddings.csv"),
#     ("Natalia_Vodonova_0_embeddings.csv", "Natalia_Vodonova_2_embeddings.csv"),
#     ("Orlando_Bloom_5_embeddings.csv", "Orlando_Bloom_0_embeddings.csv"),
#     ("Oscar_Elias_Biscet_0_embeddings.csv", "Oscar_Elias_Biscet_5_embeddings.csv")
# ]
#
# false_pairs = [
#     ("Laura_Bush_5_embeddings.csv", "Nancy_Reagan_3_embeddings.csv"),
#     ("Katharine_Hepburn_1_embeddings.csv", "Kristen_Breitweiser_5_embeddings.csv"),
#     ("Linda_Dano_3_embeddings.csv", "Nina_Jacobson_3_embeddings.csv"),
#     ("Kristin_Scott_4_embeddings.csv", "Leticia_Dolera_4_embeddings.csv"),
#     ("Louis_Van_Gaal_1_embeddings.csv", "Newt_Gingrich_1_embeddings.csv"),
#     ("Kristy_Curry_2_embeddings.csv", "Mariana_Ohata_2_embeddings.csv"),
#     ("Liu_Ye_5_embeddings.csv", "Martin_Landau_2_embeddings.csv"),
#     ("Mark_Foley_4_embeddings.csv", "Nobuyuki_Idei_1_embeddings.csv"),
#     ("Margaret_Thatcher_5_embeddings.csv", "Maria_Callas_1_embeddings.csv"),
#     ("Natalia_Verbeke_5_embeddings.csv", "Ornella_Muti_0_embeddings.csv"),
# ]

true_pairs = [
    ("Karin_Viard_1_embeddings.csv", "Karin_Viard_3_embeddings.csv"),
    ("Keira_Knightley_3_embeddings.csv", "Keira_Knightley_1_embeddings.csv"),
    ("Laura_Pausini_0_embeddings.csv", "Laura_Pausini_2_embeddings.csv"),
    ("Lin_Yung_Hsi_3_embeddings.csv", "Lin_Yung_Hsi_4_embeddings.csv"),
    ("Mahathir_Mohamad_1_embeddings.csv", "Mahathir_Mohamad_0_embeddings.csv"),
    ("Mark_Dacey_0_embeddings.csv", "Mark_Dacey_3_embeddings.csv"),
    ("Narendra_Modi_2_embeddings.csv", "Narendra_Modi_3_embeddings.csv"),
    ("Natalia_Vodonova_0_embeddings.csv", "Natalia_Vodonova_2_embeddings.csv"),
    ("Orlando_Bloom_5_embeddings.csv", "Orlando_Bloom_0_embeddings.csv"),
    ("Oscar_Elias_Biscet_0_embeddings.csv", "Oscar_Elias_Biscet_5_embeddings.csv")
]

false_pairs = [
    ("Laura_Bush_5_embeddings.csv", "Nancy_Reagan_3_embeddings.csv"),
    ("Katharine_Hepburn_1_embeddings.csv", "Kristen_Breitweiser_5_embeddings.csv"),
    ("Linda_Dano_3_embeddings.csv", "Nina_Jacobson_3_embeddings.csv"),
    ("Kristin_Scott_4_embeddings.csv", "Leticia_Dolera_4_embeddings.csv"),
    ("aaa/embeddings-HOG/Luis_Fonsi_2", "aaa/embeddings-HOG/Martin_Landau_0"),
    ("Kristy_Curry_2_embeddings.csv", "Mariana_Ohata_2_embeddings.csv"),
    ("Liu_Ye_5_embeddings.csv", "Martin_Landau_2_embeddings.csv"),
    ("aaa/embeddings-HOG/Kit_Bond_3", "aaa/embeddings-HOG/Mario_Lobo_Zagallo_1"),
    ("Margaret_Thatcher_5_embeddings.csv", "Maria_Callas_1_embeddings.csv"),
    ("Natalia_Verbeke_5_embeddings.csv", "Ornella_Muti_0_embeddings.csv"),
]

all_similarities = []
for pair in false_pairs:
    csv1_data = read_csv(pair[0])
    csv2_data = read_csv(pair[1])

    similarities = []
    for row1 in csv1_data:
        for row2 in csv2_data:
            similarity = calculate_similarity(row1['Embedding'], row2['Embedding'])
            similarities.append((pair[0], row1['Filename'], pair[1], row2['Filename'], similarity))

    all_similarities.extend(similarities)


top_max_similarity = []
csv_files_added = set()
for pair in sorted(all_similarities, key=lambda x: x[4], reverse=True):
    if pair[0] not in csv_files_added and pair[2] not in csv_files_added:
        # Check if neither of the CSV files is already in top_max_similarity
        if pair[0] not in [p[0] for p in top_max_similarity] and pair[2] not in [p[2] for p in top_max_similarity]:
            top_max_similarity.append(pair)
            csv_files_added.add(pair[0])
            csv_files_added.add(pair[2])
    if len(top_max_similarity) == 5:
        break


top_min_similarity = []
csv_files_added = set()
for pair in sorted(all_similarities, key=lambda x: x[4]):
    if pair[0] not in csv_files_added and pair[2] not in csv_files_added:
        if pair[0] not in [p[0] for p in top_min_similarity] and pair[2] not in [p[2] for p in top_min_similarity]:
            top_min_similarity.append(pair)
            csv_files_added.add(pair[0])
            csv_files_added.add(pair[2])
    if len(top_min_similarity) == 5:
        break

average_similarity = sum(x[4] for x in all_similarities) / len(all_similarities)

top_random_similarity = random.sample(all_similarities, 5)

print("Top 5 pairs for max similarity:")
for pair in top_max_similarity:
    print("Pair:", pair[:4])
    print("Similarity:", pair[4])
    print()

print("Top 5 pairs for min similarity:")
for pair in top_min_similarity:
    print("Pair:", pair[:4])
    print("Similarity:", pair[4])
    print()

print("Average similarity:", average_similarity)
print()

print("Top 5 random pairs:")
for pair in top_random_similarity:
    print("Pair:", pair[:4])
    print("Similarity:", pair[4])
    print()
