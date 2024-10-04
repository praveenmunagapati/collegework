import pandas as pd
from datetime import datetime

# File paths
csv_file_path = "E1--BHARAT-INST--OF-ENGG--AND-TECH-218043_Attendance Status report - Hierarchy Format_20241004154258_20241004154448.csv"
output_excel_path = "III_YR_Biometric_Attendance_{date}.xlsx".format(date=datetime.today().strftime('%d-%m-%Y'))

print(f"Reading CSV file: {csv_file_path}")

# Step 1: Read the CSV file (skiprows=4 was included based on assumption)
attendance_df = pd.read_csv(csv_file_path, skiprows=4)

# Step 2: Display the first few rows to verify the data
print("\nInitial data from the CSV file:")
print(attendance_df.head())

# Step 3: Display column names to understand the structure
print("\nColumns in the CSV file:")
for i in range(len(attendance_df.columns)):
    print(i,attendance_df.columns[i])
