import json

# Path to the JSON file
file_path = '../../src/data/teams.json'

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
