import csv

def count_cse_branches(filename):
  """Counts the number of branches for first-year CSE students in a CSV file.

  Args:
    filename: The name of the CSV file.

  Returns:
    The number of CSE branches.
  """

  branch_count = 0
  with open(filename, 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    # Skip header row
    next(reader)

    for row in reader:
      # Check if the row is for 'Computer Science Engineering'
      if row['Designation'] == 'YEAR 1' and row['Attendee Code'].startswith('24E11A0'):
        branch_count += 1

  return branch_count

if __name__ == '__main__':
  filename = 'attendance_YEAR 1.csv'
  cse_branch_count = count_cse_branches(filename)
  print(f"Number of CSE branches in the first year: {cse_branch_count}")