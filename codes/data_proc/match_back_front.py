import csv

# Reading the first CSV and storing the Composite Score by team_name
composite_scores = {}
with open('D:\\Coding\\LOL_Ranking\\result\\scaled_team_rankings.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        composite_scores[row['Team Name']] = float(row['Scaled Composite Score'])  # changed to float for sorting

# Reading the second CSV, updating the team_combat_capacity if the team_name matches
updated_rows = []
with open('D:\\Coding\\LOL_Ranking\\result\\match_src.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    fieldnames = csv_reader.fieldnames
    for row in csv_reader:
        if row['team_name'] in composite_scores:
            row['team_combat_capacity'] = composite_scores[row['team_name']]
        else:
            print(f"Team {row['team_name']} not found in the first CSV.")
            row['team_combat_capacity'] = ''  # clearing the value if team not found
        updated_rows.append(row)

# Sorting the teams by team_combat_capacity and redo the rank
updated_rows.sort(key=lambda x: float(x['team_combat_capacity']) if x['team_combat_capacity'] else 0, reverse=True)
for i, row in enumerate(updated_rows):
    row['Rank'] = i + 1  # adding new rank column

# Adding Rank to fieldnames
fieldnames.append('Rank')

# Writing the updated data to a new CSV file
with open('D:\\Coding\\LOL_Ranking\\result\\real_final.csv', mode='w', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(updated_rows)

print("Data updated, re-ranked, and saved to updated_second.csv")
