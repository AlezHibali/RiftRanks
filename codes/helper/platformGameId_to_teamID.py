import json
import teamID_to_teamName

# Load the JSON data from the file
with open('D:\Coding\LOL_Ranking\inc\mapping_data.json', 'r') as file:
    games = json.load(file)

# Function to get game info by platformGameId
def get_game_info(platformGameId):
    for game in games:
        if game['platformGameId'] == platformGameId:
            return {
                'esportsGameId': game['esportsGameId'],
                'teamMapping': game['teamMapping'],
                'participantMapping': game['participantMapping']
            }
    return None

# Test the function with a specific platformGameId
platformGameId = 'ESPORTSTMNT01:3413275'  # Change this to the actual platformGameId you want to look up
game_info = get_game_info(platformGameId)

team100Id = game_info['teamMapping']['100']
team200Id = game_info['teamMapping']['200']
print("Team 100 ID:", team100Id)
print("Team 200 ID:", team200Id)