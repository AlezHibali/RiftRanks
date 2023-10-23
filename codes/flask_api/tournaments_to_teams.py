import json
import teamID_to_teamName
from teamID_to_teamName import id_to_name
import csv

# Read and load the JSON content from the file
with open('../../src/data/tournaments.json', 'r') as file_tournaments:
    tournaments = json.load(file_tournaments)
with open('../../src/data/leagues.json', 'r') as file_leagues:
    leagues = json.load(file_leagues)

tournaments_slug = ''
league_name = ''

def format_tournament_slug(slug):
    # Split the slug using underscores and capitalize each word
    words = slug.split('_')
    formatted_slug = ' '.join(word.capitalize() for word in words)
    return formatted_slug

def get_year_from_slug(slug):
    # Check if '2023', '2022', or '2021' appears in the slug
    if '2023' in slug:
        return '2023'
    elif '2022' in slug:
        return '2022'
    elif '2021' in slug:
        return '2021'
    elif '2020' in slug:
        return '2020'
    else:
        return 'Others'

def write_tournament_slugs_to_csv():
    # Open the CSV file in write mode
    with open('tournament_slugs.csv', 'w', newline='') as csvfile:
        # Create a CSV writer object
        csvwriter = csv.writer(csvfile)

        # Write the header row
        csvwriter.writerow(['tournament_slugs', 'year_of_tournament'])

        # Write formatted tournament slugs and years to the CSV file
        for tournament in tournaments:
            formatted_slug = format_tournament_slug(tournament['slug'])
            year = get_year_from_slug(tournament['slug'])
            csvwriter.writerow([formatted_slug, year])

def get_team_ids_from_tournament(tournament_id):
    global tournaments_slug 

    # Use a set to store team IDs to avoid duplicates
    team_ids = set()

    # Iterate through the tournaments and collect team IDs
    for tournament in tournaments:
        if tournament['id'] == tournament_id:
            tournaments_slug = tournament['slug']
            for stage in tournament['stages']:
                for section in stage['sections']:
                    for match in section['matches']:
                        for team in match['teams']:
                            id = id_to_name(team['id'])
                            team_ids.add(id)

    return list(team_ids)

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
    
    return list(teams)

def tournament_slug_to_id(slug):
    global tournaments_slug 

    # Iterate through the tournaments and collect team IDs
    for tournament in tournaments:
        if tournament['slug'] == slug:
            return tournament['id']
    
    # if not found
    return None

if __name__ == "__main__":
    # team_ids = get_team_ids_from_tournament('110733838935136200')
    # print("Team IDs for Tournaments: ", tournaments_slug)
    # print(team_ids)

    # print('\n')

    # # teams = get_team_ids_from_leagues('109518549825754242')
    # teams = get_team_ids_from_leagues('98767991299243165')
    # print("Team IDs for Leagues: ", league_name)
    # print(teams)

    id = tournament_slug_to_id("lla_closing_2020")
    team_list = get_team_ids_from_tournament(id)
    print(team_list)