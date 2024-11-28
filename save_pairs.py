import csv

pairs = []

with open('../BIOM2/FalsePairs.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        pair = tuple('aaa/allFiles/' + item.split('.')[0] for item in row)
        pairs.append(pair)

print(pairs)


