import numpy as np
import pandas as pd

data = pd.read_csv("../BIOM2/allFilesBothPairsMAXMIN.csv")

average_distances = []

for index, row in data.iterrows():
    similarities = np.array([float(x) for x in row["Similarities"].replace("[", "").replace("]", "").split()])

    distances = 1 - similarities

    average_distance = np.mean(distances)

    average_distances.append(average_distance)

data["Average Distance"] = average_distances

data.to_csv("allFilesBothPairsMAXMINDistances.csv", index=False)

print("Average distances calculated and saved to together_with_distances.csv.")
