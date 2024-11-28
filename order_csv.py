import csv

with open('../BIOM2/aaa/Facenet_results.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

sorted_data = sorted(data, key=lambda x: float(x[2].split("'distance': ")[1].split(",")[0]))

with open('../BIOM2/sorted_csv_file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sorted_data)
