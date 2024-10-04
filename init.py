import pandas as pd
from datetime import datetime
import re  # To help extract the year number

# File paths
csv_file_path = "E1--BHARAT-INST--OF-ENGG--AND-TECH-218043_Attendance Status report - Hierarchy Format_20241004154258_20241004154448.csv"

print(f"Reading CSV file: {csv_file_path}")

# Step 1: Read the CSV file (assuming first 4 rows are headers that need to be skipped)
attendance_df = pd.read_csv(csv_file_path, skiprows=4)

# Step 2: Extract columns 12 to 17 (zero-indexed, so 12 is index 11)
selected_columns = attendance_df.iloc[:, 11:17]

# Step 3: Assign meaningful column names (if necessary)
selected_columns.columns = ['Attendee ID', 'Attendee Code', 'Attendee Name', 'Mobile No', 'Year', 'Attendance Status']

# Step 4: Display the extracted columns to verify
print("\nSelected columns (12 to 17):")
print(selected_columns.head())

# Step 5: Clean the 'Year' column by extracting the numeric part (e.g., "YEAR 4" -> 4)
selected_columns['Year'] = selected_columns['Year'].apply(lambda x: int(re.search(r'\d+', x).group()))

# Step 6: Separate data by the 'Year' column
for year in selected_columns['Year'].unique():
    # Filter data for the current year
    year_data = selected_columns[selected_columns['Year'] == year]

    # Generate an Excel file for each year
    output_excel_path = f"Attendance_Year_{year}_{datetime.today().strftime('%d-%m-%Y')}.xlsx"

    print(f"\nSaving data for Year {year} to {output_excel_path}...")

    # Save the data to an Excel file for each year
    year_data.to_excel(output_excel_path, index=False)

print("\nAll year-wise attendance reports have been generated.")
