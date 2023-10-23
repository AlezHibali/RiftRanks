import pandas as pd
import json

# Path to the JSON file
file_path = '../../src/data/dummy_team_table.csv'

# Read the JSON file
with open(file_path, 'r') as file:
    teams_data = json.load(file)

# Create a dictionary to hold the team_id as key and name, acronym as value
teams_mapping = {}

# Process each team in the JSON data
for team in teams_data:
    team_id = team['team_id']
    name = team['name']
    acronym = team['acronym']
    slug = team['slug']
    
    # Store the name and acronym in the dictionary, indexed by team_id
    teams_mapping[team_id] = {'name': name, 'acronym': acronym, 'slug': slug}


def id_to_name(input_team_id):
    if input_team_id in teams_mapping:
        team_info = teams_mapping[input_team_id]
        return team_info['name']
    else:
        return input_team_id

# Read the CSV file
df = pd.read_csv('D:\Coding\LOL_Ranking\inc\dummy_team_table.csv')

# Apply the id_to_name function to the long_official_team_id column
df['team name'] = df['long_official_team_id'].astype(str).apply(id_to_name)

# Write the updated DataFrame back to a new CSV file
df.to_csv('updatedfile.csv', index=False)

# Print the updated DataFrame to console (optional)
print(df)