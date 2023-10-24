import csv

# Read the CSV file and extract the Composite Score column
filename = 'D:\\Coding\\LOL_Ranking\\result\\team_rankings.csv'  # specify your file name
team_names = []
composite_scores = []
ranks = []

with open(filename, mode ='r') as file:
    csvReader = csv.reader(file)
    headers = next(csvReader)  # skip the header
    for row in csvReader:
        team_names.append(row[0])
        composite_scores.append(float(row[1]))  # convert to float for computation
        ranks.append(int(row[2]))  # convert to int for computation

# Calculate the min and max of Composite Score
min_original = min(composite_scores)
max_original = max(composite_scores)

# Target range
min_scaled = 0
max_scaled = 1000

# Scale the Composite Score to the range of 0-1000
scaled_scores = [(x - min_original) / (max_original - min_original) * (max_scaled - min_scaled) + min_scaled for x in composite_scores]

# Print the team names with their scaled scores and ranks
print("Team Name, Scaled Composite Score, Rank")
for team, score, rank in zip(team_names, scaled_scores, ranks):
    print(f"{team}, {score:.2f}, {rank}")

# If you want to write the scaled scores back to a new CSV file:
scaled_ranking_file = 'D:\\Coding\\LOL_Ranking\\result\\scaled_team_rankings.csv'
with open(scaled_ranking_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Team Name', 'Scaled Composite Score', 'Rank'])  # writing headers
    
    for team, score, rank in zip(team_names, scaled_scores, ranks):
        writer.writerow([team, f"{score:.2f}", rank])

front_file = 'D:\\Coding\\LOL_Ranking\\output\\front_end_data_13c_version.csv'