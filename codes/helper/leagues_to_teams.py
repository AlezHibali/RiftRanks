import json
import teamID_to_teamName
from tournaments_to_teams import get_team_ids_from_tournament

# Load the JSON data from the file
with open('D:\Coding\LOL_Ranking\inc\leagues.json', 'r') as file_leagues:
    leagues = json.load(file_leagues)

league_name = ''

def get_team_ids_from_leagues(league_id):
    global league_name

    # Use a set to store team IDs to avoid duplicates
    teams = set()

    # Iterate through the tournaments and collect team IDs
    for league in leagues:
        if league['id'] == league_id:
            league_name = league['name']
            for tournament in league['tournaments']:
                teams.update(get_team_ids_from_tournament(tournament['id']))
                #print(list(teams))
    
    return list(teams)

# teams = get_team_ids_from_leagues('98767991299243165')

teams = get_team_ids_from_leagues('109518549825754242')
print("Team IDs for Leagues: ", league_name)
print(teams)