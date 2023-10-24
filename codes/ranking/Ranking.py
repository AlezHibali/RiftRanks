# Importing necessary libraries
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# Load datasets for multiple years for teams and players
teams = []
players = []
for year in range(2021, 2024):
    teams.append(pd.read_csv(f'D:\\Coding\\LOL_Ranking\\ranking_raw\\team_{year}.csv').assign(year=year))
    players.append(pd.read_csv(f'D:\\Coding\\LOL_Ranking\\ranking_raw\\player_{year}.csv').assign(year=year))

team_data = pd.concat(teams, ignore_index=True)
player_data = pd.concat(players, ignore_index=True)

# Remove rows with blank 'team_name' in both datasets
team_data = team_data.dropna(subset=['team_name'])
player_data = player_data.dropna(subset=['team_name'])

# Assign weights based on the year
weights = {2021: 0.2, 2022: 0.5, 2023: 1}
player_data['weight'] = player_data['year'].map(weights)

# Aggregate player data by team with consideration of weights
player_data_grouped = player_data.groupby('team_name').apply(lambda x: pd.Series({
    'weighted_killCount': (x['killCount'] * x['weight']).sum(),
    'weighted_victimCount': (x['victimCount'] * x['weight']).sum(),
    'weighted_wardKilledCount': (x['wardKilledCount'] * x['weight']).sum(),
    'weighted_wardPlacedCount': (x['wardPlacedCount'] * x['weight']).sum()
})).reset_index()

# Merge team and aggregated player data
team_data_latest = team_data.drop_duplicates('team_name', keep='last')  # Keep the latest year’s team data
full_team_data = pd.merge(team_data_latest, player_data_grouped, on='team_name', how='left')

# Select relevant features for PCA and include weighted features
features = [
    'building_destroyed', 'destroyed_opponent_buildings', 'champion_kill',
    'baron_kill', 'riftHerald_kill', 'dragon_kill', 'ward_killed', 'ward_placed',
    'weighted_killCount', 'weighted_victimCount', 'weighted_wardKilledCount', 'weighted_wardPlacedCount'
]
full_team_data_selected = full_team_data[features]

# Impute missing values with mean
imputer = SimpleImputer(strategy='mean')
full_team_data_imputed = pd.DataFrame(imputer.fit_transform(full_team_data_selected), columns=features)

# Normalize the data
full_team_data_normalized = (full_team_data_imputed - full_team_data_imputed.mean()) / full_team_data_imputed.std()

# Apply PCA
pca = PCA(n_components=2)
team_pca = pca.fit_transform(full_team_data_normalized)

# Create DataFrame to hold PCA and original data for ranking
team_pca_df = pd.DataFrame(data=team_pca, columns=['PC1', 'PC2'])
team_ranking = pd.concat([full_team_data[['team_name']], team_pca_df], axis=1)

# Calculate composite score based on the explained variance ratios
explained_variance_ratios = pca.explained_variance_ratio_
team_ranking['Composite Score'] = (explained_variance_ratios[0] * team_ranking['PC1'] +
                                   explained_variance_ratios[1] * team_ranking['PC2'])

# Sort by composite score
team_ranking_sorted = team_ranking.sort_values(by='Composite Score', ascending=False)

# Assign rank
team_ranking_sorted['Rank'] = range(1, len(team_ranking_sorted) + 1)

# Print the result
print(team_ranking_sorted[['team_name', 'Composite Score', 'Rank']])

# Save to CSV
team_ranking_sorted[['team_name', 'Composite Score', 'Rank']].to_csv('D:\\Coding\\LOL_Ranking\\result\\team_rankings.csv', index=False)

# Plotting the PCA results
plt.figure(figsize=(10,7))
plt.scatter(team_ranking_sorted['PC1'], team_ranking_sorted['PC2'], c='blue', label='Teams')
for i, txt in enumerate(team_ranking_sorted['team_name']):
    plt.annotate(txt, (team_ranking_sorted['PC1'].iloc[i], team_ranking_sorted['PC2'].iloc[i]))
plt.title('PCA Results with Composite Scores')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.legend()
plt.grid(True)
plt.show()
