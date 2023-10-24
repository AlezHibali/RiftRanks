import csv

# Open the input CSV file in read mode and create a new CSV file in write mode for the cleaned data
with open('D:\\Coding\\LOL_Ranking\\output\\front_end_data_13c_version.csv', mode='r') as infile, open('D:\\Coding\\LOL_Ranking\\output\\bzd.csv', mode='w', newline='') as outfile:
    # Create a CSV reader and writer object
    csvreader = csv.reader(infile)
    csvwriter = csv.writer(outfile)

    # Write the header row to the cleaned CSV file
    headers = next(csvreader)
    csvwriter.writerow(headers)

    # Iterate through each row in the input CSV file
    for row in csvreader:
        # Check if the team_name is missing or null, if yes then skip the row
        if not row[0] or row[0].lower() == 'null':
            continue

        # Check if the team_capital_letter is not A-Z, if yes then change it to "#"
        if not row[9].isalpha() or not row[9].isupper() or len(row[9]) != 1:
            row[9] = "#"

        # Multiply the team_combat_capacity by 1000
        try:
            row[10] = str(int(float(row[10].strip()) * 1000))
        except ValueError:
            print(f"Error converting '{row[10]}' to integer.")

        # Write the cleaned and modified row to the cleaned CSV file
        csvwriter.writerow(row)

print("Cleaning completed and data written to cleaned.csv")
