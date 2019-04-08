# - import data table DONE
# - make dataframe/structure to iterate thru DONE (dict)
# - make calcPay to calculate pay from hours
# - iterate over data
# using calcPay function to
# write to a string the names &
# salaries on each line
# - export string to text file

import csv

# import data from csv into a dictionary as header keys and value lists
reader = csv.DictReader(open('EmployeePayTable.csv'))
d = {}
for row in reader:
    for column, value in row.items():
        d.setdefault(column, []).append(value)
print(d)

def calcPay(hrs,rate):
    base_pay = hrs * rate
    overtime = 0
    if (hrs > 40):
        overtime += (hrs-40)*(rate/2)
    return base_pay + overtime

def print_overtime_list(dictIn):
    for i in range(len(dictIn['ID Number'])):
        temp = ""
        temp += dictIn['Name'][i] + ", "
        temp += str(calcPay(
            int(dictIn['Hours Worked'][i]),
            float(dictIn['Pay Rate'][i].strip("$"))
            ))
        print(temp)

print_overtime_list(d)

# RESEARCH FOR STEP 1

#import pandas as pd
#df= pd.read_excel("EmployeePayTable.xlsx")
#print("Column headings:")
#print(df.columns)

"""import csv
import pprint

d.fromkeys(["ID Number",
            "Name",
            "Pay Rate",
            "Hours Worked"])

with open('EmployeePayTable.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        line_count += 1
        d.append(row)
    print(f'Processed {line_count} lines.')

pprint.pprint(d)"""

#input_file = csv.DictReader(open("EmployeePayTable.csv"))
#for row in input_file:
#    print(row)

"""reader = csv.reader(open('EmployeePayTable.csv', 'r'))
d = {}
for row in reader:
   k, v = row
   d[k] = v"""

#for (k, v) in d.items():
#    print(k, v)

"""with open('EmployeePayTable.csv') as f:
    d = dict(filter(None, csv.reader(f)))

print(d)"""
