import pandas as pd

df = pd.read_csv('../BIOM2/txt_files/rectangle_coordinates.csv')

df = df.drop_duplicates(subset=['Folder', 'Image'])

df.to_csv('updated_file.csv', index=False)
