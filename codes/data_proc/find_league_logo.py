import json
import csv

# Load the JSON data from the file
with open('D:\Coding\LOL_Ranking\inc\leagues.json', 'r') as file_leagues:
    leagues = json.load(file_leagues)

# Create a dictionary to hold the team_id as key and name, acronym as value
league_mapping = {}

for league in leagues:
    league_id = league['name']
    image = league['image']
    image_d = league['darkImage']
    image_l = league['lightImage']
    
    # Store the name and acronym in the dictionary, indexed by team_id
    league_mapping[league_id] = {'image': image, 'darkImage': image_d, 'lightImage': image_l}

# Now, write the league_mapping dictionary to a CSV file
csv_file = 'leagues.csv'

# Add error handling to manage potential file writing errors
try:
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['League Name', 'Image', 'Dark Image', 'Light Image'])

        # Write the data rows
        for league_name, images in league_mapping.items():
            writer.writerow([league_name, images['image'], images['darkImage'], images['lightImage']])
except Exception as e:
    print(f"Error writing to CSV file: {e}")

print(f"Data written to {csv_file}")