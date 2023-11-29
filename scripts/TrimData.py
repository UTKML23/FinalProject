# TrimData.py
# Noah Shoap
# Unzips the data.zip file, trims it down.

import pandas as pd
import zipfile

data_dir = '../data'
zip_path = f'{data_dir}/data.zip'

print(f'Unzipping {zip_path}.')

# I'm just doing this so the script works on a clean directory.
# I'm bored.
# Extract data.zip to files for trimming.
with zipfile.ZipFile(zip_path, 'r') as zipf:
    zipf.extractall(data_dir)

print('Reading JSON.')

# Read the game file.
game_file = f'{data_dir}/games_1512362753.8735218.json'
df = pd.read_json(game_file)

# min. year (inclusive)
year_cutoff = 2000

print('Trimming data.')

# trim to games since 2000
trimmed = df[df['year'] >= year_cutoff]

# save
json_file = '../data/trimmed_games.json'
trimmed.to_json(json_file)

print('Saved JSON file.')

# save trimmed_games.zip

zip_name = f'{data_dir}/trimmed_games.zip'

with zipfile.ZipFile(zip_name, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(json_file)

print('Saved trimmed ZIP file.')