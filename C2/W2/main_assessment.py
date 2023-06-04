#!/usr/bin/env python3
 
import csv

def read_employees(csv_file_location):
    # Register the dialect
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

    # Open the CSV file and create a reader object
    with open(csv_file_location) as file:
        employee_file = csv.DictReader(file, dialect='empDialect')

        # Initialize an empty list to store the employee data
        employee_list = []

        # Iterate over each row in the CSV file
        for data in employee_file:
            # Append the row (dictionary) to the employee list
            employee_list.append(data)

    return employee_list

# Test the function
employee_list = read_employees('employees.csv')
#print(employee_list)
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data

dictionary = process_data(employee_list)
#print(dictionary)

def write_report(dictionary, report_file):
    with open(report_file, 'w+') as f:
        for k in sorted(dictionary):
            f.write(str(k) +':'+str(dictionary[k])+'\n')
        f.close()
write_report(dictionary, 'test_report.txt')

