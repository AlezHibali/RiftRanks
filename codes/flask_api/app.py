from flask import Flask, jsonify, request
from tournaments_to_teams import tournament_slug_to_id, get_team_ids_from_tournament

app = Flask(__name__)

def header_processing(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

def replace_spaces_and_lowercase(input_string):
    modified_string = input_string.replace("'", "").replace(" ", "_").lower()
    return modified_string

def team_list_from_tournament(tournament_slug):
    id = tournament_slug_to_id(tournament_slug)
    team_list = get_team_ids_from_tournament(id)
    return team_list

# API endpoint to get team names based on tournament name
# curl localhost:5000/api/get_teams?tournament_slug=lla-closing-2020
# curl 3.133.84.90/api/get_teams?tournament_slug=lla-closing-2020
@app.route('/api/get_teams', methods=['GET'])
def get_teams():
    tournament_name = request.args.get('tournament_slug')
    teams = team_list_from_tournament(tournament_name)
    return header_processing(jsonify(teams))

if __name__ == '__main__':
    app.run(debug=True)
