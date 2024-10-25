import csv

filename = 'E1--BHARAT-INST--OF-ENGG--AND-TECH-218043_Attendance Status report - Hierarchy Format_20241025154231_20241025154458.csv'
attendance_by_year = {}
with open(filename, 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    # Skip the initial report details rows
    for row in reader:
        year = row['Designation']
        keys = row.keys()
        # print(type(keys))
        # print(type(list(keys)[16]))

        attendee_data = {
            'Attendee ID': row['Attendee ID'],
            'Attendee Code': row['Attendee Code'],
            'Attendee Name': row['Attendee Name'],
            'Mobile No': row['Mobile No'],
            'Designation': row['Designation'],
            '2024-October-04': row[list(keys)[16]],#compute date format after the csv read
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

        if year in attendance_by_year:
            attendance_by_year[year].append(attendee_data)
        else:
            attendance_by_year[year] = [attendee_data]

    attendance_by_year
# Print the attendance data for each year
# for year, attendees in attendance_by_year.items():
#     print(f"\nAttendance for {year}:")
#     for attendee in attendees:
#         print(attendee)
for year, attendees in attendance_by_year.items():
        output_filename = f"attendance_{year}.csv"
        with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
            fieldnames = attendees[0].keys()
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()
            attendees = sorted(attendees, key=lambda k: k['Attendee Code'])
            writer.writerows(attendees)

        print(f"Attendance data for {year} saved to '{output_filename}'")
