# import the modules
import os
# module to read CSV files
import csv

# set the path for the file
csvpath = os.path.join("budget_data.csv")

# opened the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # read the header row of the file
    csv_header = next(csvreader)

    # to print header
    # print(f"CSV Header: {csv_header}")

    # total begins at zero
    total = 0
    monthsProfits = []
    # reader = csv.reader(bankData)
    for row in csvreader:
        total += int(row[1])
        # monthsProfits.append(int(row[1]))
        monthProfit = [row[0], int(row[1])]
        monthsProfits.append(monthProfit)

    # average of changes of profits/losses
    monthDifferences = []
    for idx, row in enumerate(monthsProfits):
        # print(row, idx) 
        # 867884 , 0
        #If the index plus 1 is less than the number of months 
        if (idx + 1) < len(monthsProfits):
            current = monthsProfits[idx][1]
            next = monthsProfits[idx + 1][1]
            monthDifferences.append(int(next - current))

    # gives a list of all of the differences (changes) between the months
    # now, find average by adding all of the numbers in the list
    # and dividing by the length of the list
    avgMonthlyDifferencesTotal = 0
    for monthDifference in monthDifferences:
        avgMonthlyDifferencesTotal += monthDifference



    print("Financial Analysis")

    print("-------------------------")

    # count the rows of data to see how many months
    # subtract the header row
    count = len(open(csvpath).readlines())
    print("Total Months:", str(count - 1))

    print(f"Total: ${str(total)}")

    avgChange = avgMonthlyDifferencesTotal / len(monthDifferences)
    print(f"Average Change: ${round(avgChange, 2)}")
    
    # calculate the average of the changes in profit/losses
    #bankAverage = (total / count)
    #print(bankAverage)





