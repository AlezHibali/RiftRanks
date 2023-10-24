import json
import csv

# Path to the JSON file
file_path = 'D:\Coding\LOL_Ranking\inc\Teams.json'

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
    
def id_to_acronym(input_team_id):
    if input_team_id in teams_mapping:
        team_info = teams_mapping[input_team_id]
        return team_info['acronym']
    else:
        return input_team_id
    
def id_to_slug(input_team_id):
    if input_team_id in teams_mapping:
        team_info = teams_mapping[input_team_id]
        return team_info['slug']
    else:
        return input_team_id


# column now: team_name long_official_team_id match_numbers champion_kills_per_game first_baron_rate winning_rate net_building_destroyed_per_game epic_monster_killed_per_game vision_scores_per_game
# column processed: team_name team_acronym champion_kills_per_game first_baron_rate winning_rate net_building_destroyed_per_game epic_monster_killed_per_game vision_scores_per_game team_capital_letter team_combat_capacity reference_label


# Open the original CSV file for reading
with open('D:\\Coding\\LOL_Ranking\\output\\front_end_data.csv', mode='r') as infile:
    reader = csv.reader(infile)
    
    # Create a new CSV file for writing
    with open('D:\\Coding\\LOL_Ranking\\output\\front_end_data_11c_version.csv', mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Write the header to the new CSV file
        writer.writerow(['team_name', 'team_acronym', 'champion_kills_per_game', 
                         'first_baron_rate', 'winning_rate', 
                         'net_building_destroyed_per_game', 
                         'epic_monster_killed_per_game', 'vision_scores_per_game', 
                         'team_capital_letter', 'team_combat_capacity', 'reference_label'])

        # Skip the header of the original CSV
        next(reader)

        # Process each row in the original CSV
        for row in reader:
            team_name = row[0]
            long_official_team_id = row[1]
            champion_kills_per_game = row[3]
            first_baron_rate = row[4]
            winning_rate = row[5]
            net_building_destroyed_per_game = row[6]
            epic_monster_killed_per_game = row[7]
            vision_scores_per_game = row[8]

            # Convert long_official_team_id to team_acronym using the provided function
            team_acronym = id_to_acronym(long_official_team_id)

            # Get the first letter of the team_name in uppercase
            team_capital_letter = team_name[0].upper() if team_name else ''

            # team_combat_capacity has the same data as winning_rate
            team_combat_capacity = winning_rate

            # reference_label has the same data as team_name
            reference_label = team_name

            # Write the processed data to the new CSV file
            writer.writerow([team_name, team_acronym, champion_kills_per_game, 
                             first_baron_rate, winning_rate, 
                             net_building_destroyed_per_game, 
                             epic_monster_killed_per_game, vision_scores_per_game, 
                             team_capital_letter, team_combat_capacity, reference_label])