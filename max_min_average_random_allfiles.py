import pandas as pd
import numpy as np
import ast

df = pd.read_csv('../BIOM2/allFilesBothPairs.csv')

def extract_values(similarity_str):
    clean_str = similarity_str.replace('[', '').replace(']', '').replace('...', '').strip()
    return np.array([float(val) for val in clean_str.split()])



df['Similarities'] = df['Similarities'].apply(extract_values)

def find_values(similarities):
    random_value = np.random.choice(similarities)
    max_value = np.max(similarities)
    min_value = np.min(similarities)
    average_value = np.mean(similarities)
    return random_value, max_value, min_value, average_value

df['Random'] = df['Similarities'].apply(lambda x: find_values(x)[0])
df['Max'] = df['Similarities'].apply(lambda x: find_values(x)[1])
df['Min'] = df['Similarities'].apply(lambda x: find_values(x)[2])
df['Average'] = df['Similarities'].apply(lambda x: find_values(x)[3])

df.to_csv('allFilesBothPairsMAXMIN.csv', index=False)
