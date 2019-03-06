# import the modules
import os
# module to read CSV files
import csv

# set the path for the file
csvpath = os.path.join("budget_data.csv")
    

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # read the header row of the file
    csv_header = next(csvreader)
    # print the header
    print(f"CSV Header: {csv_header}")


    total = 0
    #eader = csv.reader(bankData)
    for row in csvreader:
        total += int(row[1])

    print('total')
    print(total)



