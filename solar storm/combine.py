import os
import glob
import pandas as pd

# Define the path to the folder containing your CSV files
folder_path = "ind_files"

# Use glob to find all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Check if files are found
if len(csv_files) == 0:
    print("No CSV files found in the directory")
else:
    print(f"Files found: {csv_files}")

    # Create an empty list to store the dataframes
    df_list = []

    # Loop through all the CSV files and read them into DataFrames
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            df_list.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")

    # Combine all the DataFrames into a single DataFrame
    if df_list:
        merged_df = pd.concat(df_list, ignore_index=True)
        print("Files merged successfully")

        # Save the merged DataFrame to a new CSV file
        merged_df.to_csv("merged_storm_data.csv", index=False)
        print("Merged data saved to 'merged_storm_data.csv'")
    else:
        print("No valid CSV files to merge.")
