import csv

filename = 'E1--BHARAT-INST--OF-ENGG--AND-TECH-218043_Attendance Status report - Hierarchy Format_20241004154258_20241004154448.csv'
attendance_by_year = {}
with open(filename, 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    # Skip the initial report details rows
    for _ in range(2):
        next(reader)

    for row in reader:
        year = row['Designation']
        attendee_data = {
            'Attendee ID': row['Attendee ID'],
            'Attendee Code': row['Attendee Code'],
            'Attendee Name': row['Attendee Name'],
            'Mobile No': row['Mobile No'],
            'Designation': row['Designation'],
            '2024-October-04': row['2024-October-04'],
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
# print(attendance_by_year['YEAR 1'])
# print(attendance_by_year['YEAR 2'])
# print(attendance_by_year['YEAR 3'])
# print(attendance_by_year['YEAR 4'])
#print(attendance_by_year['YEAR 1'])
students = attendance_by_year['YEAR 1']
print(students)
print(type(students))
print(len(students))
students = sorted(students, key=lambda k: k['Attendee Code'])

for student in students:
    print(student['Attendee Code'])

# attendees = sorted(attendees, key=lambda k: k['Attendee ID'])

