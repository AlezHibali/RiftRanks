import json

def extract_platform_game_ids(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    platform_game_ids = [entry['platformGameId'].replace('_', ':') for entry in data]
    return platform_game_ids

if __name__ == "__main__":
    json_file_path = '../../src/data/mapping_data.json'
    
    platform_game_ids = extract_platform_game_ids(json_file_path)
    
    print("Modified Platform Game IDs:", platform_game_ids)
