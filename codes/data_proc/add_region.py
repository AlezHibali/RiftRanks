import json
import csv
from teamID_to_teamName import id_to_name

# Read and load the JSON content from the file
with open('D:\\Coding\\LOL_Ranking\\inc\\Tournaments.json', 'r') as file_tournaments:
    tournaments = json.load(file_tournaments)
with open('D:\\Coding\\LOL_Ranking\\inc\\leagues.json', 'r') as file_leagues:
    leagues = json.load(file_leagues)

def get_team_ids_from_tournament(tournament_id):
    # Use a set to store team IDs to avoid duplicates
    team_ids = set()

    # Iterate through the tournaments and collect team IDs
    for tournament in tournaments:
        if tournament['id'] == tournament_id:
            for stage in tournament['stages']:
                for section in stage['sections']:
                    for match in section['matches']:
                        for team in match['teams']:
                            id = id_to_name(team['id'])
                            team_ids.add(id)

    return list(team_ids)

def get_team_ids_from_leagues(league_id):
    # Use a set to store team IDs to avoid duplicates
    teams = set()

    # Iterate through the tournaments and collect team IDs
    league_name = ''
    region_name = ''
    for league in leagues:
        if league['id'] == league_id:
            league_name = league['name']
            region_name = league['region']
            for tournament in league['tournaments']:
                teams.update(get_team_ids_from_tournament(tournament['id']))

    return list(teams), league_name, region_name

# Creating a dictionary with team names as keys and their corresponding leagues as values
team_to_league = {}
team_to_region = {}

for league in leagues:
    league_id = league['id']
    teams, league_name, region_name = get_team_ids_from_leagues(league_id)
    for team in teams:
        team_to_league[team] = league_name
        team_to_region[team] = region_name


input_file = 'D:\\Coding\\LOL_Ranking\\output\\front_end_data_11c_version.csv'
output_file = 'D:\\Coding\\LOL_Ranking\\output\\front_end_data_13c_version.csv'

# List to hold updated rows
updated_rows = []

with open(input_file, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Extract header from input CSV
    header = next(csvreader)
    header.extend(['league', 'region'])  # Add 'league' and 'region' columns
    updated_rows.append(header)

    # Process rows in the CSV
    for row in csvreader:
        team_name_column = row[0]  # Assuming 'team_name' is the first column
        league = team_to_league.get(team_name_column, "N/A")
        region = team_to_region.get(team_name_column, "N/A")
        
        # Append the 'league' and 'region' columns to the current row
        row.extend([league, region])
        updated_rows.append(row)

# Write the updated rows to the output CSV
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(updated_rows)