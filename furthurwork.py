# import csv
# import os
#
# # File paths and initialization
# filename = 'E1--BHARAT-INST--OF-ENGG--AND-TECH-218043_Attendance Status report - Hierarchy Format_20241025154231_20241025154458.csv'
# attendance_by_year = {}
#
# # JNTUH branch codes dictionary
# jntuh_branches = {
#     '01': 'Civil Engineering',
#     '02': 'Electrical and Electronics Engineering',
#     '03': 'Mechanical Engineering',
#     '04': 'Electronics and Communication Engineering',
#     '05': 'Computer Science and Engineering',
#     '06': 'Chemical Engineering',
#     '07': 'Electronics and Instrumentation Engineering',
#     '08': 'Biotechnology',
#     '12': 'Information Technology',
#     '14': 'Aeronautical Engineering',
#     '17': 'Automobile Engineering',
#     '19': 'Mining Engineering',
#     '21': 'Metallurgical Engineering',
#     '22': 'Agricultural Engineering',
#     '23': 'Petroleum Engineering'
# }
#
# # Read the CSV file and process data by year
# with open(filename, 'r', encoding='utf-8-sig') as csvfile:
#     reader = csv.DictReader(csvfile)
#
#     for row in reader:
#         year = row['Designation']
#         attendee_data = {
#             'Attendee ID': row['Attendee ID'],
#             'Attendee Code': row['Attendee Code'],
#             'Attendee Name': row['Attendee Name'],
#             'Mobile No': row['Mobile No'],
#             'Designation': row['Designation'],
#             '2024-October-04': row[list(row.keys())[16]],  # Adjusting for date format
#             'Total Days': row['Total Days'],
#             'TotalHolidays': row['TotalHolidays'],
#             'WorkingDays': row['WorkingDays'],
#             'Fullday Present': row['Fullday Present'],
#             'HalfDay Present': row['HalfDay Present'],
#             'Errors': row['Errors'],
#             'Total Absents': row['Total Absents'],
#             'Total Leaves': row['Total Leaves'],
#             'Week Offs': row['Week Offs'],
#             'On Duty': row['On Duty'],
#             'Eligible Days': row['Eligible Days'],
#             'Attendance%': row['Attendance%'],
#         }
#
#         # Organize data by year and branch
#         if year == "1st Year":
#             if year not in attendance_by_year:
#                 attendance_by_year[year] = {}
#
#             branch_code = row['Attendee Code'][:2]
#             branch_name = jntuh_branches.get(branch_code, "Unknown Branch")
#
#             if branch_name not in attendance_by_year[year]:
#                 attendance_by_year[year][branch_name] = []
#
#             attendance_by_year[year][branch_name].append(attendee_data)
#         else:
#             # For other years, initialize as a list if not already done
#             if year not in attendance_by_year:
#                 attendance_by_year[year] = []
#             attendance_by_year[year].append(attendee_data)
#
# # Save the attendance data to separate CSV files
# for year, data in attendance_by_year.items():
#     if year == "1st Year":
#         for branch, attendees in data.items():
#             output_filename = f"attendance_1stYear_{branch}.csv"
#             with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
#                 fieldnames = attendees[0].keys()
#                 writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#                 writer.writeheader()
#                 attendees = sorted(attendees, key=lambda k: k['Attendee Code'])
#                 writer.writerows(attendees)
#             print(f"Attendance data for 1st Year {branch} saved to '{output_filename}'")
#     else:
#         output_filename = f"attendance_{year}.csv"
#         with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
#             fieldnames = data[0].keys()
#             writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#             writer.writeheader()
#             data = sorted(data, key=lambda k: k['Attendee Code'])
#             writer.writerows(data)
#         print(f"Attendance data for {year} saved to '{output_filename}'")
import csv
import os

# File paths and initialization
filename = 'E1--BHARAT-INST--OF-ENGG--AND-TECH-218043_Attendance Status report - Hierarchy Format_20241025154231_20241025154458.csv'
attendance_by_year = {}

# JNTUH branch codes dictionary
jntuh_branches = {
    '01': 'Civil Engineering',
    '02': 'Electrical and Electronics Engineering',
    '03': 'Mechanical Engineering',
    '04': 'Electronics and Communication Engineering',
    '05': 'Computer Science and Engineering',
    '06': 'Chemical Engineering',
    '07': 'Electronics and Instrumentation Engineering',
    '08': 'Biotechnology',
    '12': 'Information Technology',
    '14': 'Aeronautical Engineering',
    '17': 'Automobile Engineering',
    '19': 'Mining Engineering',
    '21': 'Metallurgical Engineering',
    '22': 'Agricultural Engineering',
    '23': 'Petroleum Engineering'
}

# Read the CSV file and process data by year
# with open(filename, 'r', encoding='utf-8-sig') as csvfile:
#     reader = csv.DictReader(csvfile)
#
#     for row in reader:
#         year = row['Designation']
#         attendee_data = {
#             'Attendee ID': row['Attendee ID'],
#             'Attendee Code': row['Attendee Code'],
#             'Attendee Name': row['Attendee Name'],
#             'Mobile No': row['Mobile No'],
#             'Designation': row['Designation'],
#             '2024-October-04': row[list(row.keys())[16]],  # Adjusting for date format
#             'Total Days': row['Total Days'],
#             'TotalHolidays': row['TotalHolidays'],
#             'WorkingDays': row['WorkingDays'],
#             'Fullday Present': row['Fullday Present'],
#             'HalfDay Present': row['HalfDay Present'],
#             'Errors': row['Errors'],
#             'Total Absents': row['Total Absents'],
#             'Total Leaves': row['Total Leaves'],
#             'Week Offs': row['Week Offs'],
#             'On Duty': row['On Duty'],
#             'Eligible Days': row['Eligible Days'],
#             'Attendance%': row['Attendance%'],
#         }
#
#         # Organize data by year and branch
#         if year == "1st Year":
#             if year not in attendance_by_year:
#                 attendance_by_year[year] = {}
#
#             branch_code = row['Attendee Code'][:2]
#             branch_name = jntuh_branches.get(branch_code, "Unknown Branch")
#
#             if branch_name not in attendance_by_year[year]:
#                 attendance_by_year[year][branch_name] = []
#
#             attendance_by_year[year][branch_name].append(attendee_data)
#         else:
#             # For other years, initialize as a list if not already done
#             if year not in attendance_by_year:
#                 attendance_by_year[year] = []
#             attendance_by_year[year].append(attendee_data)
#
# # Save the attendance data to separate CSV files
# for year, data in attendance_by_year.items():
#     if year == "1st Year":
#         for branch, attendees in data.items():
#             # Sort attendees by 'Attendee Code' for each branch
#             attendees_sorted = sorted(attendees, key=lambda k: k['Attendee Code'])
#
#             output_filename = f"attendance_1stYear_{branch}.csv"
#             with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
#                 fieldnames = attendees_sorted[0].keys()
#                 writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#                 writer.writeheader()
#                 writer.writerows(attendees_sorted)
#             print(f"Attendance data for 1st Year {branch} saved to '{output_filename}'")
#     else:
#         output_filename = f"attendance_{year}.csv"
#         data_sorted = sorted(data, key=lambda k: k['Attendee Code'])
#         with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
#             fieldnames = data_sorted[0].keys()
#             writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(data_sorted)
#         print(f"Attendance data for {year} saved to '{output_filename}'")

# import csv
# import os
#
# # File paths and initialization
# filename = 'E1--BHARAT-INST--OF-ENGG--AND-TECH-218043_Attendance Status report - Hierarchy Format_20241025154231_20241025154458.csv'
# attendance_by_year = {}
#
# # JNTUH branch codes dictionary
# jntuh_branches = {
#     '01': 'Civil Engineering',
#     '02': 'Electrical and Electronics Engineering',
#     '03': 'Mechanical Engineering',
#     '04': 'Electronics and Communication Engineering',
#     '05': 'Computer Science and Engineering',
#     '06': 'Chemical Engineering',
#     '07': 'Electronics and Instrumentation Engineering',
#     '08': 'Biotechnology',
#     '12': 'Information Technology',
#     '14': 'Aeronautical Engineering',
#     '17': 'Automobile Engineering',
#     '19': 'Mining Engineering',
#     '21': 'Metallurgical Engineering',
#     '22': 'Agricultural Engineering',
#     '23': 'Petroleum Engineering'
# }
#
# # Additional specific branches
# specific_codes = {
#     'A0': 'CSE',
#     'A1': 'IT',
#     'A6': 'DS'
# }
#
# # Read the CSV file and process data by year
# with open(filename, 'r', encoding='utf-8-sig') as csvfile:
#     reader = csv.DictReader(csvfile)
#
#     for row in reader:
#         year = row['Designation']
#         attendee_data = {
#             'Attendee ID': row['Attendee ID'],
#             'Attendee Code': row['Attendee Code'],
#             'Attendee Name': row['Attendee Name'],
#             'Mobile No': row['Mobile No'],
#             'Designation': row['Designation'],
#             '2024-October-04': row[list(row.keys())[16]],  # Adjusting for date format
#             'Total Days': row['Total Days'],
#             'TotalHolidays': row['TotalHolidays'],
#             'WorkingDays': row['WorkingDays'],
#             'Fullday Present': row['Fullday Present'],
#             'HalfDay Present': row['HalfDay Present'],
#             'Errors': row['Errors'],
#             'Total Absents': row['Total Absents'],
#             'Total Leaves': row['Total Leaves'],
#             'Week Offs': row['Week Offs'],
#             'On Duty': row['On Duty'],
#             'Eligible Days': row['Eligible Days'],
#             'Attendance%': row['Attendance%'],
#         }
#
#         # Organize data by year and branch
#         if year == "1st Year":
#             if year not in attendance_by_year:
#                 attendance_by_year[year] = {}
#
#             # Check if 'Attendee Code' starts with a specific code
#             branch_code = row['Attendee Code'][:2]
#             if branch_code in specific_codes:
#                 branch_name = specific_codes[branch_code]
#             else:
#                 branch_name = jntuh_branches.get(branch_code, "Unknown Branch")
#
#             if branch_name not in attendance_by_year[year]:
#                 attendance_by_year[year][branch_name] = []
#
#             attendance_by_year[year][branch_name].append(attendee_data)
#         else:
#             # For other years, initialize as a list if not already done
#             if year not in attendance_by_year:
#                 attendance_by_year[year] = []
#             attendance_by_year[year].append(attendee_data)
#
# # Save the attendance data to separate CSV files
# for year, data in attendance_by_year.items():
#     if year == "1st Year":
#         for branch, attendees in data.items():
#             # Sort attendees by 'Attendee Code' for each branch
#             attendees_sorted = sorted(attendees, key=lambda k: k['Attendee Code'])
#
#             output_filename = f"attendance_1stYear_{branch}.csv"
#             with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
#                 fieldnames = attendees_sorted[0].keys()
#                 writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#                 writer.writeheader()
#                 writer.writerows(attendees_sorted)
#             print(f"Attendance data for 1st Year {branch} saved to '{output_filename}'")
#     else:
#         output_filename = f"attendance_{year}.csv"
#         data_sorted = sorted(data, key=lambda k: k['Attendee Code'])
#         with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
#             fieldnames = data_sorted[0].keys()
#             writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(data_sorted)
#         print(f"Attendance data for {year} saved to '{output_filename}'")

import csv
import os

# File paths and initialization
filename = 'E1--BHARAT-INST--OF-ENGG--AND-TECH-218043_Attendance Status report - Hierarchy Format_20241025154231_20241025154458.csv'
attendance_by_year = {}
cse_students = []  # Separate list for 1st-year CSE students (Attendee Code containing "A0")

# JNTUH branch codes dictionary for remaining branches
jntuh_branches = {
    '01': 'Civil Engineering',
    '02': 'Electrical and Electronics Engineering',
    '03': 'Mechanical Engineering',
    '04': 'Electronics and Communication Engineering',
    '05': 'Computer Science and Engineering',
    '06': 'Chemical Engineering',
    '07': 'Electronics and Instrumentation Engineering',
    '08': 'Biotechnology',
    '12': 'Information Technology',
    '14': 'Aeronautical Engineering',
    '17': 'Automobile Engineering',
    '19': 'Mining Engineering',
    '21': 'Metallurgical Engineering',
    '22': 'Agricultural Engineering',
    '23': 'Petroleum Engineering'
}

# Read the CSV file and process data by year
with open(filename, 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        year = row['Designation']
        attendee_data = {
            'Attendee ID': row['Attendee ID'],
            'Attendee Code': row['Attendee Code'],
            'Attendee Name': row['Attendee Name'],
            'Mobile No': row['Mobile No'],
            'Designation': row['Designation'],
            '2024-October-04': row[list(row.keys())[16]],  # Adjusting for date format
            'Total Days': row['Total Days'],
            'TotalHolidays': row['TotalHolidays'],
            'WorkingDays': row['WorkingDays'],
            'Fullday Present': row['Fullday Present'],
            'HalfDay Present': row['HalfDay Present'],
            'Errors': row['Errors'],
            'Total Absents': row['Total Absents'],
            'Total Leaves': row['Total Leaves'],
            'Week Offs': row['Week Offs'],
            'On Duty': row['On Duty'],
            'Eligible Days': row['Eligible Days'],
            'Attendance%': row['Attendance%'],
        }

        # Separate out 1st-year CSE students (Attendee Code containing "A0")
        if year == "1st Year" and "A0" in row['Attendee Code']:
            cse_students.append(attendee_data)
            continue  # Skip adding this to other branches

        # Organize data by year and branch
        if year == "1st Year":
            if year not in attendance_by_year:
                attendance_by_year[year] = {}

            # Determine branch based on JNTUH codes for remaining branches
            branch_code = row['Attendee Code'][10:12]  # Adjusting for branch code position in Attendee Code
            branch_name = jntuh_branches.get(branch_code, "Unknown Branch")

            if branch_name not in attendance_by_year[year]:
                attendance_by_year[year][branch_name] = []

            attendance_by_year[year][branch_name].append(attendee_data)
        else:
            # For other years, initialize as a list if not already done
            if year not in attendance_by_year:
                attendance_by_year[year] = []
            attendance_by_year[year].append(attendee_data)

# Save the attendance data to separate CSV files
for year, data in attendance_by_year.items():
    if year == "1st Year":
        for branch, attendees in data.items():
            # Sort attendees by 'Attendee Code' for each branch
            attendees_sorted = sorted(attendees, key=lambda k: k['Attendee Code'])

            output_filename = f"attendance_1stYear_{branch}.csv"
            with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
                fieldnames = attendees_sorted[0].keys()
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(attendees_sorted)
            print(f"Attendance data for 1st Year {branch} saved to '{output_filename}'")
    else:
        output_filename = f"attendance_{year}.csv"
        data_sorted = sorted(data, key=lambda k: k['Attendee Code'])
        with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
            fieldnames = data_sorted[0].keys()
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_sorted)
        print(f"Attendance data for {year} saved to '{output_filename}'")

# Save the CSE students (Attendee Code containing "A0") to their own CSV file
if cse_students:
    cse_output_filename = "attendance_1stYear_CSE.csv"
    with open(cse_output_filename, 'w', newline='', encoding='utf-8-sig') as cse_file:
        fieldnames = cse_students[0].keys()
        writer = csv.DictWriter(cse_file, fieldnames=fieldnames)
        writer.writeheader()
        cse_students_sorted = sorted(cse_students, key=lambda k: k['Attendee Code'])
        writer.writerows(cse_students_sorted)
    print(f"Attendance data for 1st Year CSE (Attendee Code containing 'A0') saved to '{cse_output_filename}'")
