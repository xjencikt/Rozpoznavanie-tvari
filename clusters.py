import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

data = pd.read_csv('../BIOM2/aaa/testja.csv')

folder = data['Folder']
filenames = data['Filename']
embeddings = data['Embedding'].apply(lambda x: np.array(eval(x)['embedding']))


def extract_person_name(folder_path):
    parts = folder_path.split('\\')[-1].split('_')
    if len(parts) >= 2:
        return parts[0] + ' ' + parts[1]
    else:
        return folder_path.split('\\')[-1]


num_clusters = 20
kmeans = KMeans(
    n_clusters=num_clusters,
    init='k-means++',  # Initialize centroids using k-means++
    max_iter=500,      # Maximum number of iterations
    tol=1e-6,          # Tolerance for convergence
    n_init=100         # Number of initializations
)
kmeans.fit(list(embeddings))

data['Cluster'] = kmeans.labels_

for cluster_id in range(num_clusters):
    cluster_indices = np.where(kmeans.labels_ == cluster_id)[0]
    cluster_persons = folder.iloc[cluster_indices].apply(extract_person_name).unique()

    num_images_to_display = min(10, len(cluster_persons))
    print(f"Cluster {cluster_id}:")

    included_persons = set()

    for i in range(num_images_to_display):
        for folder_name in folder.iloc[cluster_indices]:
            person_name = extract_person_name(folder_name)
            if person_name not in included_persons:
                person_filenames = filenames[folder.apply(extract_person_name) == person_name]
                for image_filename in person_filenames:
                    image_path = os.path.join(folder_name, image_filename)
                    try:
                        image = plt.imread(image_path)
                        plt.subplot(1, num_images_to_display, i + 1)
                        plt.imshow(image)
                        plt.axis('off')
                        print(f"  Person: {person_name}, Image: {image_filename}")
                        included_persons.add(person_name)
                        break
                    except FileNotFoundError:
                        print(f"  Image not found for {person_name}, trying another image...")
                        continue
                else:
                    print(f"  No available images found for {person_name}")
                break

    plt.show()
