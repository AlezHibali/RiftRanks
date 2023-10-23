import pandas as pd

def main():
    # Read the CSV file
    df = pd.read_csv('./real_final.csv')

    # Define the columns to be normalized and their corresponding maximum and minimum values
    columns_to_normalize = ["champion_kills_per_game", "first_baron_rate", "winning_rate",
                            "net_building_destroyed_per_game", "epic_monster_killed_per_game", "vision_scores_per_game"]

    max_values = [22.71, 1, 1, 7.8, 5.67, 205.11]
    min_values = [5, 0, 0, -11.21, 0.75, 71.6]

    # Normalize the specified columns between 0 and 1000
    for column, max_val, min_val in zip(columns_to_normalize, max_values, min_values):
        df[column] = ((df[column] - min_val) / (max_val - min_val)) * 100

    # Save the normalized data back to a new CSV file
    df.to_csv('normalized_data.csv', index=False)

if __name__ == "__main__":
    main()